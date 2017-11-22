#!/usr/bin/env python
#coding:utf-8

import  templates

g1 = templates.LinuxTemplate()
g1.groupname = 'test group'
g1.hosts = ["10.36.3.74","10.36.3.90"]

g2 = templates.NetworkTemplate()
g2.groupname = 'puppet service group'
g2.hosts = ['10.36.2.74','10.36.3.74']

monitor_groups = [g1,g2]