#!/usr/bin/env python
#coding:utf-8

import  redis
class Redis_helper(object):
    def __init__(self):
        self.__conn = redis.Redis(host="10.36.3.74",port=6379)
        self.chan = "81.7"
    def pub(self,msg):
        self.__conn.publish(self.chan,msg)
    def sub(self):
        pub = self.__conn.pubsub()
        pub.subscribe(self.chan)
        pub.parse_response()
        return pub
    def redisadd(self,*args):
        self.__conn.set(*args)
    def redislistadd(self,*args):
        self.__conn.lpush(*args)