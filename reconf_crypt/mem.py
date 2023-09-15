from pymtl3 import *
import random

MEM_DEEP = 10
class mem_obj(object):
    def __init__(s, deep):
        s.mem_core = [b32(0) for i in range(deep)]
    def read(s, addr):
        return s.mem_core[addr]
    def write(s,addr,data):
        s.mem_core[addr] = data
class mem(Component):
    def construct(s, deep):
        #Port
        s.rdata = OutPort(Bits32)
        s.wdata = InPort(Bits32)
        s.addr  = InPort(Bits32)
        s.we    = InPort()

        #mem obj
        s.mem_obj = mem_obj(deep)

        #out connect
        s.rdata_wire = Wire(Bits32)
        s.rdata_wire //= s.rdata

        #input reg
        s.wdata_reg = Wire(Bits32)
        s.addr_reg  = Wire(Bits32)
        s.we_reg    = Wire()


        @update_ff
        def always():
            s.wdata_reg <<= s.wdata
            s.addr_reg  <<= s.addr
            s.we_reg    <<= s.we

        @update
        def assign_write_read():
            if(s.we_reg == b1(1)):
                s.mem_obj.write(s.addr_reg, s.wdata_reg)
            else:
                s.rdata_wire @= s.mem_obj.read(s.addr_reg)
            
class test_bench(Component):
    def construct(s):
        s.mem = mem(MEM_DEEP)
        s.addr = Wire(Bits32)
        s.rdata = Wire(Bits32)
        s.wdata = Wire(Bits32)
        s.we =     Wire()
        s.ref_mem =[b32(0) for i in range(MEM_DEEP)] 

        #connect
        s.mem.addr //= s.addr
        s.mem.rdata //= s.rdata
        s.mem.wdata //= s.wdata
        s.mem.we //= s.we

        @update
        def assgin_op():
            s.we   @= b1(random.randint(0,1))
            s.addr @= random.randint(0,MEM_DEEP-1)
            if s.we == b1(1):
                s.wdata @= b32(random.randint(0,32))

        @update_ff
        def always_print():
            if s.we == b1(1):
                print("out write:", s.addr, s.wdata)
            else:
                print("out read:", s.addr, s.rdata)
            print(s.mem.mem_obj.mem_core)
                
            

        
def test_foo():
    tb = test_bench()
    tb.apply(DefaultPassGroup())
    tb.sim_reset()
    for i in range(10):
        print("clk------------------")
        tb.sim_tick()
