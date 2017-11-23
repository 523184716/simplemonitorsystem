#!/usr/bin/env python
#coding:utf-8

def monitor():
    with open('/proc/loadavg','r') as file:
        load_list = file.read().split()
        load_result = load_list[:3]
    return load_result

if __name__ == "__main__":
    monitor()
