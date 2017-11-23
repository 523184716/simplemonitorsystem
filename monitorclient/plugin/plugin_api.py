#!/usr/bin/env python
#coding:utf-8

import  cpu,load,network,memory,disk

def get_memory_info():
    return memory.monitor()

def get_network_info():
    return  network.monitor()

def get_cpu_status():
    return  cpu.monitor()

def get_load_info():
    return load.monitor()

def get_disk_info():
    return disk.monitor()