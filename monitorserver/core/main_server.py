#!/usr/bin/env python
#coding:utf-8

from redisbase import Redis_helper
import  serialize
import  action_process

class monitorserver(object):
    def __init__(self,ip,port):
        self.ip = ip
        self.port = port
        self.hosts = serialize.all_host_configs()
        self.redis_service = Redis_helper()

    def handler(self):
        redis_sub = self.redis_service.sub()
        while True:
            msg = redis_sub.parse_response()
            print "rcv:",msg
            action_process.action_process(self,msg)

            print "waiting for new msg"
            for host,val in self.hosts["hosts"].items():
                print host ,val
    def run(self):
        self.handler()
if __name__ == "__main__":
    service = monitorserver("0.0.0.0",8882)
    service.run()