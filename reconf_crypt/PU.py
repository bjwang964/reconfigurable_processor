from pymtl3 import *
from macro import *
from conf import *

class PU(Component):
    def construct(s):
        #port
        s.a    = [InPort(Bits32) for i in range(ROW_LEN)]
        s.out   = [OutPort(Bits32) for i in range(ROW_LEN)]
        #out connect
        s.out_wire = [Wire(Bits32) for i in range(ROW_LEN)]
        s.out_Byte = [Wire(Bits8) for i in range(16)]
        #s.tmp_wire = [[Wire(Bits8) for i in range(16)] for i in range(8)]
        for i in range(ROW_LEN):
            s.out[i] //= s.out_wire[i]
        #conf
        s.pu_conf = pu_conf()
        @update
        def assign_pu():
            for i in range(16):
                if s.pu_conf.stage_se[i] < 4 :
                    s.out_Byte[i] @= s.a[0][8*i:8*(i+1)]
                elif s.pu_conf.stage_se[i] < 8 :
                    s.out_Byte[i] @= s.a[1][8*(i-4):8*(i-3)]
                elif s.pu_conf.stage_se[i] < 12 :
                    s.out_Byte[i] @= s.a[2][8*(i-8):8*(i-7)]
                else :
                    s.out_Byte[i] @= s.a[3][8*(i-12):8*(i-11)]
            #s.out_wire[0] @= s.out_Byte[0] | s.out_Byte[1] << 8 | s.out_Byte[2] << 16 | s.out_Byte[3] << 24
            for i in range(4):
                s.out_wire[i] @= zext(s.out_Byte[i*4] | s.out_Byte[i*4+1] << 8 | s.out_Byte[i*4+2] << 16 | s.out_Byte[i*4+3] << 24, 32)
        # @update
        # def assign_route():
        #     for i in range(8):
        #         for j in range(16):
        #             if i == 0:
        #                 if j < 4 :
        #                     s.tmp_wire[i][j] @= s.r0[0][8*j:8*(j+1)]
        #                 elif j < 8 :
        #                     s.tmp_wire[i][j] @= s.r0[1][8*j:8*(j+1)]
        #                 elif j < 12 :
        #                     s.tmp_wire[i][j] @= s.r0[2][8*j:8*(j+1)]
        #                 else:
        #                     s.tmp_wire[i][j] @= s.r0[3][8*j:8*(j+1)]
        #             else:
        #                 if s.pu_conf.stage_se[i-1][j/2] == SE_ST:
        #                     s.tmp_wire[i][j] @= s.tmp_wire[i-1][j]
        #                 else:
        #                     s.tmp_wire[i][j] @= 
        
    
class PU_FUNC(object):
    def construct(s):
        s.benes_net = CalleePort(method = s.benes_net_)

    def benes_stage(stage_se_sel, stage_in, stage_out):
        for i in range(8):
            if(stage_se_sel[i] == SE_CR):
                stage_out[2*i] = stage_in[2*i+1]
                stage_out[2*i+1] = stage_in[2*i]
            else:
                stage_out[2*i] = stage_in[2*i]
                stage_out[2*i+1] = stage_in[2*i+1]

    def benes_net_(s, calc, din, dout):
        #benes network for 16B * 16B
        din_wire = [[]]
        din_wire[0] = din
        for i in range(8):
            s.benes_stage(calc.se_sel[i], din_wire[i], din_wire[i+1])
        return din_wire[7][0] | din_wire[7][1] << 8 | din_wire[7][2] << 16