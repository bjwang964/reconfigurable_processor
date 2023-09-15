from pymtl3 import *
class wire_comb(Component):
    def construct(s):
        s.out = Wire(Bits16)

    @method_port
    def comb(s, in0, in1):
        s.out[0:8] @= in0
        s.out[8:16] @= in1
        return s.out
        
        

class ff(Component):    
    def construct(s):
        s.d     = InPort(Bits8)
        s.q     = OutPort(Bits8)
        s.value = Wire(Bits8)
        s.q    //= s.value

        @update_ff
        def always():
            print("FF", s.value)
            s.value <<= s.d

class sync(Component):
    def construct(s):
        s.ff0 = ff()
        s.ff1 = ff()
        s.inter = Wire(Bits8)
        s.q = Wire(Bits8)
        s.cnt = Wire(Bits8)
        s.ff0.d//=s.cnt
        s.ff0.q//=s.inter
        s.inter//=s.ff1.d
        s.ff1.q//=s.q

        s.comb = wire_comb()
        s.ww = Wire(Bits16)

        @update
        def assign0():
            s.cnt @= s.ff1.q+b8(1)
            print("1")

        @update
        def assign_print():
            print(s.ff0.d, s.ff0.q, s.ff1.q, s.ww)
            print("2")
            
        
        @update_once
        def comb_print():
            s.ww @= s.comb.comb(s.ff1.q,s.ff0.q)
            print("3")
        


def test_sync():
    tb = sync()
    tb.apply(DefaultPassGroup())
    tb.sim_reset()
    for i in range(9):
        print("clk----------------------")
        tb.sim_tick()
        tb.ff0.value = b8(8)
        print(tb.ff0.value)
        tb.ff0.value = b8(10)
        print(tb.ff0.value)
