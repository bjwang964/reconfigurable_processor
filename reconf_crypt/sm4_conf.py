from pymtl3 import *
from macro import *
from conf import *


sm4_conf = array_conf()
#x3 xor rki
    #PE
sm4_conf.layer_conf[0].pe_conf[0].r0_calc.type = b8(LU_OP)
sm4_conf.layer_conf[0].pe_conf[0].r0_calc.op = b8(NONE)
sm4_conf.layer_conf[0].pe_conf[0].r0_calc.src = b8(1)
sm4_conf.layer_conf[0].pe_conf[1].r0_calc.type = b8(LU_OP)
sm4_conf.layer_conf[0].pe_conf[1].r0_calc.op = b8(NONE)
sm4_conf.layer_conf[0].pe_conf[1].r0_calc.src = b8(1)
sm4_conf.layer_conf[0].pe_conf[2].r0_calc.type = b8(LU_OP) 
sm4_conf.layer_conf[0].pe_conf[2].r0_calc.op = b8(NONE)
sm4_conf.layer_conf[0].pe_conf[2].r0_calc.src = b8(1)
sm4_conf.layer_conf[0].pe_conf[3].r0_calc.type = b8(LU_OP)
sm4_conf.layer_conf[0].pe_conf[3].r0_calc.op = b8(XOR)
sm4_conf.layer_conf[0].pe_conf[3].r0_calc.src = b8(3)
    #connect
sm4_conf.layer_conf[0].conc_conf.conf_io.from_io = 0
sm4_conf.layer_conf[0].conc_conf.conf_io.to_io = 0
sm4_conf.layer_conf[0].conc_conf.conf_out_route[0].a_src = 0
sm4_conf.layer_conf[0].conc_conf.conf_out_route[0].b_src = 0
sm4_conf.layer_conf[0].conc_conf.conf_out_route[0].c_src = 0
sm4_conf.layer_conf[0].conc_conf.conf_out_route[1].a_src = 1#x1
sm4_conf.layer_conf[0].conc_conf.conf_out_route[1].b_src = 2#x2
sm4_conf.layer_conf[0].conc_conf.conf_out_route[1].c_src = 3#x3 xor rki


#x1 xor x2 xor x3 xor rki
    #PE
sm4_conf.layer_conf[1].pe_conf[0].r0_calc.type = b8(LU_OP)
sm4_conf.layer_conf[1].pe_conf[0].r0_calc.op = b8(NONE)
sm4_conf.layer_conf[1].pe_conf[0].r0_calc.src = b8(1)
sm4_conf.layer_conf[1].pe_conf[1].r0_calc.type = b8(LU_OP)
sm4_conf.layer_conf[1].pe_conf[1].r0_calc.op = b8(XX)
sm4_conf.layer_conf[1].pe_conf[1].r0_calc.src = b8(7)
    #connect
sm4_conf.layer_conf[1].conc_conf.conf_io.from_io = 0
sm4_conf.layer_conf[1].conc_conf.conf_io.to_io = 0
sm4_conf.layer_conf[1].conc_conf.conf_out_route[0].a_src = 0
sm4_conf.layer_conf[1].conc_conf.conf_out_route[0].b_src = 0
sm4_conf.layer_conf[1].conc_conf.conf_out_route[0].c_src = 0
sm4_conf.layer_conf[1].conc_conf.conf_out_route[1].a_src = 1
sm4_conf.layer_conf[1].conc_conf.conf_out_route[1].b_src = 1
sm4_conf.layer_conf[1].conc_conf.conf_out_route[1].c_src = 1


#t
    #PE
sm4_conf.layer_conf[2].pe_conf[0].r0_calc.type = b8(LU_OP)
sm4_conf.layer_conf[2].pe_conf[0].r0_calc.op = b8(NONE)
sm4_conf.layer_conf[2].pe_conf[0].r0_calc.src = b8(1)
sm4_conf.layer_conf[2].pe_conf[1].r0_calc.type = b8(LUT_OP)
sm4_conf.layer_conf[2].pe_conf[1].r0_calc.op = b8(0)
sm4_conf.layer_conf[2].pe_conf[1].r0_calc.src = b8(1)
    #connect
