from pymtl3 import *
from macro import *
#4*32
class rf_core(object):
    def __init__(s, deep):
        s.rf_core = [b32(0) for i in range(deep)]
    def read(s, addr):
        return s.rf_core[addr]
class rf_OutPort(Component):
     #Port
    def construct(s):
        s.rfout = [OutPort(Bits32) for i in range(ROW_LEN)]
class rf(Component):
    def construct(s, deep):
        #Port
        s.addr = [InPort(Bits32) for i in range(COL_LEN)]
        s.rdata= [[OutPort(Bits32) for i in range(ROW_LEN)] for j in range(COL_LEN)]
                    

        #rf obj
        s.rf_obj = [rf_core(deep) for i in range(ROW_LEN)]

        #out connect
        s.rdata_wire = [[Wire(Bits32) for i in range(ROW_LEN)] for j in range(COL_LEN)]
        
        for i in range(COL_LEN):
            for j in range(ROW_LEN):
                s.rdata[i][j] //= s.rdata_wire[i][j]
        
        @update
        def assign():
            for i in range(COL_LEN):
                for j in range(ROW_LEN):
                        s.rdata_wire[i][j] @= s.rf_obj[j].read(s.addr[i][0:9])#TODO:addr length
class test_bench(Component):
    def construct(s):
        s.rf = rf(1024)
        for i in range(10):
            for j in range(ROW_LEN):
                s.rf.rf_obj[j].rf_core[i] = i + 1
        s.addr = [Wire(Bits32) for i in range(COL_LEN)]
        s.rdata = [[Wire(Bits32) for i in range(ROW_LEN)] for j in range(COL_LEN)]

        for i in range(COL_LEN):
            s.addr[i] //= s.rf.addr[i]
            for j in range(ROW_LEN):
                s.rdata[i][j]//= s.rf.rdata[i][j]
        @update
        def assign_init():
            for i in range(COL_LEN):
                s.addr[i] @= b32(i)
        @update_ff
        def always_print():
            print("out read:", s.addr, s.rdata)

def test_foo():
    tb = test_bench()
    tb.apply(DefaultPassGroup())
    tb.sim_reset()
    for i in range(10):
        print("clk--------")
        tb.sim_tick()