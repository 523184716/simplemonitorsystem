#!/usr/bin/env python
#coding:utf-8

def monitor():
    mem_dic = {}
    with open("/proc/meminfo","r") as file:
        mem_list = file.readlines()
        for line in mem_list:
            lines = line.split(":")[0]
            lines2 = line.split(":")[1].strip().split()[0]
            #print lines,lines2
            if lines == "MemTotal":
                mem_dic["MemTotal"] = lines2
            elif lines == "MemAvailable":
                mem_dic["used"] = int(mem_dic["MemTotal"]) - int(lines2)
            else:
                pass
    return mem_dic

if __name__ == "__main__":
    monitor()