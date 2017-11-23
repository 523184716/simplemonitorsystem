#!/usr/bin/env python
#coding:utf-8

from data_process import *
import  generic

class cpu(generic.BaseService):
    """
    1.继承父类
    2.super继承父类的__init__（），然后重写里面的域变量
    """
    def __init__(self):
        super(cpu,self).__init__()
        self.name = 'linux_cpu'
        self.interval = 30
        self.plugin_name = 'get_cpu_status'
        self.triggers = {
            'idle':{
                'func':avg,
                'minutes':15,
                'operator':'lt',
                'warning':20,
                'critical':5,
                'data_type':'percentage'
            },
            'iowait': {
                'func': hit,
                'minutes': 10,
                'operator': 'gt',
                'threshole':3,
                'warning': 80,
                'critical': 90,
                'data_type': 'percentage'
            },
        }

class memory(generic.BaseService):
    def __init__(self):
        super(memory,self).__init__()
        self.name = 'linux_memory'
        self.interval = 30
        self.plugin_name = 'get_memory_info'
        self.triggers = {
            'usage':{
                'func':avg,
                'minutes':15,
                'operator':'gt',
                'warning':80,
                'criticla':90,
                'data_type':'percentage'

            }
        }

class load(generic.BaseService):
    def __init__(self):
        super(load,self).__init__()
        self.name = 'linux_load'
        self.interval = 30
        self.plugin_name = 'get_load_info'
        self.triggers = {
            'usage':{
                'func':avg,
                'minutes':15,
                'operator':'gt',
                'warning':80,
                'criticla':90,
                'data_type':'percentage'

            }
        }

class disk(generic.BaseService):
    def __init__(self):
        super(disk,self).__init__()
        self.name = 'linux_disk'
        self.interval = 30
        self.plugin_name = 'get_disk_info'
        self.triggers = {
            'usage':{
                'func':avg,
                'minutes':15,
                'operator':'gt',
                'warning':80,
                'criticla':90,
                'data_type':'percentage'

            }
        }