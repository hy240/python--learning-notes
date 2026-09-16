#day2(运算符)
#1.算术运算符
#   +,-,*,/,//,%,**(加,减,乘,除,整除,取余,幂)
a =10 
b =10
print(a+b) #加
print(a-b) #减
print(a*b) #乘
print(a/b) #除
print(a//b) #整除
print(a%b) #取余
print(a**b) #幂
#2.比较运算符
#   ==,!=,>,<,>=,<=
print(a == b) #等于
print(a != b) #不等于
print(a > b) #大于
print(a < b) #小于
print(a >= b) #大于等于
print(a <= b) #小于等于
#3.赋值运算符
#   =,+=,-=,*=,/=,//=,%=,**=   
print(a) #10
a += 1 #a = a + 1   
print(a) #11
#4.逻辑运算符
#   and,or,not
#优先顺序: not > and > or
#not 
print(not a) #False
#and:两个条件都为True,结果才为True
print(a > 5 and a < 15) #True
#or:两个条件有一个为True,结果就为True
print(a > 5 or a < 15) #True
#5.成员运算符
#   in,not in
#查看是否存在相关的元素
list1 = [1,2,3,4,5]
print(1 in list1) #True
print(6 in list1) #False
#6.身份运算符
#   is, is not
#查看两个变量是否引用自同一个对象
a = 10 
b = 10
print(a is b) #True
print(a is not b) #False    


#补充:海象运算符
#形式 变量名 := 表达式
#作用:将表达式的值赋值给变量,并返回该值
name = input("请输入你的名字:")
if (n := len(name)) > 5:
    print(f"你的名字太长了,长度为{n}")
# 实例
#1 .关于温度计算
f = float(input("请输入华氏温度:"))
s =(f - 32)/1.8
print(f"华氏温度为:{f},摄氏温度为:{s}")
#计算圆周率
import math 
long = float(input("请输入圆的周长:"))
zhoucang =long / (2*math.pi)
print(f"圆的周长为:{long},半径为:{zhoucang}")

