"""
P79.算数表达式求值
----------------------------------
    设计一个程序，假设接受一个输入字符串，最后输出一个表达式的值。
    例如：
        （1+（（2 + 3）*（4 * 5）））
    解题思路：
        我们根据以下4种情况从左至右逐个将这些实体送入栈处理。
            1.将操作数压入操作数栈
            2.将运算符压入运算符栈
            3.忽略左括号
            4.在遇到右括号时，弹出一个运算符，弹出所需数量的操作数，并将运算符和操作数的运算结果压入操作数栈。
"""
import queue
# 判断当前迭代列表元素是否为运算符
# @oper 运算符
# @return True||False
def is_operation(oper):
    if oper == '+' or oper == '-' or oper == '*' or oper == '/':
        return True
    else:
        return False
# 对两个数字进行运算操作
# @a    浮点数数字变量
# @0    运算操作符
# @b    浮点数数字变量
# @return 浮点数运算结果
def get_aob(a,o,b):
    if o == '+':
        return a + b
    if o == '-':
        return a - b
    if o == '*':
        return a * b
    if o == '/':
        return a / b
# 进行运算的主要方法
# @expression   带有公式的字符串
# return    浮点数计算结果
def getValue(expression):
    exp_list = list(expression)     #将公式字符串转换为列表
    ops = queue.LifoQueue()         #创建操作符栈
    vals = queue.LifoQueue()        #创建数字栈
    temp = ''                       #创建临时存储变量，用以保存大于10的数值
    if(exp_list):
        for item in exp_list:
            if is_operation(item):
                ops.put(item)
                if (temp):
                    vals.put(float(temp))
                    temp = ''

            elif item == ')':
                if (temp):
                    vals.put(float(temp))
                    temp = ''
                op = ops.get()
                result = vals.get()
                result = get_aob(result,op,vals.get())
                vals.put(float(result))
            elif item == ' ' or item == '(':
                continue
            else:
                temp += item
        return vals.get()

if __name__ == "__main__":
    print(getValue('(1+((2 + 9)*(4 * 5)))'))

