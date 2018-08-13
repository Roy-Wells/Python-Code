"""
P1.最大公约数：
    求解方法（自然语言描述）：
        计算两个非负整数 x，y 。如果y是0，那么最大公约数为x。否则，用x除以y得到余数r。
        x和y的最大公约数即为y和r的最大公约数。
        如此循环，直到递归中的r的值为0，则返回当前x的值，即为x和y的最大公约数
"""
def gcd(x, y):
    if y == 0:
        return x
    r = x % y
    return gcd(y,r)
a = int(input("输入第一个数字"))
b = int(input("输入第二个数字"))
c = gcd(a,b)
print(c)