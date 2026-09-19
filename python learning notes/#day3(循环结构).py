#day3(循环结构)
#1.用time模块进行循环
import time
print("hi world")
time.sleep(1)#sleep,可以间隔时间运行代码
#运用for-in 对循环范围进行限制
for _ in range(6):#补充:range(a ：b : c)a表示start(开始值),b表示end(结束值,但是取不到end值),c(表示跨度,有+-,表示方向)
    print("hi")
time.sleep(9) 
#2:用循环求和
tatal = 0
for i in range(101):
    tatal += i
print(tatal)
#进阶可以穿插相关筛选条件
#关于偶数相加
tatal2 = 0
for i1 in range(101):
    if i1 % 2 == 0:
     tatal2 += i1
print(tatal2)
#也可用sum()求和
print(sum(range(0,101,2)))
#while循环
tatal3 = 0
i2 = 1
while i2 <=100:
    tatal3 += i2
    i2 += 1
print(tatal3) 
#break:结束循环(可以运用到if中如果该条件不满足则停止)
#continue:跳过该程序(if如果在该条件下满足则跳过)
#循环嵌套(实例:九九乘法表)
for x in range(0,10):
    for g in range(1,x+1):
        print(f"{x}*{g}:",x*g,end="/t")
        print(f"{x}*{g}:",x*g,end="/t")