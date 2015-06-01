import struct

class Mset_4x:
	memcpy = 0x001BFA60											# bx lr
	GSPGPU_FlushDataCache = 0x0013C5D4							# ldmfd sp!, {r4-r6, pc}
	nn__gxlow__CTR__CmdReqQueueTx__TryEnqueue = 0x001AC924		# ldmfd sp!, {r4-r10,pc}
	nn__gxlow__CTR__detail__GetInterruptReceiver = 0x0027C580
	svcSleepThread = 0x001AEA50									# bx lr
	fopen = 0x001B82A8											# ldmfd sp!, {r4-r8,pc}
	fread = 0x001B3954											# ldmfd sp!, {r4-r9,pc}
	fwrite = 0x001B3B50											# ldmfd sp!, {r4-r11,pc}
	
	# Pop counts
	GSPGPU_FlushDataCache_pops = 3
	nn__gxlow__CTR__CmdReqQueueTx__TryEnqueue_pops = 7
	fopen_pops = 5
	fread_pops = 6
	fwrite_pops = 8

	rop_loc = 0x002B0000
	gsp_handle = 0x0027FAC4
	gsp_addr = 0x14000000
	gsp_code_addr = 0x00700000
	fcram_code_addr = 0x03E6D000
	payload_addr = 0x00140000
	file_handle = 0x279000
	buffer = gsp_addr + gsp_code_addr
	code_target = gsp_addr + fcram_code_addr + payload_addr
	code_entry = 0x100000 + payload_addr

class Spider_4x:
	memcpy = 0x0029BF60											# bx lr
	GSPGPU_FlushDataCache = 0x00344C2C							# ldmfd sp!, {r4-r6, pc}
	nn__gxlow__CTR__CmdReqQueueTx__TryEnqueue = 0x002CF3EC		# ldmfd sp!, {r4-r8, pc}
	nn__gxlow__CTR__detail__GetInterruptReceiver = 0x003F54E8
	svcSleepThread = 0x002A513C									# bx lr
	fopen = 0x0025B0A4											# ldmfd sp!, {r4-r7,pc}
	fread = 0x002FC8E4											# ldmfd sp!, {r4-r9,pc}
	fwrite = 0x00311D90											# ldmfd sp!, {r4-r11,pc}

	# Pop counts
	GSPGPU_FlushDataCache_pops = 3
	nn__gxlow__CTR__CmdReqQueueTx__TryEnqueue_pops = 5
	fopen_pops = 4
	fread_pops = 6
	fwrite_pops = 8

	rop_loc = 0x08F01000
	gsp_handle = 0x003B643C
	fcram_code_addr = 0x067DE000
	file_handle = 0x08F00400
	buffer = 0x18410000
	code_target = 0x192D3000
	code_entry = 0x009D2000

# Spider 5.x ~ 6.x
class Spider_5x:
	memcpy = 0x00240B58											# bx lr
	GSPGPU_FlushDataCache = 0x0012C228							# ldmfd sp!, {r4-r6, pc}
	nn__gxlow__CTR__CmdReqQueueTx__TryEnqueue = 0x0012BF4C		# ldmfd sp!, {r4-r10, pc}
	nn__gxlow__CTR__detail__GetInterruptReceiver = 0x003D7C40
	svcSleepThread = 0x0010420C									# bx lr
	fopen = 0x0022FE44											# ldmfd sp!, {r4-r8,pc}
	fread = 0x001686C0											# ldmfd sp!, {r4-r9,pc}
	fwrite = 0x00168748											# ldmfd sp!, {r4-r11,pc}

	# Pop counts
	GSPGPU_FlushDataCache_pops = 3
	nn__gxlow__CTR__CmdReqQueueTx__TryEnqueue_pops = 7
	fopen_pops = 5
	fread_pops = 6
	fwrite_pops = 8

	rop_loc = 0x08F01000
	gsp_handle = 0x003DA72C
	#fcram_code_addr = 0x067DE000
	file_handle = 0x08F00400 
	buffer = 0x18410000
	code_target = 0x19592000
	code_entry = 0x009D2000

# Spider 7.x ~ 9.2
class Spider_9x:
	memcpy = 0x00240B50											# bx lr
	GSPGPU_FlushDataCache = 0x0012C1E0							# ldmfd sp!, {r4-r6, pc}
	nn__gxlow__CTR__CmdReqQueueTx__TryEnqueue = 0x0012BF04		# ldmfd sp!, {r4-r10, pc}
	nn__gxlow__CTR__detail__GetInterruptReceiver = 0x003D7C40
	svcSleepThread = 0x001041F8									# bx lr
	fopen = 0x0022FE08											# ldmfd sp!, {r4-r8,pc}
	fread = 0x001686DC											# ldmfd sp!, {r4-r9,pc}
	fwrite = 0x00168764											# ldmfd sp!, {r4-r11,pc}

	# Pop counts
	GSPGPU_FlushDataCache_pops = 3
	nn__gxlow__CTR__CmdReqQueueTx__TryEnqueue_pops = 7
	fopen_pops = 5
	fread_pops = 6
	fwrite_pops = 8

	rop_loc = 0x08F01000
	gsp_handle = 0x003DA72C
	#fcram_code_addr = 0x067DE000
	file_handle = 0x08F00400
	buffer = 0x18370000
	code_target = 0x19592000
	code_entry = 0x009D2000