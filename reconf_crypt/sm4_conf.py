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
    #connect
sm4_conf.layer_conf[0].conc_conf.conf_out_route[0].a_src = 0 #x0

sm4_conf.layer_conf[0].conc_conf.conf_out_route[1].a_src = 1 #x1
sm4_conf.layer_conf[0].conc_conf.conf_out_route[1].b_src = 2 #x2

sm4_conf.layer_conf[0].conc_conf.conf_out_route[2].a_src = 3 #x3
sm4_conf.layer_conf[0].conc_conf.conf_out_route[2].b_src = 8+0 #rk0

sm4_conf.layer_conf[0].conc_conf.conf_out_route[3].a_src = 4+3 #rki_addr
    #IO
sm4_conf.layer_conf[0].addr_r0 = 3#rki_addr






