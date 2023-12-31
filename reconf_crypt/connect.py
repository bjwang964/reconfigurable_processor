from pymtl3 import *
from PE_row import *
import random
from conf import *

#class connect_conf_route(object):
#    def __init__(s, src_a=0, src_b=0, src_c=0):
#        s.a_src = src_a
#        s.b_src = src_b
#        s.c_src = src_c
#class connect_conf_io(object):
#    def __init__(s, from_io=0, to_io=0):
#        s.from_io = from_io 
#        s.to_io   = to_io   
#    
#
#class connect_conf(object):
#    def __init__(s):
#        s.conf_out_route = [connect_conf_route() for i in range(ROW_LEN)]
#        s.conf_io = connect_conf_io()

class connector(Component):
    def construct(s):
        #Port
        s.r0     =  [InPort(Bits32) for i in range(ROW_LEN)]
        s.r1     =  [InPort(Bits32) for i in range(ROW_LEN)]
        s.a      =  [OutPort(Bits32) for i in range(ROW_LEN)]
        s.b      =  [OutPort(Bits32) for i in range(ROW_LEN)]
        s.c      =  [OutPort(Bits32) for i in range(ROW_LEN)]
        s.out_r0 =  [OutPort(Bits32) for i in range(ROW_LEN)]
        s.out_r1 =  [OutPort(Bits32) for i in range(ROW_LEN)]
        s.in_a   =  [InPort(Bits32) for i in range(ROW_LEN)]
        s.in_b   =  [InPort(Bits32) for i in range(ROW_LEN)]
        s.in_c   =  [InPort(Bits32) for i in range(ROW_LEN)]

        #out connect
        s.a_wire =  [Wire(Bits32) for i in range(ROW_LEN)]
        s.b_wire =  [Wire(Bits32) for i in range(ROW_LEN)]
        s.c_wire =  [Wire(Bits32) for i in range(ROW_LEN)]
        s.out_r0_wire =  [Wire(Bits32) for i in range(ROW_LEN)]
        s.out_r1_wire =  [Wire(Bits32) for i in range(ROW_LEN)]
        for i in range(ROW_LEN):
            s.a[i] //= s.a_wire[i]
            s.b[i] //= s.b_wire[i]
            s.c[i] //= s.c_wire[i]
            s.out_r0[i] //= s.out_r0_wire[i]
            s.out_r1[i] //= s.out_r1_wire[i]
        #conf
        s.connect_conf = connect_conf()

        @update
        def assign_route():
            for i in range(ROW_LEN) :
                if s.connect_conf.conf_out_route[i].a_src < 4:
                    s.a_wire[i] @= s.r0[s.connect_conf.conf_out_route[i].a_src]
                elif s.connect_conf.conf_out_route[i].a_src < 8:
                    s.a_wire[i] @= s.r1[s.connect_conf.conf_out_route[i].a_src-4]
                elif s.connect_conf.conf_out_route[i].a_src < 12:
                    s.a_wire[i] @= s.in_a[s.connect_conf.conf_out_route[i].a_src-8]
                else:
                    s.a_wire[i] @= s.in_b[s.connect_conf.conf_out_route[i].a_src-12]

                if s.connect_conf.conf_out_route[i].b_src < 4:
                    s.b_wire[i] @= s.r0[s.connect_conf.conf_out_route[i].b_src]
                elif s.connect_conf.conf_out_route[i].b_src < 8:
                    s.b_wire[i] @= s.r1[s.connect_conf.conf_out_route[i].b_src-4]
                elif s.connect_conf.conf_out_route[i].b_src < 12:
                    s.b_wire[i] @= s.in_a[s.connect_conf.conf_out_route[i].b_src-8]
                else:
                    s.b_wire[i] @= s.in_b[s.connect_conf.conf_out_route[i].b_src-12]

                if s.connect_conf.conf_out_route[i].c_src < 4:
                    s.c_wire[i] @= s.r0[s.connect_conf.conf_out_route[i].c_src]
                elif s.connect_conf.conf_out_route[i].c_src < 8:
                    s.c_wire[i] @= s.r1[s.connect_conf.conf_out_route[i].c_src-4]
                elif s.connect_conf.conf_out_route[i].c_src < 12:
                    s.c_wire[i] @= s.in_a[s.connect_conf.conf_out_route[i].c_src-8]
                else:
                    s.c_wire[i] @= s.in_b[s.connect_conf.conf_out_route[i].c_src-12]



            for i in range(ROW_LEN):
                s.out_r0_wire[i] @= s.r0[i]
                s.out_r1_wire[i] @= s.r1[i]

    def update_conf(s,connect_conf):
        s.connect_conf = connect_conf
        print("update connect configure", end="   ")
        for i in range(ROW_LEN):
            print(s.connect_conf.conf_out_route[i].__dict__, end="   ")
        print("")
        print(s.connect_conf.conf_io.__dict__)

