#!/usr/bin/env python
#coding:utf-8

import psutil
def monitor():
    cpu_dic = {}
    cpu_last = "%.2f"% psutil.cpu_percent(interval= 0.5)+"%"
    cpu_dic["cpu_last"] = cpu_last
    return cpu_dic

if __name__ == "__main__":
    monitor()