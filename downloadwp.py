#!/usr/bin/python
#encoding:utf-8
#import urllib
import xml.etree.ElementTree as ET
import os 
import sys
import requests
from PIL import Image

            
def getmd5(path):
    xmlFilePath = os.path.abspath(path)
    try:
        tree = ET.parse(xmlFilePath)
#        print ("tree type:", type(tree))
        # 获得根节点
        root = tree.getroot()
    except Exception as e:
        print ("parse test.xml fail!")
        sys.exit()
    
#    遍历root的下一层
    for child in root:
        for child in child:
            with open('md5.txt', 'a') as f:
                f.write(child.attrib['md5'] + '.jpg' + '\n') 
    input("Press <enter>") 

def getmd5w(path):
    xmlFilePath = os.path.abspath(path)
    try:
        tree = ET.parse(xmlFilePath)
#        print ("tree type:", type(tree))
        # 获得根节点
        root = tree.getroot()
    except Exception as e:
        print ("parse test.xml fail!")
        sys.exit()
    
#    遍历root的下一层
    for child in root:
        for child in child:
            with open('md5w.txt', 'a') as f:
                f.write(child.attrib['md5_4_3'] + '.jpg' + '\n') 
    input("Press <enter>")
#def Schedule(a,b,c):
#    '''''
#    a:已经下载的数据块
#    b:数据块的大小
#    c:远程文件的大小
#   '''
#    per = 100.0 * a * b / c
#    if per > 100 :
#        per = 100
#    print('%.2f%%' % per)

def downloadjpg(pathmd5):
    file = open(pathmd5,'rb').read().decode().split("\r\n")
    for i in range(0,len(file)-1):
        downloadpath = "http://www.eyeprotect.wallpaperm.cmcm.com/" + file[i]
        print(downloadpath)
        r = requests.get(downloadpath) # create HTTP response object
        with open("wallpaper/" + file[i],'wb') as f:
            f.write(r.content)
    input("Press <enter>") 

def downloadjpgw(pathmd5):
    file = open(pathmd5,'rb').read().decode().split("\r\n")
    for i in range(0,len(file)-1):
        downloadpath = "http://www.eyeprotect.wallpaperm.cmcm.com/" + file[i]
        print(downloadpath)
        r = requests.get(downloadpath) # create HTTP response object
        with open("wallpaperw/" + file[i],'wb') as f:
            f.write(r.content)
    input("Press <enter>") 
    
def getjpgsize(jpgpath):
#    path =  "D:\\1333\\护眼\\getimgsize\\wallpaper\\"
    list = os.listdir(jpgpath)
    for i in range (0,len(list)):
        img = Image.open(jpgpath + list[i])
        if int(img.size[0]) < 1920 or int(img.size[1]) < 1080:
            print(list[i],img.size)     
    input("Press <enter>") 

def getjpgsizew(jpgpath):
#    path =  "D:\\1333\\护眼\\getimgsize\\wallpaper\\"
    list = os.listdir(jpgpath)
    for i in range (0,len(list)):
        img = Image.open(jpgpath + list[i])
        if int(img.size[0]) < 1440 or int(img.size[1]) < 1080:
            print(list[i],img.size)     
    input("Press <enter>") 
    
def help():
    print("---说明---")
    print("\n")
    print("配置文件请于该文件放置同级目录,以下所有命令后面加上w代表执行普屏壁纸：getmd5w")
    print("\n")
    print("getmd5 --- 获取图片名称")   
    print("\n")         
    print("downloadjpg --- 下载图片")     
    print("\n")       
    print("getsize --- 获取图片大小")
            
if __name__ == "__main__":
#    path = "D:\\1333\\护眼\\getimgsize\\healthctrlwallpaper.dat"
    a = sys.argv[0:]
    choose = a[1]
    pypath = str(os.getcwd())
#    print(os.getcwd()) #获取当前工作目录路径
#    print(b)
    if choose == 'getmd5':
        path = pypath + "\\healthctrlwallpaper.dat"
        getmd5(path)
    elif choose == 'getmd5w':
        path = pypath + "\\healthctrlwallpaper.dat"
        getmd5w(path)
    elif choose == 'downloadjpg':
        pathmd5 = pypath + "\\md5.txt"
        downloadjpg(pathmd5)
    elif choose == 'downloadjpgw':
        pathmd5 = pypath + "\\md5w.txt"
        downloadjpgw(pathmd5)
    elif choose == 'getsize':
        jpgpath = pypath + "\\wallpaper\\"
        getjpgsize(jpgpath)
    elif choose == 'getsizew':
        jpgpath = pypath + "\\wallpaperw\\"
        getjpgsizew(jpgpath)
    elif choose == 'help':
        help()
