from pymtl3 import *
from macro import *
from conf import *


sm4_conf = array_conf()
#layer  0
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
sm4_conf.layer_conf[0].pe_conf[3].r0_calc.op = b8(NONE)
sm4_conf.layer_conf[0].pe_conf[3].r0_calc.src = b8(1)

sm4_conf.layer_conf[0].pe_conf[3].r1_calc.type = b8(LU_OP)
sm4_conf.layer_conf[0].pe_conf[3].r1_calc.op = b8(NONE)
sm4_conf.layer_conf[0].pe_conf[3].r1_calc.src = b8(4)
    #connect
sm4_conf.layer_conf[0].conc_conf.conf_out_route[0].a_src = 0 #x0
sm4_conf.layer_conf[0].conc_conf.conf_out_route[0].c_src = 1 #x1

sm4_conf.layer_conf[0].conc_conf.conf_out_route[1].a_src = 1 #x1
sm4_conf.layer_conf[0].conc_conf.conf_out_route[1].b_src = 2 #x2
sm4_conf.layer_conf[0].conc_conf.conf_out_route[1].c_src = 2 #x2

sm4_conf.layer_conf[0].conc_conf.conf_out_route[2].a_src = 3 #x3
sm4_conf.layer_conf[0].conc_conf.conf_out_route[2].b_src = 8+0 #rk0
sm4_conf.layer_conf[0].conc_conf.conf_out_route[2].c_src = 3 #x3

sm4_conf.layer_conf[0].conc_conf.conf_out_route[3].c_src = 4+3 #rki_addr
    #IO
sm4_conf.layer_conf[0].io_conf.addr_r0 = 3#rki_addr
sm4_conf.layer_conf[0].io_conf.out_forward = 0#from rf

sm4_conf.layer_conf[0].cnt = 8
sm4_conf.layer_conf[0].next_cc = 8







#layer  1
    #PE
sm4_conf.layer_conf[1].pe_conf[0].r0_calc.type = b8(LU_OP)
sm4_conf.layer_conf[1].pe_conf[0].r0_calc.op = b8(NONE)
sm4_conf.layer_conf[1].pe_conf[0].r0_calc.src = b8(1)

sm4_conf.layer_conf[1].pe_conf[0].r1_calc.type = b8(LU_OP)
sm4_conf.layer_conf[1].pe_conf[0].r1_calc.op = b8(NONE)
sm4_conf.layer_conf[1].pe_conf[0].r1_calc.src = b8(4)

sm4_conf.layer_conf[1].pe_conf[1].r0_calc.type = b8(LU_OP)
sm4_conf.layer_conf[1].pe_conf[1].r0_calc.op = b8(XOR)
sm4_conf.layer_conf[1].pe_conf[1].r0_calc.src = b8(3)

sm4_conf.layer_conf[1].pe_conf[1].r1_calc.type = b8(LU_OP)
sm4_conf.layer_conf[1].pe_conf[1].r1_calc.op = b8(NONE)
sm4_conf.layer_conf[1].pe_conf[1].r1_calc.src = b8(4)

sm4_conf.layer_conf[1].pe_conf[2].r0_calc.type = b8(LU_OP) 
sm4_conf.layer_conf[1].pe_conf[2].r0_calc.op = b8(XOR)
sm4_conf.layer_conf[1].pe_conf[2].r0_calc.src = b8(3)

sm4_conf.layer_conf[1].pe_conf[2].r1_calc.type = b8(LU_OP) 
sm4_conf.layer_conf[1].pe_conf[2].r1_calc.op = b8(NONE)
sm4_conf.layer_conf[1].pe_conf[2].r1_calc.src = b8(4)

sm4_conf.layer_conf[1].pe_conf[3].r0_calc.type = b8(LU_OP)
sm4_conf.layer_conf[1].pe_conf[3].r0_calc.op = b8(NONE)
sm4_conf.layer_conf[1].pe_conf[3].r0_calc.src = b8(1)

sm4_conf.layer_conf[1].pe_conf[3].r1_calc.type = b8(AU_OP)
sm4_conf.layer_conf[1].pe_conf[3].r1_calc.op = b8(ADD_ONE)
sm4_conf.layer_conf[1].pe_conf[3].r1_calc.src = b8(4)

    #connect
