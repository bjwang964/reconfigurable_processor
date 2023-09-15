from pymtl3 import *
from PE_row import *
from connect import *
from copy import deepcopy
class layer_conf(object):
    def __init__(s):
        s.pe_conf = [PE_conf() for i in range(ROW_LEN)]
        s.conc_conf = connect_conf()
        


class array_layer(Component):
    def construct(s):
        #Port
        s.in_a        =  [InPort(Bits32) for i in range(ROW_LEN)]
        s.in_b        =  [InPort(Bits32) for i in range(ROW_LEN)]
        s.in_c        =  [InPort(Bits32) for i in range(ROW_LEN)]
        s.up_a        =  [InPort(Bits32) for i in range(ROW_LEN)]
        s.up_b        =  [InPort(Bits32) for i in range(ROW_LEN)]
        s.up_c        =  [InPort(Bits32) for i in range(ROW_LEN)]

        s.down_a      =  [OutPort(Bits32) for i in range(ROW_LEN)]
        s.down_b      =  [OutPort(Bits32) for i in range(ROW_LEN)]
        s.down_c      =  [OutPort(Bits32) for i in range(ROW_LEN)]
        s.out_r0      =  [OutPort(Bits32) for i in range(ROW_LEN)]

        #PE_ROW   connect
        s.PE_row      =  PE_ROW()
        s.connect     =  connect()

        #conf
        s.layer_conf  = layer_conf()

        #inter connect
        s.inter_r0 = [Wire(Bits32) for i in range(ROW_LEN)]

        for i in range(ROW_LEN):
            s.up_a[i] //= s.PE_row.pe_a[i]
            s.up_b[i] //= s.PE_row.pe_b[i]
            s.up_c[i] //= s.PE_row.pe_c[i]
            s.inter_r0[i] //= s.PE_row.pe_r0[i]

            s.inter_r0[i] //= s.connect.r0[i]
            s.down_a[i]   //= s.connect.a[i]
            s.down_b[i]   //= s.connect.b[i]
            s.down_c[i]   //= s.connect.c[i]

            s.in_a[i]  //= s.connect.in_a[i]
            s.in_b[i]  //= s.connect.in_b[i]
            s.in_c[i]  //= s.connect.in_c[i]
            s.out_r0[i] //= s.connect.out_r0[i]

    
    
    def update_conf(s,layer_conf):
        print("update layer configure")
        s.layer_conf = layer_conf
        for i in range(ROW_LEN):
            s.PE_row.pe[i].update_conf(s.layer_conf.pe_conf[i])
        s.connect.update_conf(s.layer_conf.conc_conf)


    
class test_bench(Component):
    def construct(s):
        s.al = array_layer()
        s.cnt = Wire(Bits32)
        s.layer_conf = layer_conf()
        #output wire
        s.wire_out_r0 = [Wire(Bits32) for i in range(ROW_LEN)]
        for i in range(ROW_LEN):    
            s.wire_out_r0[i] //= s.al.out_r0[i]
        #inter wire
        s.wire_a        =  [Wire(Bits32) for i in range(ROW_LEN)]
        for i in range(ROW_LEN):    
            s.wire_a[i] //= s.al.up_a[i]
            s.wire_a[i] //= s.al.down_a[i]

        @update
        def assign_init():
            #init conf
            if(s.cnt == b32(0)):
                for i in range(ROW_LEN):
                    s.layer_conf.pe_conf[i].r0_calc.type = AU_OP
                    s.layer_conf.pe_conf[i].r0_calc.op = ADD
                    s.layer_conf.pe_conf[i].r0_calc.src = b8(0)
                    s.layer_conf.conc_conf.conf_out_route[i].a_src = i 
                    s.layer_conf.conc_conf.conf_out_route[i].b_src = i 
                    s.layer_conf.conc_conf.conf_out_route[i].c_src = i 
                s.layer_conf.conc_conf.conf_io.from_io = 0
                s.layer_conf.conc_conf.conf_io.to_io = 0

                s.al.update_conf(s.layer_conf)
            #input
            for i in range(ROW_LEN):    
                s.al.up_b[i] @= b32(i)
                s.al.up_c[i] @= b32(i)
                s.al.in_a[i] @= b32(i)
                s.al.in_b[i] @= b32(i)
                s.al.in_c[i] @= b32(i)


        

        @update_ff
        def always_print():
            s.cnt <<= s.cnt+b32(1)
            for i in range(ROW_LEN):    
                print(s.al.up_a[i], end=" ")
            print("")


def test_foo():
    tb = test_bench()
    tb.apply(DefaultPassGroup())
    tb.sim_reset()
    for i in range(10):
        print("clk posedge------------------")
        tb.sim_tick()

