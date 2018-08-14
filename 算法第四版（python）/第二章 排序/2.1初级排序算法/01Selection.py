"""
P156.选择排序
    基本思想：首先，找到数组中最小的那个元素。其次，将它和数组的第一个元素交换位置。
    再次，在剩下的元素中找到最小的元素，将它与数组的第二个元素交换位置。如此往复，直到将整个数组排序。
    8 5 2 6 9 3 1 4 0 7
    0 5 2 6 9 3 1 4 8 7
    0 1 2 6 9 3 5 4 8 7
    0 1 2 3 9 6 5 4 8 7
    0 1 2 3 4 6 5 9 8 7
    0 1 2 3 4 5 6 9 8 7
    0 1 2 3 4 5 6 7 8 9
    时间复杂度：O(n^2)
    特点：
        1.运行时间和输入顺序无关
        2.数据移动是最少的。原地操作是选择排序唯一的优点。当空间复杂度要求较高时，可以考虑选择排序。
"""
def Selection(array):
    l = len(array)
    for i in range(l):
        min = i
        #range(start, stop[, step])
        #start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
        #stop: 计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
        #step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)
        for j in range (i+1, l):
            if (array[min]>array[j]):
                min = j
        if min != i:
            array[i],array[min] = array[min],array[i]
    return array
if  __name__ == '__main__':
    print(Selection([17,23,20,14,12,25,1,20,81,14,11,12]))