from sys import getrefcount

#引用计数
a1 = 1000000
a2 = 1000000

print(id(a1))
print(id(a2))

#检验a1和a2是同一个东西
print(a1 is a2)

#获取引用计数
print(getrefcount(a1))
print(getrefcount(a2))