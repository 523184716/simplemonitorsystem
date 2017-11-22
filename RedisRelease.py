#!/usr/bin/env python
#coding:utf-8

from test import Redis_helper

def redisrelease(msg):
    pub = Redis_helper()
    pub.pub(msg,'81')

for i in range(11,20):
    data = {'host':"10.36.3.%d"% i,"问题":"cpu is more than 90%"}
    redisrelease(data)