from pymtl3 import *
from PE import *
from PE_row import *
from connect import *
from array_layer import *
from conf_mem import *
from macro import *
from conf import *



class layer_conf_controller(Component):
    def construct(s):
        s.conf_queue = [layer_conf() for i in range(QUEUE_LEN)]
        s.head_index = 0

    #@method_port
    def go_step(s,array_layer):
        s.conf_queue[s.head_index].cnt = s.conf_queue[s.head_index].cnt -1 
        if s.conf_queue[s.head_index].cnt  == 0: #deq and update next conf
            if s.conf_queue[s.head_index].conf.last_conf == 1:
                s.head_index = 0
            else:
                read_next_conf(head_index,s.conf_queue[s.head_index].next_cc)#enq
                s.head_index = (head_index + 1)% QUEUE_LEN
                layer_conf = s.conf_queue[s.head_index].conf
                array_layer.update_conf(layer_conf)#apply conf

    #@method_port
    def read_next_conf(s, head_index, conf_cnt):
        new_conf = conf_mem.read(conf_cnt)
        s.conf_queue[head_index] = new_conf
        
