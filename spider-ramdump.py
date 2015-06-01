# mset_gspwn

import sys

from p3ds.util import *
from p3ds.ROP import *
from p3ds.app import *

def main(argv):
	app = Spider_4x()
	r = Spider_4x_ROP(app.rop_loc)
	
	# Set file object u64 offset to 0
	r.store_i32(0, app.file_handle + 4)
	r.store_i32(0, app.file_handle + 8)

	r.call(app.fopen + 4, [app.file_handle, Ref("fname"), 6], 4)
	r.call(app.fwrite + 4, [app.file_handle, app.file_handle + 0x20, 0x100000, 0x300000], 8)
	
	r.call_lr(app.svcSleepThread, [1000000000, 0x00000000])

	# Data.
	r.label("fname")
	r.data("dmc:/DUMP.BIN".encode('utf-16le') + "\x00\x00")
	
	rop = r.gen()
	
	with open(argv[1], "wb") as fl:
		fl.write(rop)

if __name__ == "__main__":
	main(sys.argv[1:])
	