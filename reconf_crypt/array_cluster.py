from pymtl3 import *
from PE import *
from PE_row import *
from connect import *
from array_layer import *

COL_LEN=32
class array_conf(object):
    def __init__(s):
        s.layer_conf = [layer_conf() for i in range(COL_LEN)]

class array_cluster(Component):
    def construct(s):
        #Port
        #s.in_a        =  [InPort(Bits32)  for i in range(COL_LEN)]
        #s.in_b        =  [InPort(Bits32)  for i in range(COL_LEN)]
        #s.in_c        =  [InPort(Bits32)  for i in range(COL_LEN)]
        #s.out_r0      =  [OutPort(Bits32) for i in range(COL_LEN)]
        
        s.up_a        =  [InPort(Bits32)  for i in range(ROW_LEN)]
        s.up_b        =  [InPort(Bits32)  for i in range(ROW_LEN)]
        s.up_c        =  [InPort(Bits32)  for i in range(ROW_LEN)]
        s.down_a      =  [OutPort(Bits32) for i in range(ROW_LEN)]
        s.down_b      =  [OutPort(Bits32) for i in range(ROW_LEN)]
        s.down_c      =  [OutPort(Bits32) for i in range(ROW_LEN)]

        #layer
        s.layer       = [array_layer() for i in range(COL_LEN)]

        
        #layer connect
        for i in range(ROW_LEN):
            s.layer[0].up_a[i] //= s.up_a[i]
            s.layer[0].up_b[i] //= s.up_b[i]
            s.layer[0].up_c[i] //= s.up_c[i]
            s.down_a[i] //= s.layer[COL_LEN-1].down_a[i]
            s.down_b[i] //= s.layer[COL_LEN-1].down_b[i]
            s.down_c[i] //= s.layer[COL_LEN-1].down_c[i]
        for l in range(COL_LEN-1):
            for p in range(ROW_LEN):
                s.layer[l].down_a[p] //= s.layer[l+1].up_a[p]
                s.layer[l].down_b[p] //= s.layer[l+1].up_b[p]
                s.layer[l].down_c[p] //= s.layer[l+1].up_c[p]
        for l in range(COL_LEN):
            for p in range(ROW_LEN):
                s.layer[l].in_a[p] //= Bits32(0)
                s.layer[l].in_b[p] //= Bits32(0)
                s.layer[l].in_c[p] //= Bits32(0)


        ##io connect
        #for l in range(COL_LEN):
        #    for p in range(ROW_LEN):
        #        s.layer[l].in_a[p] //= s.in_a[l][p]
        #        s.layer[l].in_b[p] //= s.in_b[l][p]
        #        s.layer[l].in_c[p] //= s.in_c[l][p]
        #        s.out_r0[l][p] //= s.layer[l].out_r0[p] 

        #conf
        s.array_conf = array_conf()

class test_bench(Component):
    def construct(s):
        s.arr = array_cluster()
        s.cnt = Wire(Bits32)
        s.array_conf = array_conf()
        #input wire
        s.up_a        =  [Wire(Bits32)  for i in range(ROW_LEN)]
        s.up_b        =  [Wire(Bits32)  for i in range(ROW_LEN)]
        s.up_c        =  [Wire(Bits32)  for i in range(ROW_LEN)]
        s.down_a        =  [Wire(Bits32)  for i in range(ROW_LEN)]
        s.down_b        =  [Wire(Bits32)  for i in range(ROW_LEN)]
        s.down_c        =  [Wire(Bits32)  for i in range(ROW_LEN)]
        for i in range(ROW_LEN):    
            s.arr.up_a[i]  //=  s.up_a[i]  
            s.arr.up_b[i]  //=  s.up_b[i]  
            s.arr.up_c[i]  //=  s.up_c[i]  
            s.down_a[i] //= s.arr.down_a[i]
            s.down_b[i] //= s.arr.down_b[i]
            s.down_c[i] //= s.arr.down_c[i]

        @update
        def assign_init():  
            #init conf
            if(s.cnt == b32(0)):
                print("conf array")
            #init input
            for i in range(ROW_LEN):
                s.up_a[i] @= b32(0)
                s.up_b[i] @= b32(0)
                s.up_c[i] @= b32(0)


        @update_ff
        def always_print():
            s.cnt <<= s.cnt+b32(1)
            for i in range(ROW_LEN):    
                print("")
def test_foo():
    tb = test_bench()
    tb.apply(DefaultPassGroup())
    tb.sim_reset()
    for i in range(10):
        print("clk posedge------------------")
        tb.sim_tick()