sm4_conf.layer_conf[1].conc_conf.conf_out_route[0].a_src = 0 #x0
sm4_conf.layer_conf[1].conc_conf.conf_out_route[0].c_src = 0+4 #x1

sm4_conf.layer_conf[1].conc_conf.conf_out_route[1].a_src = 1 #x1^x2
sm4_conf.layer_conf[1].conc_conf.conf_out_route[1].b_src = 2 #x3^rk0
sm4_conf.layer_conf[1].conc_conf.conf_out_route[1].c_src = 1+4 #x2

sm4_conf.layer_conf[1].conc_conf.conf_out_route[2].a_src = 8+0 #2
sm4_conf.layer_conf[1].conc_conf.conf_out_route[2].c_src = 2+4 #x3

sm4_conf.layer_conf[1].conc_conf.conf_out_route[3].c_src = 3+4 #rki_addr
    #IO
sm4_conf.layer_conf[1].io_conf.fix_acc = 1
sm4_conf.layer_conf[1].io_conf.fix_addr = 40
sm4_conf.layer_conf[1].io_conf.out_forward = 0#from rf
sm4_conf.layer_conf[1].io_conf.src_a = 0


sm4_conf.layer_conf[1].cnt = 1000




#layer  2
    #PE
sm4_conf.layer_conf[2].pe_conf[0].r0_calc.type = b8(LU_OP)
sm4_conf.layer_conf[2].pe_conf[0].r0_calc.op = b8(NONE)
sm4_conf.layer_conf[2].pe_conf[0].r0_calc.src = b8(1)

sm4_conf.layer_conf[2].pe_conf[0].r1_calc.type = b8(LU_OP)
sm4_conf.layer_conf[2].pe_conf[0].r1_calc.op = b8(NONE)
sm4_conf.layer_conf[2].pe_conf[0].r1_calc.src = b8(4)

sm4_conf.layer_conf[2].pe_conf[1].r0_calc.type = b8(LU_OP)
sm4_conf.layer_conf[2].pe_conf[1].r0_calc.op = b8(XOR)
sm4_conf.layer_conf[2].pe_conf[1].r0_calc.src = b8(3)

sm4_conf.layer_conf[2].pe_conf[1].r1_calc.type = b8(LU_OP)
sm4_conf.layer_conf[2].pe_conf[1].r1_calc.op = b8(NONE)
sm4_conf.layer_conf[2].pe_conf[1].r1_calc.src = b8(4)

sm4_conf.layer_conf[2].pe_conf[2].r0_calc.type = b8(LU_OP) 
sm4_conf.layer_conf[2].pe_conf[2].r0_calc.op = b8(NONE)
sm4_conf.layer_conf[2].pe_conf[2].r0_calc.src = b8(1)

sm4_conf.layer_conf[2].pe_conf[2].r1_calc.type = b8(LU_OP) 
sm4_conf.layer_conf[2].pe_conf[2].r1_calc.op = b8(NONE)
sm4_conf.layer_conf[2].pe_conf[2].r1_calc.src = b8(4)

sm4_conf.layer_conf[2].pe_conf[3].r0_calc.type = b8(LU_OP)
sm4_conf.layer_conf[2].pe_conf[3].r0_calc.op = b8(NONE)
sm4_conf.layer_conf[2].pe_conf[3].r0_calc.src = b8(1)

sm4_conf.layer_conf[2].pe_conf[3].r1_calc.type = b8(LU_OP)
sm4_conf.layer_conf[2].pe_conf[3].r1_calc.op = b8(NONE)
sm4_conf.layer_conf[2].pe_conf[3].r1_calc.src = b8(4)

    #connect
sm4_conf.layer_conf[2].conc_conf.conf_out_route[0].a_src = 0 #x0
sm4_conf.layer_conf[2].conc_conf.conf_out_route[0].c_src = 0+4 #x1

sm4_conf.layer_conf[2].conc_conf.conf_out_route[1].a_src = 1 #x1^x2^x3
sm4_conf.layer_conf[2].conc_conf.conf_out_route[1].c_src = 1+4 #x2

