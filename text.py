"""
默认参数
    调用函数时，如果没有传递参数，则会使用默认参数。
    以下示例中如果没有传入age参数，则使用默认值。
def printinfo(name,age=25):
    print("名字={0},年龄={1}".format(name,age))
printinfo(age=20,name="王五")
printinfo(name="张三")
输出结果
名字=王五,年龄=20
名字=张三,年龄=25

不定长参数
（1）函数中用*arg方式接收数据，以元组（tuple）的形式传参
def func(x,*args):
    print("x={0},args={1}".format(x,args))

    result=x
    for i in args:
        result=result+i
        return result
print("result=",func(1,2,3))

print(func(1))
函数func中args参数名称可以不一样，但符号*必须有。可以不给args传参数，这也是允许的。

输出结果
x=1,args=(2, 3)
result= 3

x=1,args=()
1

(2)函数中用**kargs方式接收数据，以字典（dict）的形式传参。
def func(x, **kargs):
    print('x=', x)
    print('kargs=', kargs)

print(func(1, a=1,b=2,c=3))

输出结果

x= 1
kargs= {'a': 1, 'b': 2, 'c': 3}
用**kargs的形式收集值，会得到字典类型的数据，
因为字典是以“键-值”对形式出现的，所以传值的时候也要说明“键”和值。


结合*和**的传递参数:
(1)def func(x,y,*args, **kargs):
    print('x=', x)
    print('y=', y)
    print('args=', args)
    print('kargs=', kargs)

print(func(1,2,3,2,a=1,b=2,c=3))
输出结果
x= 1
y= 2
args= (3, 2)
kargs= {'a': 1, 'b': 2, 'c': 3}

(2)def func(x,y,**kargs,*args):
    print('x=', x)
    print('y=', y)

    print('kargs=', kargs)
    print('args=', args)

print(func(1,2,a=1,b=2,c=3,2,2))

输出结果
SyntaxError: invalid syntax（无效语法）

(3)def func(x,*args,y,**kargs):
    print('x=', x)
    print('y=', y)

    print('kargs=', kargs)
    print('args=', args)

print(func(1,2,2,a=1))
输出结果
TypeError: func() missing 1 required keyword-only argument: 'y'

(4)def func(*args,**kargs,y,x):
    print('x=', x)
    print('y=', y)

    print('kargs=', kargs)
    print('args=', args)

print(func(1,2,a=1,1,1))
输出结果
SyntaxError: invalid syntax

函数作为参数传递
函数可以作为一个对象进行参数传递。作为参数被传递的函数也称为回调函数。
下面的例子中函数名为func的函数就作为参数进行传递，传递给test函数。
def test(fun,a,b):
    print(fun(a,b))

def func(x,y):
    return 2*x+y

test(func,2,2)

输出结果
6

test()函数的第一个参数fun就是一个函数对象。将函数func()作为参数传递
给test()函数，test中的参数fun就拥有了函数func()的功能。
因此可以提高程序的灵活性。可以使用上面的test()函数，带入不同的函数参数。
可以使用lambda创建匿名函数作函数参数。例如test((lamdba x,y:2*x+y),2,2)

大胆的写
def test(fun,d,a,b,c):
    print(fun(a,b),c)

def func(x,y):
    return 2*x+y

test(func,2,2,3)
输出结果
6 3
"""






"""
项目名称：教务管理系统
项目小组：狂拽酷炫吊炸天
小组成员：
小组口号：高薪就业找达内
项目简介：
    
初定功能模块：
    登录界面模块
        初定功能：根据不同身份自动选择登录入口   
    学生模块
        初定功能： 1.修改个人信息
                  2.查看个人信息
                  3.浏览消息   
    教职工模块
        初定功能：1.修改个人信息
                 2.查看个人信息
                 3.浏览消息
                 4.发布消息
                 5.管理自己发布消息   
    管理员模块
        初定功能：1.注册教职工
                 2.注册学生
                 3.管理所有信息
                 4.发布消息
                 5.审核教职工发布的消息
                 6.初始化教职工和学生密码
    用户界面模块
    

系统环境等：

项目管理：
    人员分工：        
        李俊宏：待定
        姚双双：待定
        李朔：待定
        马泽宏：待定
        陈磊：待定
    项目进度：
        第一阶段：待定
        第二阶段：待定
        第三阶段：待定
            。
            。
"""


# list01=[12,565,24]
# for i,j in enumerate(list01):
#     print("i={0},j={1}".format(i,j))


# def func(x,*args,y,**kargs):
#     print('x=', x)
#     print('y=', y)
#
#     print('kargs=', kargs)
#     print('args=', args)
#
# print(func(1,2,y=2,a=1))

# import os
# file01=os.stat("/home/tarena/1905ljh/data/linklist.py").st_size
# print(file01)

# with open('/home/tarena/1905ljh/text01.csv','r+',encoding="utf-8") as file01:
#     file01.write("'你好',20,'hao'\n")
#     file01.write("'ok',22,'ee'\n")
#     file01.write("'好',10,'hdfgfd'\n")


# import csv
# with open("/home/tarena/1905ljh/text01.csv","r+",newline='') as file02:
#     c=csv.writer(file02)
#     c.writerow(['asdsads',25,'dsad'])
#     c.writerow(['sads', 5, 'ad'])
#     c.writerow(['ds', 2, 'sad'])

# class Aaa:
#     def __call__(self, a):
#         print(a)
# a=Aaa()
# a('sadsa')

# import os
# import time
# while True:
#     data=os.popen('iostat').read()
#     print(data)
#     time.sleep(5)

import subprocess
re=subprocess.call(['ping','127.0.0.0'])
print(re)
