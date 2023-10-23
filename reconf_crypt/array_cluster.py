from pymtl3 import *
from PE import *
from PE_row import *
from connect import *
from array_layer import *
from macro import *
from conf import *
from sm4_conf import *
from io_row import *
from rf import *
#class array_conf(object):
#    def __init__(s):
#        s.layer_conf = [layer_conf() for i in range(COL_LEN)]




class array_cluster(Component):
    def construct(s):
        #Port
        #s.in_a        =  [InPort(Bits32)  for i in range(COL_LEN)]
        #s.in_b        =  [InPort(Bits32)  for i in range(COL_LEN)]
        #s.in_c        =  [InPort(Bits32)  for i in range(COL_LEN)]
        #s.out_r0      =  [OutPort(Bits32) for i in range(COL_LEN)]
        
        s.up_go       = InPort()
        s.up_a        =  [InPort(Bits32)  for i in range(ROW_LEN)]
        s.up_b        =  [InPort(Bits32)  for i in range(ROW_LEN)]
        s.up_c        =  [InPort(Bits32)  for i in range(ROW_LEN)]
        s.down_a      =  [OutPort(Bits32) for i in range(ROW_LEN)]
        s.down_b      =  [OutPort(Bits32) for i in range(ROW_LEN)]
        s.down_c      =  [OutPort(Bits32) for i in range(ROW_LEN)]


        #layer
        s.layer       = [array_layer() for i in range(COL_LEN)]
        s.forward_bus_r0 = forward_bus()
        s.forward_bus_r1 = forward_bus()
        s.rf          = rf(1024)
        s.stop_req    = [Wire() for i in range(COL_LEN)]
        s.stop_resp   = [Wire() for i in range(COL_LEN)]
        #stop connect
        for i in range(COL_LEN):
            s.stop_req[i] //= s.layer[i].stop_o        
            s.stop_resp[i] //= s.layer[i].stop_i

        @update
        def assign_stop():
            for i in range(COL_LEN):
                for j in range(i, COL_LEN):
                    if s.stop_req[j] == b1(1):
                        s.stop_resp[i] @= b1(1)
                        break
                    else:
                        s.stop_resp[i] @= b1(0)
                


        #io connect
        for i in range(COL_LEN):
            for j in range(ROW_LEN):
                s.forward_bus_r0.in_forward[i][j] //= s.layer[i].out_forward[j]
                s.forward_bus_r0.out_forward[j] //= s.layer[i].in_forward[j]

                s.forward_bus_r1.in_forward[i][j] //= s.layer[i].out_forward_r1[j]
                s.forward_bus_r1.out_forward[j] //= s.layer[i].in_forward_r1[j]

                s.layer[i].rf_rdata[j]    //= s.rf.rdata[i][j]
            s.layer[i].rf_addr  //= s.rf.addr[i]        
        #layer connect
        s.layer[0].up_go //= s.up_go
        for i in range(ROW_LEN):
            s.layer[0].up_a[i] //= s.up_a[i]
            s.layer[0].up_b[i] //= s.up_b[i]
            s.layer[0].up_c[i] //= s.up_c[i]
            s.down_a[i] //= s.layer[COL_LEN-1].down_a[i]
            s.down_b[i] //= s.layer[COL_LEN-1].down_b[i]
            s.down_c[i] //= s.layer[COL_LEN-1].down_c[i]
        for l in range(COL_LEN-1):
            s.layer[l].down_go //= s.layer[l+1].up_go
            for p in range(ROW_LEN):
                s.layer[l].down_a[p] //= s.layer[l+1].up_a[p]
                s.layer[l].down_b[p] //= s.layer[l+1].up_b[p]
                s.layer[l].down_c[p] //= s.layer[l+1].up_c[p]
        # for l in range(COL_LEN):
        #     for p in range(ROW_LEN):
        #         s.layer[l].in_a[p] //= s.io_row[l].out_a[p]
        #         s.layer[l].in_b[p] //= s.io_row[l].out_b[p]
        #         s.layer[l].in_c[p] //= s.io_row[l].out_c[p]
                


        ##io connect
        #for l in range(COL_LEN):
        #    for p in range(ROW_LEN):
        #        s.layer[l].in_a[p] //= s.in_a[l][p]
        #        s.layer[l].in_b[p] //= s.in_b[l][p]
        #        s.layer[l].in_c[p] //= s.in_c[l][p]
        #        s.out_r0[l][p] //= s.layer[l].out_r0[p] 

        #conf
        s.array_conf = array_conf()

    def update_conf(s, array_conf):
        s.array_conf = array_conf
        s.forward_bus_r0.update_conf(s.array_conf.forward_conf)
        s.forward_bus_r1.update_conf(s.array_conf.forward_conf)
        for i in range(COL_LEN):
            print("*******************************************")
            print("***************", i,"layer", "******************")
            print("*******************************************")
            s.layer[i].update_conf(s.array_conf.layer_conf[i])
    def init_conf(s):
        for i in range(COL_LEN):
            s.layer[i].layer_conf_controller.init_conf(i)


