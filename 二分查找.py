# encoding: utf-8

def binary_search(alist, data):
    """
    非递归解决二分查找
    """
    n = len(alist)
    first = 0
    last = n - 1
    print(last)
    while first <= last:
        # " / "就表示浮点数除法，返回浮点结果;" // "表示整数除法
        mid = (last+first)//2
        if alist[mid] > data:
            last = mid - 1
        elif alist[mid] < data:
            first = mid + 1
        else:
            return True
    return False

def binary_search2(alist, data):
    """
    递归解决二分查找
    """
    n = len(alist)
    if n < 1:
        return False
    mid = n//2
    if alist[mid] > data:
        return binary_search2(alist[0:mid], data)
    elif alist[mid] < data:
        return binary_search2(alist[mid+1:], data)
    else:
        return True

alist = [0, 1, 10, 88, 19, 9, 1]
alist = sorted(alist)
if binary_search2(alist, 19):
    print("ok")
else:
    print("false")