sm4_conf.layer_conf[2].conc_conf.conf_out_route[2].a_src = 2 #2
sm4_conf.layer_conf[2].conc_conf.conf_out_route[2].c_src = 2+4 #x3

sm4_conf.layer_conf[2].conc_conf.conf_out_route[3].a_src = 8+0 #10
sm4_conf.layer_conf[2].conc_conf.conf_out_route[3].c_src = 3+4 #rki_addr
    #IO
sm4_conf.layer_conf[2].io_conf.fix_acc = 1
sm4_conf.layer_conf[2].io_conf.fix_addr = 44
sm4_conf.layer_conf[2].io_conf.out_forward = 0#from rf
sm4_conf.layer_conf[2].io_conf.src_a = 0


sm4_conf.layer_conf[2].cnt = 1000

#layer  3
    #PE
sm4_conf.layer_conf[3].pe_conf[0].r0_calc.type = b8(LU_OP)
sm4_conf.layer_conf[3].pe_conf[0].r0_calc.op = b8(NONE)
sm4_conf.layer_conf[3].pe_conf[0].r0_calc.src = b8(1)

sm4_conf.layer_conf[3].pe_conf[0].r1_calc.type = b8(LU_OP)
sm4_conf.layer_conf[3].pe_conf[0].r1_calc.op = b8(NONE)
sm4_conf.layer_conf[3].pe_conf[0].r1_calc.src = b8(4)

sm4_conf.layer_conf[3].pe_conf[1].r0_calc.type = b8(LUT_OP)
sm4_conf.layer_conf[3].pe_conf[1].r0_calc.op = b8(NONE)
sm4_conf.layer_conf[3].pe_conf[1].r0_calc.src = b8(1)

sm4_conf.layer_conf[3].pe_conf[1].r1_calc.type = b8(LU_OP)
sm4_conf.layer_conf[3].pe_conf[1].r1_calc.op = b8(NONE)
sm4_conf.layer_conf[3].pe_conf[1].r1_calc.src = b8(4)

sm4_conf.layer_conf[3].pe_conf[2].r0_calc.type = b8(LU_OP) 
sm4_conf.layer_conf[3].pe_conf[2].r0_calc.op = b8(NONE)
sm4_conf.layer_conf[3].pe_conf[2].r0_calc.src = b8(1)

sm4_conf.layer_conf[3].pe_conf[2].r1_calc.type = b8(LU_OP) 
sm4_conf.layer_conf[3].pe_conf[2].r1_calc.op = b8(NONE)
sm4_conf.layer_conf[3].pe_conf[2].r1_calc.src = b8(4)

sm4_conf.layer_conf[3].pe_conf[3].r0_calc.type = b8(LU_OP)
sm4_conf.layer_conf[3].pe_conf[3].r0_calc.op = b8(NONE)
sm4_conf.layer_conf[3].pe_conf[3].r0_calc.src = b8(1)

sm4_conf.layer_conf[3].pe_conf[3].r1_calc.type = b8(LU_OP)
sm4_conf.layer_conf[3].pe_conf[3].r1_calc.op = b8(NONE)
sm4_conf.layer_conf[3].pe_conf[3].r1_calc.src = b8(4)

    #connect
sm4_conf.layer_conf[3].conc_conf.conf_out_route[0].a_src = 0 #x0
sm4_conf.layer_conf[3].conc_conf.conf_out_route[0].b_src = 1 #B
sm4_conf.layer_conf[3].conc_conf.conf_out_route[0].c_src = 0+4 #x1

sm4_conf.layer_conf[3].conc_conf.conf_out_route[1].a_src = 1 #B
sm4_conf.layer_conf[3].conc_conf.conf_out_route[1].b_src = 2 #2
sm4_conf.layer_conf[3].conc_conf.conf_out_route[1].c_src = 1+4 #x2

sm4_conf.layer_conf[3].conc_conf.conf_out_route[2].a_src = 1 #B
sm4_conf.layer_conf[3].conc_conf.conf_out_route[2].b_src = 3 #10
sm4_conf.layer_conf[3].conc_conf.conf_out_route[2].c_src = 2+4 #x3

