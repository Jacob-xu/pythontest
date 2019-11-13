import psutil
import os
import time
#import sys


def killprocess(sleeptime,processname):
    time.sleep(sleeptime)
    pids = psutil.pids()
    for pid in pids:
        p = psutil.Process(pid)
        if p.name() == processname:
            cmd = 'taskkill /F /IM ' + processname
            os.system(cmd)
            print("kill success")
#        else:
#            print("process inexistence")
    input("Press <enter>")

def helpinfo():
    print("----使用说明----\n")
    
if __name__ == '__main__':
#    a=sys.argv[0:]
    processname = input("进程名:")
    sleeptime = int(input("等待时间:"))
    killprocess(sleeptime,processname)
#    choose = a[1]
#    print(a)
#    if choose == 'help':
#        helpinfo()
#    elif choose == 'kill':
#        processname = a[2]
#        sleeptime = int(a[3])
#        killprocess(sleeptime,processname)
