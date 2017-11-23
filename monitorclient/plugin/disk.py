#!/usr/bin/env python
#coding:utf-8

import os

def monitor():
    disk_list = os.popen('for i in `df -h |awk \'{print $1}\' | grep /dev/`;do df -h|grep $i|awk \'{print $6}\';done')
    disk_list = disk_list.read().strip().split()
    hd_total = {}
    hd = {}
    for i in disk_list:
        disk = os.statvfs(i)
#        hd['available'] = disk.f_bsize * disk.f_bavail
        hd['capacity'] = disk.f_bsize * disk.f_blocks
        hd['avail'] = disk.f_bsize * disk.f_bfree
        hd['used'] = hd['capacity'] - hd['avail']
        hd_total[i] = hd
    return hd_total
if __name__ == "__main__":
    monitor()