sm4_conf.layer_conf[3].conc_conf.conf_out_route[3].a_src = 8+0 #8
sm4_conf.layer_conf[3].conc_conf.conf_out_route[3].c_src = 3+4 #rki_addr
    #IO
sm4_conf.layer_conf[3].io_conf.fix_acc = 1
sm4_conf.layer_conf[3].io_conf.fix_addr = 48
sm4_conf.layer_conf[3].io_conf.out_forward = 0#from rf
sm4_conf.layer_conf[3].io_conf.src_a = 0

sm4_conf.layer_conf[3].cnt = 1000



#layer  4
    #PE
sm4_conf.layer_conf[4].pe_conf[0].r0_calc.type = b8(LU_OP)
sm4_conf.layer_conf[4].pe_conf[0].r0_calc.op = b8(XOR)
sm4_conf.layer_conf[4].pe_conf[0].r0_calc.src = b8(3)

sm4_conf.layer_conf[4].pe_conf[0].r1_calc.type = b8(LU_OP)
sm4_conf.layer_conf[4].pe_conf[0].r1_calc.op = b8(NONE)
sm4_conf.layer_conf[4].pe_conf[0].r1_calc.src = b8(4)

sm4_conf.layer_conf[4].pe_conf[1].r0_calc.type = b8(LU_OP)
sm4_conf.layer_conf[4].pe_conf[1].r0_calc.op = b8(SLA)
sm4_conf.layer_conf[4].pe_conf[1].r0_calc.src = b8(3)

sm4_conf.layer_conf[4].pe_conf[1].r1_calc.type = b8(LU_OP)
sm4_conf.layer_conf[4].pe_conf[1].r1_calc.op = b8(NONE)
sm4_conf.layer_conf[4].pe_conf[1].r1_calc.src = b8(4)

sm4_conf.layer_conf[4].pe_conf[2].r0_calc.type = b8(LU_OP) 
sm4_conf.layer_conf[4].pe_conf[2].r0_calc.op = b8(SLA)
sm4_conf.layer_conf[4].pe_conf[2].r0_calc.src = b8(3)

sm4_conf.layer_conf[4].pe_conf[2].r1_calc.type = b8(LU_OP) 
sm4_conf.layer_conf[4].pe_conf[2].r1_calc.op = b8(NONE)
sm4_conf.layer_conf[4].pe_conf[2].r1_calc.src = b8(4)

sm4_conf.layer_conf[4].pe_conf[3].r0_calc.type = b8(LU_OP)
sm4_conf.layer_conf[4].pe_conf[3].r0_calc.op = b8(NONE)
sm4_conf.layer_conf[4].pe_conf[3].r0_calc.src = b8(1)

sm4_conf.layer_conf[4].pe_conf[3].r1_calc.type = b8(LU_OP)
sm4_conf.layer_conf[4].pe_conf[3].r1_calc.op = b8(NONE)
sm4_conf.layer_conf[4].pe_conf[3].r1_calc.src = b8(4)

    #connect
sm4_conf.layer_conf[4].conc_conf.conf_out_route[0].a_src = 0 #x0^B
sm4_conf.layer_conf[4].conc_conf.conf_out_route[0].b_src = 1 #B2
sm4_conf.layer_conf[4].conc_conf.conf_out_route[0].c_src = 0+4 #x1

sm4_conf.layer_conf[4].conc_conf.conf_out_route[1].a_src = 2 #B10
sm4_conf.layer_conf[4].conc_conf.conf_out_route[1].c_src = 1+4 #x2

sm4_conf.layer_conf[4].conc_conf.conf_out_route[2].a_src = 2 #B10
sm4_conf.layer_conf[4].conc_conf.conf_out_route[2].b_src = 3 #8
sm4_conf.layer_conf[4].conc_conf.conf_out_route[2].c_src = 2+4 #x3

