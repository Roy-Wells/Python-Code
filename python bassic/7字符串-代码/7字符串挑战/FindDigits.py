#!/usr/bin/env python3
f = open('/home/shiyanlou/Code/String.txt')
fr = f.read()
s = ''
for i in fr:
        if i.isdigit():
           s += i
print(s)
