#分支结构
#关于if和elif分支
#列子
#1:计算BMI指数(身高/体重的平方)
height = float(input("请输入您的身高(m): "))
weight = float(input("请输入您的体重(kg): "))
BMI = weight / (height ** 2)
if BMI < 18.5:
    print("您的BMI指数为%.2f,体重过轻" % BMI)
elif BMI < 24:
    print("您的BMI指数为%.2f,体重正常" % BMI)
else:
    print("您的BMI指数为%.2f,体重过重" % BMI)
#2:计算成绩等级
score = float(input("请输入您的成绩: "))
if score >90:
    print("您的成绩等级为A")
elif score >80:
    print("您的成绩等级为B")
elif score >70:
    print("您的成绩等级为C")    
elif score >60:
    print("您的成绩等级为D")
#3:网页状态
status_code = int(input("请输入网页状态码: "))
if status_code == 200:
    print("网页状态正常")
elif status_code == 404:
    print("NOT FOUND")
else:
    print("网页状态异常")   
#进阶matach-case分支结构
#以评级为列
score =float(input("请输入您的成绩: "))
match score:
    case 90 : 
        print("您的成绩等级为A")
    case 80 :       
        print("您的成绩等级为B")
    case 70 :   
        print("您的成绩等级为C")

#常见分支的运用
#求分段函数
x =float(input("请输入x的值: "))
if x < -1:
    y = 5 * x + 3
elif x >= -1 and x <= 1:
    y = x + 2
else :
    y =3 * x - 5
print(float(y))

#计算三角形面积
a = float(input("your long"))
b = float(input("your long"))
c = float(input("your long"))
if a + b == c and a + c == b and b + c == a:
    preimeter = (a + b + c) 
s = preimeter / 2
area = (s*(a-b) + s*(a-c) + s*(b-c))/2
print(float(area))
