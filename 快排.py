def quick_sort(array):
    # 为空或者只包含一个元素的数组是有序的，直接返回
    if len(array) < 2:
        return array
    else:
        # 设定基线条件
        key = array[0]
        # 所有小于基线条件的元素组成一个数组
        left = [i for i in array[1:] if i <= key]
        # 所有大于基线条件的元素组成一个数组
        right = [i for i in array[1:] if i > key]
# 对于小于和大于的数组循环重复上面的排序
    return quick_sort(left) + [key] + quick_sort(right)

alist = [0, 10, 88, 19, 9, 1, 7]
print(quick_sort(alist))