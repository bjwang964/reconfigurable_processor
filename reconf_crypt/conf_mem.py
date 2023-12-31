from pymtl3 import *
from PE import *
from PE_row import *
from connect import *
from array_layer import *
from sm4_conf import *

CONF_MEM_DEEP=50
class conf_mem_obj(object):
    def __init__(s):
        s.conf_mem_core = [layer_conf() for i in range(CONF_MEM_DEEP)]
        for i in range(len(sm4_conf.layer_conf)):
            s.conf_mem_core[i] = sm4_conf.layer_conf[i]

    def read(s, addr):
        return s.conf_mem_core[addr]


conf_mem = conf_mem_obj()
        
