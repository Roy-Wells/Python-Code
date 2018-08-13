"""
P28.二分查找
    基本思想：二分查找的基本思想是将n个元素分成大致相等的两部分，取a[n/2]与x做比较，如果x=a[n/2],则找到x,算法中止；
    如果x<a[n/2],则只要在数组a的左半部分继续搜索x,如果x>a[n/2],则只要在数组a的右半部搜索x.
    O(N)=O(log2n)
"""
def BinarySearch(array,key):
    #在列表的首尾设置两个指针
    head = 0
    tail = len(array) - 1
    while(head <= tail):
        #根据首尾指针计算出中间指针，并不断更新
        #这里需要注意的是。在python2与python3中的整除方法稍微不一样
        #python3中的整除为——"//"
        mid = head + (tail - head)//2
        #而python2中的整除为"/".python 2.7 里，不管除数和被除数种是否有浮点数，得到的结果都是浮点数
        # 如果分母和分子都是整数，得到的结果就是整数;
        #而且得到的整数不是四舍五入后的结果，而是无论小数点后的数值如何，直接抹去。
        #"//"则表示为不管除数和被除数种是否有浮点数，得到的结果都是整数
        if (key < array[mid]):
            tail = mid - 1
        elif (key > array[mid]):
            head = mid + 1
        else:
            return mid
    return -1
if __name__ == "__main__":
    print (BinarySearch([1,2,3,5,6,8,9,11,14,52],9))