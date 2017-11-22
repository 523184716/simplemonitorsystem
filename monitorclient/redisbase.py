#!/usr/bin/env python
#coding:utf-8

import  redis
from  conf import config_setting
class Redis_helper(object):
    def __init__(self):
        self.__conn = redis.Redis(host=config_setting.redis_ip)
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

    def redisget(self,*args):
        result = self.__conn.get(*args)
        return  result