sm4_conf.layer_conf[4].conc_conf.conf_out_route[3].a_src = 2 #B10
sm4_conf.layer_conf[4].conc_conf.conf_out_route[3].b_src = 0+8 #14
sm4_conf.layer_conf[4].conc_conf.conf_out_route[3].c_src = 3+4 #rki_addr
    #IO
sm4_conf.layer_conf[4].io_conf.fix_acc = 1
sm4_conf.layer_conf[4].io_conf.fix_addr = 52
sm4_conf.layer_conf[4].io_conf.out_forward = 0#from rf
sm4_conf.layer_conf[4].io_conf.src_a = 0

sm4_conf.layer_conf[4].cnt = 1000


#layer  5
    #PE
sm4_conf.layer_conf[5].pe_conf[0].r0_calc.type = b8(LU_OP)
sm4_conf.layer_conf[5].pe_conf[0].r0_calc.op = b8(XOR)
sm4_conf.layer_conf[5].pe_conf[0].r0_calc.src = b8(3)

sm4_conf.layer_conf[5].pe_conf[0].r1_calc.type = b8(LU_OP)
sm4_conf.layer_conf[5].pe_conf[0].r1_calc.op = b8(NONE)
sm4_conf.layer_conf[5].pe_conf[0].r1_calc.src = b8(4)

sm4_conf.layer_conf[5].pe_conf[1].r0_calc.type = b8(LU_OP)
sm4_conf.layer_conf[5].pe_conf[1].r0_calc.op = b8(NONE)
sm4_conf.layer_conf[5].pe_conf[1].r0_calc.src = b8(1)

sm4_conf.layer_conf[5].pe_conf[1].r1_calc.type = b8(LU_OP)
sm4_conf.layer_conf[5].pe_conf[1].r1_calc.op = b8(NONE)
sm4_conf.layer_conf[5].pe_conf[1].r1_calc.src = b8(4)

sm4_conf.layer_conf[5].pe_conf[2].r0_calc.type = b8(LU_OP) 
sm4_conf.layer_conf[5].pe_conf[2].r0_calc.op = b8(SLA)
sm4_conf.layer_conf[5].pe_conf[2].r0_calc.src = b8(3)

sm4_conf.layer_conf[5].pe_conf[2].r1_calc.type = b8(LU_OP) 
sm4_conf.layer_conf[5].pe_conf[2].r1_calc.op = b8(NONE)
sm4_conf.layer_conf[5].pe_conf[2].r1_calc.src = b8(4)

sm4_conf.layer_conf[5].pe_conf[3].r0_calc.type = b8(LU_OP)
sm4_conf.layer_conf[5].pe_conf[3].r0_calc.op = b8(SLA)
sm4_conf.layer_conf[5].pe_conf[3].r0_calc.src = b8(3)

sm4_conf.layer_conf[5].pe_conf[3].r1_calc.type = b8(LU_OP)
sm4_conf.layer_conf[5].pe_conf[3].r1_calc.op = b8(NONE)
sm4_conf.layer_conf[5].pe_conf[3].r1_calc.src = b8(4)

    #connect
sm4_conf.layer_conf[5].conc_conf.conf_out_route[0].a_src = 0 #x0^B^B2
sm4_conf.layer_conf[5].conc_conf.conf_out_route[0].b_src = 1 #B10
sm4_conf.layer_conf[5].conc_conf.conf_out_route[0].c_src = 0+4 #x1

sm4_conf.layer_conf[5].conc_conf.conf_out_route[1].c_src = 1+4 #x2

sm4_conf.layer_conf[5].conc_conf.conf_out_route[2].a_src = 2 #B18
sm4_conf.layer_conf[5].conc_conf.conf_out_route[2].b_src = 3 #B24
sm4_conf.layer_conf[5].conc_conf.conf_out_route[2].c_src = 2+4 #x3

sm4_conf.layer_conf[5].conc_conf.conf_out_route[3].c_src = 3+4 #rki_addr
    #IO

sm4_conf.layer_conf[5].cnt = 1000


#layer  6
    #PE
sm4_conf.layer_conf[6].pe_conf[0].r0_calc.type = b8(LU_OP)
sm4_conf.layer_conf[6].pe_conf[0].r0_calc.op = b8(XOR)
sm4_conf.layer_conf[6].pe_conf[0].r0_calc.src = b8(3)

