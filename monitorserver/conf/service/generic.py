#!/usr/bin/env python
#coding:utf-8

class BaseService(object):
    """
    定义一个基类，设置一些基本的公用变量，以供其他方法调用
    """
    def __init__(self):
        self.name = 'BaseService'
        self.interval = 30
        self.last_time = 0
        self.plugin_name = 'your_plugin_name'
        self.triggers = {}