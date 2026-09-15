#day1
#认识量
#1 整数(int),整数的表示形式有十进制、二进制、八进制、十六进制
#如果要将一个整数转换为二进制、八进制、十六进制，可以使用内置函数bin()、oct()、hex()
a = 190
bin(a)  # 二进制
oct(a)  # 八进制
hex(a)  # 十六进制
#
#2 浮点数(float),浮点数的表示形式有科学计数法
b = 3.14
#3 字符串(str),字符串是由字符组成的有限序列，字符串可以使用单引号、双引号、三引号表示
c = "Hello, World!"
#三者的转化
s = 11 
d = 1.111
f = "111"
print(int(d)) #将浮点数转换为整数
print(float(s)) #将整数转换为浮点数 ,会精确到小数点后6位
print(str(d)) #将浮点数转换为字符串
print(int(f)) #将字符串转换为整数
#在转化整数时可以自定义进制
print(int(f,base =2 ))#2进制
print(int(f,base =8 ))#8进制
print(int(f,base =16 ))#16进制
#4 chr()和ord()函数
#chr()将字符转化成相应的ASCII码
print(chr(90))
print(ord("s")) #ord()将ASCII码转化成相应的字符
#5 布尔值(bool),布尔值只有两个值True和False,布尔值可以和整数进行运算，True等于1，False等于0
print(True + 1)  # 2#查看程序是否正确
#6 查看数据类型type()
print(type(a)) #查看变量a的数据类型
print(type(b)) #查看变量b的数据类型
print(type(c)) #查看变量c的数据类型 
print(type(s)) #查看变量s的数据类型
