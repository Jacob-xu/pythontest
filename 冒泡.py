#冒泡排序
def bubble_sort(lists):
    #获取数组长度
    count = len(lists) - 1
    #N个元素遍历N次
    for index in range(count, 0 , -1):
        print(index)
        #第i个和第i+1个依次对比
        for sub_index in range(index):
            print("sub_index = ", sub_index)
            #大的元素冒上去
            if lists[sub_index] > lists[sub_index+1]:
                lists[sub_index],lists[sub_index+1] = lists[sub_index+1],lists[sub_index]
                print(lists)
    return lists


alist = [0, 10, 88, 19, 9, 1]
print(bubble_sort(alist))