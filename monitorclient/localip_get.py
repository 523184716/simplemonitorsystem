#!/usr/bin/env python
#coding:utf-8

import system_classify
import  socket
def Get_local_ip():
    # system_result = system_classify()
    # if system_result == "window":
    localIP = localIP = socket.gethostbyname(socket.gethostname())
    return  localIP


