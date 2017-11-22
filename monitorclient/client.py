#!/usr/bin/env python
#coding:utf-8

from  redisbase import Redis_helper
from conf import  config_setting
#host_ip = config_setting.host_ip
import  time
import threading
from plugin import plugin_api
key = "HostConfig::%s" % config_setting.host_ip
print key
class monitorclient():

    def __init__(self,server,port):
        self.server = server
        self.port = port
        self.configs = {}
        self.redis_service = Redis_helper()
    def fomat_data(self,key,value):
        msg = {key:value}
        return msg
    def config_get(self):
        """
        从redis数据库中获取此主机的相关数据
        :return:
        """
        config = self.redis_service.redisget(key)
        if config:
            self.configs = eval(config)
            return True
        else:
            print "failed"
    def handler(self):
        """
        根据获取到的相关数据来循环启动函数去收集监控需要的数据信息
        :return:
        """
        if self.config_get():
            print self.configs
            while True:
                for service_name,val  in self.configs["services"].items():
                    plugin_name,interval,last_check = val
                    if time.time() - last_check > interval:
                        t = threading.Thread(target=self.task,args=(service_name,plugin_name))
                        t.start()
                        self.configs["services"][service_name][2] = time.time()
                    else:
                        next_run = interval - (time.time() - last_check)
                        print "%s  will be run in next %s second" % (service_name,next_run)
                time.sleep(5)
        else:
            pass
    def task(self,service_name,plugin_name):
        """
        收集监控数据信息,调用Redis的订阅发布把数据返回给server端
        :func 反射来确定是否有对应的方法:
        :result 调用反射或得的方法来返回数据:
        :msg 格式化数据
        :return:
        """
        print "\033[32m;----going to service:\033[0m", service_name,plugin_name
        func = getattr(plugin_api,plugin_name)
        result = func()
        msg = self.fomat_data(
            "report_service_data",
            {
                "ip":config_setting.host_ip,
                "service_name":service_name,
                "data":result
            }
        )
        self.redis_service.pub(msg)
    def run(self):
        """
        启动函数
        :return:
        """
        self.handler()

if __name__ == "__main__":
    service = monitorclient("1",2)
    service.run()
