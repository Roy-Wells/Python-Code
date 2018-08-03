#!/usr/bin/env python3
basic_salary = 1500
bouns_rate = 200
commission_rate = 0.02
numberofcamera = int(input("Enter the number of inputs sold:"))
price = float(input("Enter the price of camera"))
bouns = (bouns_rate * numberofcamera)
commission =(commission_rate * price * numberofcamera)
print("Bonus = {:6.2f}".format(bouns))
print("Commission ={:6.2f}".format(commission))
print("Gross salary = {:6.2f}".format(basic_salary + bouns + commission))

