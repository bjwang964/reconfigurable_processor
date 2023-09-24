from pymtl3 import *
from PE_row import *
from macro import *

class io_row(Component):
    def construct(s):
        #port
        s.r0    =   [InPort(Bits32) for i in range(ROW_LEN)]
        s.rf_addr=  OutPort(Bits32)
        s.rf_in =   InPort(Bits128)
        s.forward_in=   [InPort(Bits32) for i in range(ROW_LEN)]
        s.forward_out=  [OutPort(Bits32) for i in range(ROW_LEN)]
        s.out_a =   [OutPort(Bits32) for i in range(ROW_LEN)]
        s.out_b =   [OutPort(Bits32) for i in range(ROW_LEN)]
        s.out_c =   [OutPort(Bits32) for i in range(ROW_LEN)]
        #out connect
        s.a_wire=   [Wire(Bits32) for i in range(ROW_LEN)]
        s.b_wire=   [Wire(Bits32) for i in range(ROW_LEN)]
        s.c_wire=   [Wire(Bits32) for i in range(ROW_LEN)]
        s.addr  =   Wire(Bits32)
        s.r0_wire=  [Wire(Bits32) for i in range(ROW_LEN)]
        s.forward_wire = [Wire(Bits32) for i in range(ROW_LEN)]
        for i in range(ROW_LEN):
            s.out_a[i] //= s.a_wire[i]
            s.out_b[i] //= s.b_wire[i]
            s.out_c[i] //= s.c_wire[i]
        s.rf_addr //= s.addr
        s.io_conf = io_conf()

        @update
        def assign_route():
            s.addr @= s.r0[s.io_conf.addr_r0]
            if s.io_conf.out_forward == b1(1):
                for i in range(ROW_LEN):
                    s.r0_wire[i]   @=   s.forward_in[i]
            else:
                for i in range(ROW_LEN):
                    s.r0_wire[i]   @=   s.rf_in[(i+1)*32-1:i*32]
            for i in range(ROW_LEN):
                s.forward_out[i]    @=  s.r0[i]
            #full connect
            for i in range(ROW_LEN):
                s.a_wire[i] @=  s.r0_wire[s.io_conf.src_a]
                s.b_wire[i] @=  s.r0_wire[s.io_conf.src_b]
                s.c_wire[i] @=  s.r0_wire[s.io_conf.src_c]
    
    def update_conf(s, io_row_conf):
        s.io_conf = io_row_conf
        print("update io row configure", end="  ")
        print(s.io_conf.__dict__)
        
class forward_port(Component):
    def construct(s):
        s.in_forward    =   [InPort(Bits32) for i in range(ROW_LEN)]
        s.out_forward   =   [OutPort(Bits32) for i in range(ROW_LEN)]

class forward_bus(Component):
    def construct(s):
        s.forward_port  =   [forward_port() for i in range(COL_LEN)]
        s.forward_conf  =   forward_conf()
        #out
        s.out_wire      =   [Wire(Bits32) for i in range(ROW_LEN)]
        s.port_wire     =   []
        for i in range(COL_LEN):
            s.port_wire[i]     =   [Wire(Bits32) for j in range(ROW_LEN)]
            for j in range(ROW_LEN):
                s.forward_port[i].out_forward[j] //= s.port_wire[i][j]
        
        @update
        def assign():
            k = 0
            for i in range(ROW_LEN):
                for j in range(COL_LEN):
                    if s.forward_conf.forward_en :
                        break
                    else:
                        k+=1
                if k == COL_LEN :
                    k = 0
                s.out_wire[i]   @=    s.forward_port[k].in_forward[i]
            for i in range(COL_LEN):
                for j in range(ROW_LEN):
                    s.port_wire[i][j]   @=  s.out_wire[j]
    def update_conf(s, forward_conf):
        s.forward_conf = forward_conf
        print("update io forward configure", end="  ")
        print(s.forward_conf.__dict__)

    