sm4_conf.layer_conf[6].pe_conf[0].r1_calc.type = b8(LU_OP)
sm4_conf.layer_conf[6].pe_conf[0].r1_calc.op = b8(NONE)
sm4_conf.layer_conf[6].pe_conf[0].r1_calc.src = b8(4)

sm4_conf.layer_conf[6].pe_conf[1].r0_calc.type = b8(LU_OP)
sm4_conf.layer_conf[6].pe_conf[1].r0_calc.op = b8(NONE)
sm4_conf.layer_conf[6].pe_conf[1].r0_calc.src = b8(1)

sm4_conf.layer_conf[6].pe_conf[1].r1_calc.type = b8(LU_OP)
sm4_conf.layer_conf[6].pe_conf[1].r1_calc.op = b8(NONE)
sm4_conf.layer_conf[6].pe_conf[1].r1_calc.src = b8(4)

sm4_conf.layer_conf[6].pe_conf[2].r0_calc.type = b8(LU_OP) 
sm4_conf.layer_conf[6].pe_conf[2].r0_calc.op = b8(XOR)
sm4_conf.layer_conf[6].pe_conf[2].r0_calc.src = b8(3)

sm4_conf.layer_conf[6].pe_conf[2].r1_calc.type = b8(LU_OP) 
sm4_conf.layer_conf[6].pe_conf[2].r1_calc.op = b8(NONE)
sm4_conf.layer_conf[6].pe_conf[2].r1_calc.src = b8(4)

sm4_conf.layer_conf[6].pe_conf[3].r0_calc.type = b8(LU_OP)
sm4_conf.layer_conf[6].pe_conf[3].r0_calc.op = b8(NONE)
sm4_conf.layer_conf[6].pe_conf[3].r0_calc.src = b8(1)

sm4_conf.layer_conf[6].pe_conf[3].r1_calc.type = b8(LU_OP)
sm4_conf.layer_conf[6].pe_conf[3].r1_calc.op = b8(NONE)
sm4_conf.layer_conf[6].pe_conf[3].r1_calc.src = b8(4)

    #connect
sm4_conf.layer_conf[6].conc_conf.conf_out_route[0].a_src = 0 #x0^B^B2^B10
sm4_conf.layer_conf[6].conc_conf.conf_out_route[0].b_src = 2 #B8^B24

sm4_conf.layer_conf[6].conc_conf.conf_out_route[1].a_src = 0+4 #x1

sm4_conf.layer_conf[6].conc_conf.conf_out_route[2].a_src = 1+4 #x2

sm4_conf.layer_conf[6].conc_conf.conf_out_route[3].a_src = 2+4 #x3
sm4_conf.layer_conf[6].conc_conf.conf_out_route[3].c_src = 3+4 #rki_addr
    #IO

sm4_conf.layer_conf[6].cnt = 1000


#layer  7
    #PE
sm4_conf.layer_conf[7].pe_conf[0].r0_calc.type = b8(LU_OP)
sm4_conf.layer_conf[7].pe_conf[0].r0_calc.op = b8(XOR)
sm4_conf.layer_conf[7].pe_conf[0].r0_calc.src = b8(3)

sm4_conf.layer_conf[7].pe_conf[0].r1_calc.type = b8(LU_OP)
sm4_conf.layer_conf[7].pe_conf[0].r1_calc.op = b8(NONE)
sm4_conf.layer_conf[7].pe_conf[0].r1_calc.src = b8(4)

sm4_conf.layer_conf[7].pe_conf[1].r0_calc.type = b8(LU_OP)
sm4_conf.layer_conf[7].pe_conf[1].r0_calc.op = b8(NONE)
sm4_conf.layer_conf[7].pe_conf[1].r0_calc.src = b8(1)

sm4_conf.layer_conf[7].pe_conf[1].r1_calc.type = b8(LU_OP)
sm4_conf.layer_conf[7].pe_conf[1].r1_calc.op = b8(NONE)
sm4_conf.layer_conf[7].pe_conf[1].r1_calc.src = b8(4)

