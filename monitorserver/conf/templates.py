#!/usr/bin/env python
#coding:utf-8

from  service import  linux,network

class BaseTemplate(object):
    """
    定义一个基类，方便调用，同时也方便维护
    """
    def  __init__(self):
        self.name = 'your templatename'
        self.groupname = 'your group name'
        self.hosts=[]
        self.service=[]

class LinuxTemplate(BaseTemplate):
    """
    定义监控模板，继承基类重写方法，定义模板名及监控的类别
    """
    def __init__(self):
        super(LinuxTemplate,self).__init__()
        self.name = 'LinuxTemplate'
        self.service = [
            linux.cpu,
            linux.memory
        ]

class NetworkTemplate(BaseTemplate):
    """
    定义监控模板，继承基类重写方法，定义模板名及监控的类别
    """
    def __init__(self):
        super(NetworkTemplate,self).__init__()
        self.name = 'NetworkTemplate'
        self.service = [
            linux.cpu,
            network.nic
        ]

if __name__ == "__main__":
    t = LinuxTemplate()
    for service in t.service:
        service = service()
        if service.name == "linux_cpu":
            service.interval = 120
        print service.name,service.interval

    print "-------t2--------below"
    t2 = LinuxTemplate()
    for service in t2.service:
        service = service()
        print service.name,service.interval