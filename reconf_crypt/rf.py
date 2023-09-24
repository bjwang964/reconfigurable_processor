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
        s.rf_obj = rf_core(deep)

        #out connect
        s.rdata_wire = [[Wire(Bits32) for i in range(ROW_LEN)] for j in range(COL_LEN)]
        
        for i in range(COL_LEN):
            for j in range(ROW_LEN):
                s.rdata[i][j] //= s.rdata_wire[i][j]
        
        @update
        def assign():
            for i in range(COL_LEN):
                s.rdata_wire @= s.rf_obj.read(s.addr[i])