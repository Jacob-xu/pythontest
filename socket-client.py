# 导入socket模块
import socket

# 创建socket对象
s = socket.socket()

s.connect(("127.0.0.1", 6666))
print(s.recv(1024))
s.close()