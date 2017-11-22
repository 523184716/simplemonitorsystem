#!/usr/bin/env python
#coding:utf-8

from  data_process import  *
import  generic
class nic(generic.BaseService):
    def __init__(self):
        super(nic,self).__init__()
        self.name = 'nic_network'
        self.interval = 30
        self.plugin_name = 'get_network_info'
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