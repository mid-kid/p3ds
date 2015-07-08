# 3DS ROP library (for DS user settings exploit).
# Copyright (C) 2013 naehrwert
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2.0.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License 2.0 for more details.
# 
# A copy of the GPL 2.0 should have been included with the program.
# If not, see http://www.gnu.org/licenses/

import struct

# Gadgets.
class Mset_4x_Gadget:
	# Register loads.
	_pop_pc = 0x001002F9
	_pop_r0_pc = 0x00143D8C
	_pop_r1_pc = 0x001C4FC4 #0x001549E1
	_pop_r2_pc = 0x0022952D
	_pop_r3_pc = 0x0010538C
	_pop_r4_pc = 0x001001ED #0x001B3AA0
	_pop_r4_to_r12_pc = 0x0018D5DC
	_pop_r4_lr_bx_r2 = 0x001D9360
	# Loads and stores.
	_ldr_r0_r0_pop_r4_pc = 0x0012FBBC
	_str_r1_r0_pop_r4_pc = 0x0010CCBC

class Mset_6x_Gadget:
	# Register loads.
	_pop_pc = 0x001002F9
	_pop_r0_pc = 0x00144CF8
	_pop_r1_pc = 0x001CD804
	_pop_r3_pc = 0x00105110
	_pop_r4_pc = 0x001001ED
	_pop_r4_to_r12_pc = 0x0018B184
	_pop_r4_lr_bx_r2 = 0x00192758
	_pop_r1_to_r3_pc = 0x0011BE4D
	# Loads and stores.
	_ldr_r0_r0_pop_r4_pc = 0x00130818
	_str_r1_r0_pop_r4_pc = 0x0010CF5C

class Spider_4x_Gadget:
	# Register loads.
	_pop_pc = 0x0010DB6C
	_pop_r0_pc = 0x002AD574
	_pop_r1_pc = 0x00269758
	_pop_r2_pc = 0x0012F815 # thumb casted
	_pop_r3_pc = 0x0011B064
	_pop_r4_pc = 0x0010DAA8
	_pop_lr_pc = 0x002D6A34 # only for testing
	_pop_r4_to_r12_pc = 0x00103DA8
	_pop_r2_to_r4_pc = 0x00101878 # only for testing
	_pop_r0_to_r4_pc = 0x0022B550 # only for testing
	_pop_r4_lr_bx_r2 = 0x00100C8C
	# Loads and stores.
	_ldr_r0_r0_pop_r4_pc = 0x001CCC64
	_str_r1_r0_pop_r4_pc = 0x0016F3FC

class Spider_5x_Gadget:
	# Register loads.
	_pop_pc = 0x001057E0
	_pop_r0_pc = 0x0010C320
	_pop_r1_pc = 0x00228B10
	_pop_r3_pc = 0x00105100
	_pop_r4_pc = 0x0010510C
	_pop_lr_pc = 0x001303A4
	_pop_r4_to_r12_pc = 0x0010CC4C
	_pop_r2_to_r4_pc = 0x001007B4
	_pop_r0_to_r4_pc = 0x0012A3D4
	# Loads and stores.
	_ldr_r0_r0_pop_r4_pc = 0x0011BB00
	_str_r1_r0_pop_r4_pc = 0x001066B0

class Spider_9x_Gadget:
	# Register loads.
	_pop_pc = 0x001057C4
	_pop_r0_pc = 0x0010C2FC
	_pop_r1_pc = 0x00228AF4
	_pop_r3_pc = 0x001050E8
	_pop_r4_pc = 0x001050F0
	_pop_lr_pc = 0x0013035C
	_pop_r4_to_r12_pc = 0x001065A8
	_pop_r2_to_r4_pc = 0x001007B4
	_pop_r0_to_r4_pc = 0x0010B5B4
	# Loads and stores.
	_ldr_r0_r0_pop_r4_pc = 0x0011BACC
	_str_r1_r0_pop_r4_pc = 0x00106694

class Ref:
	def __init__(self, _name):
		self.name = _name

class Data:
	def __init__(self, _data):
		m = len(_data) % 4
		self.data = (_data + "\x00" * (4 - m) if m else _data)

class ROP:
	def __init__(self, _base, _gadget):
		self.base = _base
		self.addr = _base
		self.stack = []
		self.labels = {}
		self.gadget = _gadget

	def _append(self, v):
		self.stack.append(v)
		self.addr += 4

	def label(self, name):
		self.labels[name] = self.addr

	def ref(self, name):
		self._append(Ref(name))

	def data(self, data):
		d = Data(data)
		self.stack.append(d)
		self.addr += len(d.data)

	def i32(self, v):
		self._append(v)

	def pop_pc(self):
		self._append(self.gadget._pop_pc)

	def pop_r0(self, r0):
		self._append(self.gadget._pop_r0_pc)
		self._append(r0)

	def pop_r1(self, r1):
		self._append(self.gadget._pop_r1_pc)
		self._append(r1)

	def pop_r3(self, r3):
		self._append(self.gadget._pop_r3_pc)
		self._append(r3)

	def pop_r4(self, r4):
		self._append(self.gadget._pop_r4_pc)
		self._append(r4)

	def pop_rX(self, **kwargs):
		regs = ['r4', 'r5', 'r6', 'r7', 'r8', 'r9', 'r10', 'r11', 'r12']
		values = [
			0x44444444, 0x55555555, 0x66666666, 
			0x77777777, 0x88888888, 0x99999999, 
			0xAAAAAAAA, 0xBBBBBBBB, 0xCCCCCCCC
		]
		for k, v in kwargs.items():
			if k not in regs:
				print "Wat? ({0})".format(k)
				return
			else:
				values[int(k[1:]) - 4] = v
		self._append(self.gadget._pop_r4_to_r12_pc)
		for v in values:
			self._append(v)

	def load_r0(self, addy):
		self.pop_r0(addy)
		self._append(self.gadget._ldr_r0_r0_pop_r4_pc)
		self._append(0x44444444)

	def store_r1(self, addy):
		self.pop_r0(addy)
		self._append(self.gadget._str_r1_r0_pop_r4_pc)
		self._append(0x44444444)

	def store_i32(self, value, addy):
		self.pop_r1(value)
		self.store_r1(addy)

	def gen(self):
		res = ""
		for s in self.stack:
			if isinstance(s, Ref):
				res += struct.pack("<I", self.labels[s.name])
			elif isinstance(s, Data):
				res += s.data
			else:
				res += struct.pack("<I", s)
		return res

