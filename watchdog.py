import platform 
import win32api
import win32con
import re
import os
import psutil
from time import sleep

sysinfo = platform.architecture()[0]


    
def watchdog():
#    key = getkey()
#    path = win32api.RegQueryValueEx(key,'ProgramPath')[0] + 'data\\utdata'
    path = input("请输入监控目录:")
    monitor_dir = path
    os.listdir(monitor_dir)
    now_file = dict([(f,None)for  f in os.listdir(monitor_dir)])
    while True:
        new_file = dict([(f,None)for  f in os.listdir(monitor_dir)])
        added = [f for f in new_file if not f in now_file]
        removed = [f for f in now_file if not f in new_file]
        if added:
            print ("新增文件:",",".join(added))
        if removed:
            print ("删除文件:",",".join(removed))
            break
        now_file = new_file

        
if __name__ == '__main__':
    print("=====watchdog=====")
    watchdog()