sm4_conf.layer_conf[7].pe_conf[2].r0_calc.type = b8(LU_OP) 
sm4_conf.layer_conf[7].pe_conf[2].r0_calc.op = b8(NONE)
sm4_conf.layer_conf[7].pe_conf[2].r0_calc.src = b8(1)

sm4_conf.layer_conf[7].pe_conf[2].r1_calc.type = b8(LU_OP) 
sm4_conf.layer_conf[7].pe_conf[2].r1_calc.op = b8(NONE)
sm4_conf.layer_conf[7].pe_conf[2].r1_calc.src = b8(4)

sm4_conf.layer_conf[7].pe_conf[3].r0_calc.type = b8(LU_OP)
sm4_conf.layer_conf[7].pe_conf[3].r0_calc.op = b8(NONE)
sm4_conf.layer_conf[7].pe_conf[3].r0_calc.src = b8(1)

sm4_conf.layer_conf[7].pe_conf[3].r1_calc.type = b8(LU_OP)
sm4_conf.layer_conf[7].pe_conf[3].r1_calc.op = b8(NONE)
sm4_conf.layer_conf[7].pe_conf[3].r1_calc.src = b8(4)

    #connect
    #IO

sm4_conf.layer_conf[7].cnt = 1000





#layer  0
    #PE
sm4_conf.layer_conf[8].pe_conf[0].r0_calc.type = b8(LU_OP)
sm4_conf.layer_conf[8].pe_conf[0].r0_calc.op = b8(NONE)
sm4_conf.layer_conf[8].pe_conf[0].r0_calc.src = b8(1)

sm4_conf.layer_conf[8].pe_conf[1].r0_calc.type = b8(LU_OP)
sm4_conf.layer_conf[8].pe_conf[1].r0_calc.op = b8(NONE)
sm4_conf.layer_conf[8].pe_conf[1].r0_calc.src = b8(1)

sm4_conf.layer_conf[8].pe_conf[2].r0_calc.type = b8(LU_OP) 
sm4_conf.layer_conf[8].pe_conf[2].r0_calc.op = b8(NONE)
sm4_conf.layer_conf[8].pe_conf[2].r0_calc.src = b8(1)

sm4_conf.layer_conf[8].pe_conf[3].r0_calc.type = b8(LU_OP)
sm4_conf.layer_conf[8].pe_conf[3].r0_calc.op = b8(NONE)
sm4_conf.layer_conf[8].pe_conf[3].r0_calc.src = b8(1)

sm4_conf.layer_conf[8].pe_conf[3].r1_calc.type = b8(LU_OP)
sm4_conf.layer_conf[8].pe_conf[3].r1_calc.op = b8(NONE)
sm4_conf.layer_conf[8].pe_conf[3].r1_calc.src = b8(4)
    #connect
sm4_conf.layer_conf[8].conc_conf.conf_out_route[0].a_src = 8+0 #x0
sm4_conf.layer_conf[8].conc_conf.conf_out_route[0].c_src = 8+1 #x1

sm4_conf.layer_conf[8].conc_conf.conf_out_route[1].a_src = 8+1 #x1
sm4_conf.layer_conf[8].conc_conf.conf_out_route[1].b_src = 8+2 #x2
sm4_conf.layer_conf[8].conc_conf.conf_out_route[1].c_src = 8+2 #x2

sm4_conf.layer_conf[8].conc_conf.conf_out_route[2].a_src = 8+3 #x3
sm4_conf.layer_conf[8].conc_conf.conf_out_route[2].b_src = 12+0 #rk0
sm4_conf.layer_conf[8].conc_conf.conf_out_route[2].c_src = 8+3 #x3

sm4_conf.layer_conf[8].conc_conf.conf_out_route[3].c_src = 12+3 #rki_addr
    #IO
sm4_conf.layer_conf[8].io_conf.addr_r0 = 3#rki_addr
sm4_conf.layer_conf[8].io_conf.out_forward = 1#from fw

sm4_conf.layer_conf[8].cnt = 8
sm4_conf.layer_conf[8].next_cc = 8
sm4_conf.layer_conf[8].last_conf = 1

















