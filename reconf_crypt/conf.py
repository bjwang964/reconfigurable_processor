from macro import *
from pymtl3 import *
#type:LU/AU/LUT
#op  :calc operat
#src :src operator bit map
class conf_calc(object):
    def __init__(s, tp=b8(LU_OP), op=b8(NONE), src=b8(1)):
        s.type = tp
        s.op   = op
        s.src  = src
#r0/1/2_calc:r0/1/2 calc configure
class PE_conf(object):
    def __init__(s):
        s.r0_calc = conf_calc()
        s.imm     = b32()
class connect_conf_route(object):
    def __init__(s, src_a=0, src_b=0, src_c=0):
        s.a_src = src_a
        s.b_src = src_b
        s.c_src = src_c
class connect_conf_io(object):
    def __init__(s):
        s.from_io = [0 for i in range(ROW_LEN)] 
        s.to_io   = 0
class connect_conf(object):
    def __init__(s):
        s.conf_out_route = [connect_conf_route() for i in range(ROW_LEN)]
        s.conf_io = connect_conf_io()
class io_conf(object):
    def __init__(s, addr_r0=0, out_forward=0, src_a=0, src_b=0, src_c=0):
        s.addr_r0 = addr_r0
        s.out_forward = out_forward
        s.src_a = src_a
        s.src_b = src_b
        s.src_c = src_c
class forward_conf(object):
        def __init__(s):
            s.forward_en = 0
class layer_conf(object):
    def __init__(s):
        s.pe_conf = [PE_conf() for i in range(ROW_LEN)]
        s.conc_conf = connect_conf()
        s.last_conf = 0
        s.cnt = 0
        s.next_cc = 0
class array_conf(object):
    def __init__(s):
        s.layer_conf = [layer_conf() for i in range(COL_LEN)]
        s.io_conf    = [io_conf() for i in range(COL_LEN)]
        s.forward_conf = forward_conf()