class test_bench(Component):
    def construct(s):
        s.connect = connector()
        s.cnt = [Wire(Bits32) for i in range(ROW_LEN)]
        #route
        s.p_a = [i for i in range(ROW_LEN)]
        s.p_b = [i for i in range(ROW_LEN)]
        s.p_c = [i for i in range(ROW_LEN)]
        s.from_io = [0 for i in range(ROW_LEN)]
        s.to_io = b1(0)
        s.conf = connect_conf()

        @update
        def assign_conf():
            s.conf.conf_io.from_io = [random.randint(0,1) for i in range(ROW_LEN)]
            for i in range(ROW_LEN):
                s.p_a[i] = random.randint(0,3)
                s.p_b[i] = random.randint(0,3)
                s.p_c[i] = random.randint(0,3)
                s.conf.conf_out_route[i] = connect_conf_route(s.p_a[i],s.p_b[i],s.p_c[i])
            s.connect.update_conf(s.conf)
                
        @update
        def assign_cnt():
            for i in range(ROW_LEN):
                s.cnt[i]  @= b32(random.randint(1,1000))

        @update
        def assign_input():
            for i in range(ROW_LEN):
                s.connect.r0[i] @= s.cnt[i]
                s.connect.in_a[i] @= s.cnt[i]
                s.connect.in_b[i] @= s.cnt[i]
                s.connect.in_c[i] @= s.cnt[i]


        @update
        def assign_assert():
            for i in range(len(s.connect.connect_conf.conf_io.from_io)):
                if s.connect.connect_conf.conf_io.from_io[i] == 0:
                    assert s.connect.a[i] == s.connect.r0[s.connect.connect_conf.conf_out_route[i].a_src]
                    assert s.connect.b[i] == s.connect.r0[s.connect.connect_conf.conf_out_route[i].b_src]
                    assert s.connect.c[i] == s.connect.r0[s.connect.connect_conf.conf_out_route[i].c_src]
                else:
                    assert s.connect.a[i] == s.connect.in_a[i]
                    assert s.connect.b[i] == s.connect.in_b[i]
                    assert s.connect.c[i] == s.connect.in_c[i]

        #@update_ff
        #def always_print():
        #    if s.connect.connect_conf.conf_io.from_io == b1(0):
        #        for i in range(ROW_LEN):
        #            print(s.connect.r0[i], end='                                    ')
        #        print('')
        #        for i in range(ROW_LEN):
        #            print(\
        #            s.connect.connect_conf.conf_out_route[i].a_src,':', s.connect.a[i], \
        #            s.connect.connect_conf.conf_out_route[i].b_src,':', s.connect.b[i], \
        #            s.connect.connect_conf.conf_out_route[i].c_src,':', s.connect.c[i], \
        #            end='      ')
        #        print('')
        #    else:
        #        for i in range(ROW_LEN):
        #            print(s.connect.in_a[i], s.connect.in_b[i], s.connect.in_c[i],end='     ')
        #        print('')
        #        for i in range(ROW_LEN):
        #            print(s.connect.a[i], s.connect.b[i], s.connect.c[i], end='      ')
        #        print('')

            

def test_foo():
    tb = test_bench()
    tb.apply(DefaultPassGroup())
    tb.sim_reset()
    for i in range(10000):
        print("clk posedge------------------")
        tb.sim_tick()