sm4_conf.layer_conf[2].conc_conf.conf_io.from_io = 0
sm4_conf.layer_conf[2].conc_conf.conf_io.to_io = 0
sm4_conf.layer_conf[2].conc_conf.conf_out_route[0].a_src = 0 #x0
sm4_conf.layer_conf[2].conc_conf.conf_out_route[0].b_src = 1 #B
sm4_conf.layer_conf[2].conc_conf.conf_out_route[0].c_src = 0
sm4_conf.layer_conf[2].conc_conf.conf_out_route[1].a_src = 1 #B
sm4_conf.layer_conf[2].conc_conf.conf_out_route[1].b_src = 1
sm4_conf.layer_conf[2].conc_conf.conf_out_route[1].c_src = 1
sm4_conf.layer_conf[2].conc_conf.conf_out_route[2].a_src = 1 #B
sm4_conf.layer_conf[2].conc_conf.conf_out_route[2].b_src = 1
sm4_conf.layer_conf[2].conc_conf.conf_out_route[2].c_src = 1
sm4_conf.layer_conf[2].conc_conf.conf_out_route[3].a_src = 1 #B
sm4_conf.layer_conf[2].conc_conf.conf_out_route[3].b_src = 1
sm4_conf.layer_conf[2].conc_conf.conf_out_route[3].c_src = 1


#L
    #PE
sm4_conf.layer_conf[3].pe_conf[0].r0_calc.type = b8(LU_OP)
sm4_conf.layer_conf[3].pe_conf[0].r0_calc.op = b8(XOR)
sm4_conf.layer_conf[3].pe_conf[0].r0_calc.src = b8(3)
sm4_conf.layer_conf[3].pe_conf[1].r0_calc.type = b8(LU_OP)
sm4_conf.layer_conf[3].pe_conf[1].r0_calc.op = b8(SLA)
sm4_conf.layer_conf[3].pe_conf[1].r0_calc.src = b8(9)
sm4_conf.layer_conf[3].pe_conf[1].imm = b32(2)
sm4_conf.layer_conf[3].pe_conf[2].r0_calc.type = b8(LU_OP)
sm4_conf.layer_conf[3].pe_conf[2].r0_calc.op = b8(SLA)
sm4_conf.layer_conf[3].pe_conf[2].r0_calc.src = b8(9)
sm4_conf.layer_conf[3].pe_conf[2].imm = b32(0xa)
sm4_conf.layer_conf[3].pe_conf[3].r0_calc.type = b8(LU_OP)
sm4_conf.layer_conf[3].pe_conf[3].r0_calc.op = b8(SLA)
sm4_conf.layer_conf[3].pe_conf[3].r0_calc.src = b8(9)
sm4_conf.layer_conf[3].pe_conf[3].imm = b32(0x12)
    #connect
sm4_conf.layer_conf[3].conc_conf.conf_io.from_io = 0
sm4_conf.layer_conf[3].conc_conf.conf_io.to_io = 0
sm4_conf.layer_conf[3].conc_conf.conf_out_route[0].a_src = 0 #x0
sm4_conf.layer_conf[3].conc_conf.conf_out_route[0].b_src = 1 #B<<<2
sm4_conf.layer_conf[3].conc_conf.conf_out_route[0].c_src = 2 #B<<<10
sm4_conf.layer_conf[3].conc_conf.conf_out_route[1].a_src = 3 #B<<<18
sm4_conf.layer_conf[3].conc_conf.conf_out_route[1].b_src = 1
sm4_conf.layer_conf[3].conc_conf.conf_out_route[1].c_src = 1


#F
    #PE
sm4_conf.layer_conf[4].pe_conf[0].r0_calc.type = b8(LU_OP)
sm4_conf.layer_conf[4].pe_conf[0].r0_calc.op = b8(XX)
sm4_conf.layer_conf[4].pe_conf[0].r0_calc.src = b8(7)
sm4_conf.layer_conf[4].pe_conf[1].r0_calc.type = b8(LU_OP)
sm4_conf.layer_conf[4].pe_conf[1].r0_calc.op = b8(NONE)
sm4_conf.layer_conf[4].pe_conf[1].r0_calc.src = b8(1)
    #connect
sm4_conf.layer_conf[4].conc_conf.conf_out_route[0].a_src = 0 
sm4_conf.layer_conf[4].conc_conf.conf_out_route[0].b_src = 1 
sm4_conf.layer_conf[4].conc_conf.conf_out_route[0].c_src = 1 
#FF
    #PE
sm4_conf.layer_conf[5].pe_conf[0].r0_calc.type = b8(LU_OP)
sm4_conf.layer_conf[5].pe_conf[0].r0_calc.op = b8(XOR)
sm4_conf.layer_conf[5].pe_conf[0].r0_calc.src = b8(3)
