"""
P163.希尔排序
    基本思想：希尔排序是把记录按下标的一定增量分组，对每组使用直接插入排序算法排序；
    随着增量逐渐减少，每组包含的关键词越来越多，当增量减至1时，整个文件恰被分成一组，算法便终止。
    属于不稳定排序。
"""
def Shell(array):
    l = len(array)
    gap = l // 2
    while gap > 0 :
        for i in range(gap,l):
            temp = array[i]
            j = i
            while j >= gap and array[j - gap] > temp:
                array[j] = array[j - gap]
                j -= gap
            array[j] = temp
            print(array)
        gap = gap // 2
    return array

if __name__ == '__main__':

    print("最终排序结果为:\n",Shell([49, 38, 65, 97, 26, 13, 27, 49, 55, 4]))