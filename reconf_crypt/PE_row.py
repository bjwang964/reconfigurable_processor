from pymtl3 import *
from PE import *
from macro import *
class PE_ROW(Component):
    def construct(s):
        #PE
        s.pe = [PE() for i in range(ROW_LEN)]
        #Port
        s.pe_a  = [InPort(Bits32) for i in range(ROW_LEN)]
        s.pe_b  = [InPort(Bits32) for i in range(ROW_LEN)]
        s.pe_c  = [InPort(Bits32) for i in range(ROW_LEN)]
        s.pe_r0 = [OutPort(Bits32) for i in range(ROW_LEN)]

        #connect
        for i in range(ROW_LEN):
            s.pe_a[i]  //= s.pe[i].a
            s.pe_b[i]  //= s.pe[i].b 
            s.pe_c[i]  //= s.pe[i].c 
            s.pe_r0[i] //= s.pe[i].r0

        #@update
        #def assign_print():
        #    print("clk------------------")
        #    for i in range(ROW_LEN):
        #        print(s.pe_a[i], s.pe_b[i], s.pe_c[i],'  |',end='')
        #    print('')
        #    for i in range(ROW_LEN):
        #        print(s.pe_r0[i], '                    |',end='')
        #    print('')
        #    #for i in range(ROW_LEN):
        #    #    print(s.pe[i].conf.r0_calc.type, '                    |',end='')
        #    #print('')

class test_bench(Component):
    def construct(s):
        s.pe_row = PE_ROW()
        s.cnt = Wire(Bits32)
        s.pe_conf = PE_conf()
        s.pe_conf.r0_calc = conf_calc(b8(LUT_OP),b8(ADD),b8(5))
        s.pe_conf.imm = b32(1)

        @update
        def init():
            for i in range(ROW_LEN):
                s.pe_row.pe[i].update_conf(s.pe_conf)

        @update
        def assign():
            for i in range(ROW_LEN):
                s.pe_row.pe_a[i] @= s.cnt+i
                s.pe_row.pe_b[i] @= s.cnt+i+1
                s.pe_row.pe_c[i] @= s.cnt+i+2

        @update_ff
        def always():
            s.cnt  <<= s.cnt + b32(1)
def test_foo():
    tb = test_bench()
    tb.apply(DefaultPassGroup())
    tb.sim_reset()
    tb.sim_tick()
