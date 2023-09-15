from pymtl3 import *
from PE import *
from PE_row import *
from connect import *
from array_layer import *

class algthm_conf_entry(object):
    def __init__(s):
        s.entry = layer_conf()

class algthm_conf(object):
    def __init__(s):
        s.entry_num = 10
        s.conf_entry = [algthm_conf_entry for i in range(s.entry_num)]
        
