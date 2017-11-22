#!/usr/bin/env python
#coding:utf-8
import time
from  test import Redis_helper

def redissub():
    sub = Redis_helper()
    pub=sub.sub('81')
    return  pub.parse_response()

while True:
    A = redissub()
    print A
    B = Redis_helper()
    date_now = time.strftime("%Y-%m-%d %H:%M:%S")
    C = eval(A[-1])
    C["update"]=date_now
    B.redislistadd("host",C)