class ROP_WR2(ROP):
	def pop_r2(self, r2):
		self._append(self.gadget._pop_r2_pc)
		self._append(r2)
	
	def pop_lr(self, lr):
		self.pop_r2(self.gadget._pop_pc)
		self._append(self.gadget._pop_r4_lr_bx_r2)
		self._append(0x44444444)
		self._append(lr)

	def call(self, fun, args, cleancnt):
		pops = [self.gadget._pop_r0_pc, self.gadget._pop_r1_pc, self.gadget._pop_r2_pc, self.gadget._pop_r3_pc]
		if len(args) > 4:
			print "Nahhhh, not now, maybe later ({0})".format(args)
			return
		for i in xrange(len(args)):
			self._append(pops[i])
			self._append(args[i])
		self._append(fun)
		for i in xrange(cleancnt):
			self._append(0xDEADBEEF)

	def call_lr(self, fun, args):
		pops = [self.gadget._pop_r0_pc, self.gadget._pop_r1_pc, self.gadget._pop_r2_pc, self.gadget._pop_r3_pc]
		if len(args) > 4:
			print "Nahhhh, not now, maybe later ({0})".format(args)
			return
		self.pop_lr(self.gadget._pop_pc)
		for i in xrange(len(args)):
			self._append(pops[i])
			self._append(args[i])
		self._append(fun)

class ROP_WOR2(ROP):
	def pop_r2(self, r2):
		self._append(self.gadget._pop_r2_to_r4_pc)
		self._append(r2)
		self._append(0x33333333)
		self._append(0x44444444)

	def pop_lr(self, lr):
		self._append(self.gadget._pop_lr_pc)
		self._append(lr)

	def call(self, fun, args, cleancnt):
		if len(args) > 4:
			print "Nahhhh, not now, maybe later ({0})".format(args)
			return
		self._append(self.gadget._pop_r0_to_r4_pc)
		for i in xrange(len(args)):
			self._append(args[i])
		for i in xrange(5 - len(args)):
			self._append(0xDEADBEEF)
		self._append(fun)
		for i in xrange(cleancnt):
			self._append(0xDEADBEEF)

	def call_lr(self, fun, args):
		if len(args) > 4:
			print "Nahhhh, not now, maybe later ({0})".format(args)
			return
		self.pop_lr(self.gadget._pop_pc)
		self._append(self.gadget._pop_r0_to_r4_pc)
		for i in xrange(len(args)):
			self._append(args[i])
		for i in xrange(5 - len(args)):
			self._append(0xDEADBEEF)
		self._append(fun)

class ROP_WOR2_M6(ROP):
	def pop_r2(self, r2):
		self._append(self.gadget._pop_r1_to_r3_pc)
		self._append(0x11111111)
		self._append(r2)
		self._append(0x33333333)

	def pop_lr(self, lr):
		self.pop_r2(self.gadget._pop_pc)
		self._append(self.gadget._pop_r4_lr_bx_r2)
		self._append(0x44444444)
		self._append(lr)

	def call(self, fun, args, cleancnt):
		if len(args) > 4:
			print "Nahhhh, not now, maybe later ({0})".format(args)
			return
		if len(args) >= 1:
			self._append(self.gadget._pop_r0_pc)
			self._append(args[0])
		if len(args) > 1:
			self._append(self.gadget._pop_r1_to_r3_pc)
			for i in xrange(1, len(args)):
				self._append(args[i])
			for i in xrange(len(args) - 1, 3):
				self._append(0xDEADBEEF)
		self._append(fun)
		for i in xrange(cleancnt):
			self._append(0xDEADBEEF)

	def call_lr(self, fun, args):
		if len(args) > 4:
			print "Nahhhh, not now, maybe later ({0})".format(args)
			return
		self.pop_lr(self.gadget._pop_pc)
		if len(args) >= 1:
			self._append(self.gadget._pop_r0_pc)
			self._append(args[0])
		if len(args) > 1:
			self._append(self.gadget._pop_r1_to_r3_pc)
			for i in xrange(1, len(args)):
				self._append(args[i])
			for i in xrange(len(args) - 1, 3):
				self._append(0xDEADBEEF)
		self._append(fun)

class Mset_4x_ROP(ROP_WR2):
	def __init__(self, _base):
		ROP_WR2.__init__(self, _base, Mset_4x_Gadget());

class Mset_6x_ROP(ROP_WOR2_M6):
	def __init__(self, _base):
		ROP_WOR2_M6.__init__(self, _base, Mset_6x_Gadget());

class Spider_4x_ROP(ROP_WR2):
	def __init__(self, _base):
		ROP_WR2.__init__(self, _base, Spider_4x_Gadget());

class Spider_5x_ROP(ROP_WOR2):
	def __init__(self, _base):
		ROP_WOR2.__init__(self, _base, Spider_5x_Gadget());

class Spider_9x_ROP(ROP_WOR2):
	def __init__(self, _base):
		ROP_WOR2.__init__(self, _base, Spider_9x_Gadget());