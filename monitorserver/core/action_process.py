#!/usr/bin/env python
#coding:utf-8
import  serialize
def  action_process(server_instance,msg):
    msg = eval(msg[2])
    func_name = msg.keys()[0]
    #print func_name
    func = getattr(serialize,func_name)
    func(server_instance,msg[func_name])