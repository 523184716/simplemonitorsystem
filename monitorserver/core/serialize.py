#!/usr/bin/env python
#coding:utf-8

#import global_settings
from monitorsystem.monitorserver.conf import hosts
from  redisbase import Redis_helper
import time

def hosts_config_serializer(host_ip):
    """
    根据输入的主机来获取所有模板中的需要监控的plugin_name
    :param host_ip:
    :return:
    """
    applied_service = []
    configs = {
        'services':{},
    }
    for group in hosts.monitor_groups:
        if host_ip in group.hosts:
           # for service in group.service:
                #service = service()
            #applied_service.extend([service.name,service.plugin_name,service.interval])
            applied_service.extend(group.service)
        else:
            print "failese"
    for service in set(applied_service):
        services = service()
        configs['services'][services.name] = [services.plugin_name,services.interval,0]
    return configs

def flush_all_host_config_into_redis():
    applied_hosts = []
    redis_service = Redis_helper()
    for group in hosts.monitor_groups:
        applied_hosts.extend(group.hosts)
    applied_hosts = set(applied_hosts)
    for host in applied_hosts:
        host_config = hosts_config_serializer(host)
        key = "HostConfig::%s" % host
        redis_service.redisadd(key,host_config)

def all_host_configs():
    configs = {"hosts":{}}
    for group in hosts.monitor_groups:
        for host_ip in group.hosts:
            configs["hosts"][host_ip] = {}
    return  configs

def report_service_data(server_instance,msg):
    host_ip = msg["ip"]
    service_status_data = msg["data"]
    service_name = msg["service_name"]
    print server_instance.hosts
    server_instance.hosts["hosts"][host_ip][service_name] = {
        "data":service_status_data,
        "time_stamp":time.time()
    }
    print server_instance.hosts

    key = "StatusData::%s" % host_ip
    server_instance.redis_service.redisadd(key,server_instance.hosts["hosts"][host_ip])
if __name__ == "__main__":
    server = flush_all_host_config_into_redis()
    server