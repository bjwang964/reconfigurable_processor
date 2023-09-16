from pymtl3 import *
from PE import *
from PE_row import *
from connect import *
from array_layer import *


class AES_round_conf(object):
    def __init__(s):
        s.step_num = 4
        s.conf_entry = [layer_conf() for i in range(s.step_num)]
        #Byte sub
            #PE
        s.conf_entry[0].pe_conf[0].r0_calc.type = LUT_OP
        s.conf_entry[0].pe_conf[0].r0_calc.op = b8(0)
        s.conf_entry[0].pe_conf[0].r0_calc.src = b8(1)

        s.conf_entry[0].pe_conf[1].r0_calc.type = LUT_OP
        s.conf_entry[0].pe_conf[1].r0_calc.op = b8(0)
        s.conf_entry[0].pe_conf[1].r0_calc.src = b8(1)

        s.conf_entry[0].pe_conf[2].r0_calc.type = LUT_OP
        s.conf_entry[0].pe_conf[2].r0_calc.op = b8(0)
        s.conf_entry[0].pe_conf[2].r0_calc.src = b8(1)

        s.conf_entry[0].pe_conf[3].r0_calc.type = LUT_OP
        s.conf_entry[0].pe_conf[3].r0_calc.op = b8(0)
        s.conf_entry[0].pe_conf[3].r0_calc.src = b8(1)
            #connect
        s.conf_entry[0].conc_conf.conf_io.from_io = 0
        s.conf_entry[0].conc_conf.conf_io.to_io = 0
        for i in range(ROW_LEN):
            s.conf_entry[0].conc_conf.conf_out_route[i].src_a = i
            s.conf_entry[0].conc_conf.conf_out_route[i].src_b = i
            s.conf_entry[0].conc_conf.conf_out_route[i].src_c = i
        
        #row shif
            #PE
        s.conf_entry[1].pe_conf[0].r0_calc.type = LU_OP
        s.conf_entry[1].pe_conf[0].r0_calc.op = b8(NONE)
        s.conf_entry[1].pe_conf[0].r0_calc.src = b8(9)
        s.conf_entry[1].pe_conf[0].imm = b32(0)

        s.conf_entry[1].pe_conf[1].r0_calc.type = LU_OP
        s.conf_entry[1].pe_conf[1].r0_calc.op = b8(SLA)
        s.conf_entry[1].pe_conf[1].r0_calc.src = b8(9)
        s.conf_entry[1].pe_conf[0].imm = b32(8)

        s.conf_entry[1].pe_conf[2].r0_calc.type = LU_OP
        s.conf_entry[1].pe_conf[2].r0_calc.op = b8(SLA)
        s.conf_entry[1].pe_conf[2].r0_calc.op = b8(9)
        s.conf_entry[1].pe_conf[0].imm = b32(8)

        s.conf_entry[1].pe_conf[3].r0_calc.type = LU_OP
        s.conf_entry[1].pe_conf[3].r0_calc.op = b8(SLATB)
        s.conf_entry[1].pe_conf[3].r0_calc.op = b8(0)
            #connect
        s.conf_entry[1].conc_conf.conf_io.from_io = 0
        s.conf_entry[1].conc_conf.conf_io.to_io = 0
        for i in range(ROW_LEN):
            s.conf_entry[1].conc_conf.conf_out_route[i].src_a = 0
            s.conf_entry[1].conc_conf.conf_out_route[i].src_b = 0
            s.conf_entry[1].conc_conf.conf_out_route[i].src_c = 0

        #




