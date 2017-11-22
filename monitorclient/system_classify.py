#!/usr/bin/env python
#coding:utf-8

import  sys

def system_classfy():
    system_result = sys.platform
    if "win" in system_result:
        result = "window"
    elif "linux" in system_result:
        result = "linux"
    else:
        result = "mac"
    return  result