class test_bench(Component):
    def construct(s):
        s.arr = array_cluster()
        s.cnt = Wire(Bits32)
        s.array_conf = array_conf()
        #input wire
        s.up_go       = Wire()
        s.up_a        =  [Wire(Bits32)  for i in range(ROW_LEN)]
        s.up_b        =  [Wire(Bits32)  for i in range(ROW_LEN)]
        s.up_c        =  [Wire(Bits32)  for i in range(ROW_LEN)]
        s.down_a        =  [Wire(Bits32)  for i in range(ROW_LEN)]
        s.down_b        =  [Wire(Bits32)  for i in range(ROW_LEN)]
        s.down_c        =  [Wire(Bits32)  for i in range(ROW_LEN)]
        for i in range(ROW_LEN):    
            s.arr.up_go //= s.up_go
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
                print("conf array-----------------------------------------------")
                s.arr.update_conf(sm4_conf)
                s.arr.init_conf()
                print("conf array-----------------------------------------------")

                #init input
                for i in range(ROW_LEN):
                    s.up_a[i] @= s.cnt+b32(i)
                    s.up_b[i] @= s.cnt+b32(i)+b32(1)
                    s.up_c[i] @= s.cnt+b32(i)+b32(2)
                    s.up_go   @= b1(1)


        @update_ff
        def always_print():
            s.cnt <<= s.cnt+b32(1)
            print(s.arr.forward_bus_r0.out_forward)
            print(s.arr.forward_bus_r1.out_forward)
            for i in range(COL_LEN):    
                print("------------------------------------------------layer", i,':', s.arr.layer[i].stop_i,"--------------------------------------------------------", s.arr.layer[i].up_go)
                for k in range(ROW_LEN):
                    print("           ","PE",k,"          | ",end='')
                print('')
                for j in range(ROW_LEN):
                    print(s.arr.layer[i].PE_row.pe[j].a,s.arr.layer[i].PE_row.pe[j].b,s.arr.layer[i].PE_row.pe[j].c, end=' | ')
                print("")
                for j in range(ROW_LEN):
                    print('  ',s.arr.layer[i].PE_row.pe[j].r0,'  ', s.arr.layer[i].PE_row.pe[j].r1,end='    | ')
                print("")
            print("rf_read: ", s.arr.rf.addr, "data: ", s.arr.rf.rdata)
            print("======================================================ROUND",int(s.cnt),"======================================================")
            #if int(s.cnt) <COL_LEN :
            #    print('---------------------rounds',s.cnt,'----------------',)
            #    print("start:", end="")
            #    for i in range(ROW_LEN):
            #        print(s.up_a[i], s.up_b[i], s.up_c[i],end="||")
            #    print("")
            #    for i in range(ROW_LEN):
            #        print(s.arr.layer[int(s.cnt)-1].PE_row.pe[i].r0, end='  ')
            #    print("")
                
def test_foo():
    tb = test_bench()
    tb.apply(DefaultPassGroup())
    tb.sim_reset()
    for i in range(COL_LEN*8):
        #print("clk posedge------------------")
        #input()
        tb.sim_tick()

