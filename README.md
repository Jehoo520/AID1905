# AID1905 第二次周测题

## 一、选择题

1. 下列哪项不是Linux操作系统的特征（D）

> A. Linux操作系统是开源的
>
> B. Linux操作系统有内核，文件系统，shell，应用构成
>
> C. Linux图形化界面和网络功能的支持较差
>
> D. Linux操作系统是一种常用的服务器系统

2. 关于绝对路径和相对路径的说法正确的是（A，B）

> A. 绝对路径是从根目录开始查找文件
>
> B. 相对路径是从当前位置查找文件
>
> C. 使用绝对路径比相对路径方便
>
> D. 使用相对路径比绝对路径方便

3. 关于二叉树的遍历，以下选项中描述错误的是 A，D

> A. 前序遍历是先遍历左子树，然后访问根结点，最后遍历右子树
>
> B. 后序遍历二叉树的过程是一个递归的过程
>
> C.  二叉树的遍历是指不重复地访问二叉树中的所有结点
>
> D. 二叉树的遍历可以分为三种：前序遍历、中序遍历、后序遍历

4. 下面四个选项, 关于with语句描述正确的是(B )

> A. 任何对象都能用with语句进行管理
>
> B. open 函数返回的文件流对象可以用with语句中进行管理
>
> C. with 语句主要用于容易引发异常的异常处理中
>
> D. 在 with 语句内部创建的变量,在with语句之后无法再次访问

5. 下列说法不正确的是（A）

> A. 多进程并发，多线程并发，协程并发原理一样，都是每个客户端创建一个分支进行处
>
> B. select，poll，epoll都是IO多路复用的方法
>
> C. socketserver模块可以实现多进程和多线程的并发模型
>
> D. 协程拥有很好的处理IO并发请求的能力

## 二、简答题

1. 写出下列命令的作用

> ```
> mkdir：创建目录
> touch：如果文件不存在,新建文件
> vi:进入编辑模式
> rm：删除指定的文件名
> cp：复制文件或目录
> ```

2. 请阐述进程、线程、协程，以及他们的应用场景。

> ```
> 1) 一个线程可以多个协程，一个进程也可以单独拥有多个协程
> 2) 线程进程都是同步机制，而协程则是异步
> 3) 协程能保留上一次调用时的状态，每次过程重入时，就相当于进入上一次调用的状态
> 4）每个进程都有自己独立的内存空间，不同进程之间的内存空间不共享
> 5）一个进程可以有多个线程，所有线程共享进程的内存空间，通讯效率高，切换开销小
> 6）协程又称微线程，在单线程上执行多个任务
> ```

3. 请阐述七层模型、四层模型，说明其作用及并列举对应的协议。

> ```
> 七层模型：应用层（FTP），表示层，会话层，传输层（TCP，UDP），网络层，数据链路层，物理层
> 四层模型：应用层，传输层（TCP，UDP），网际层，网络接口
> ```

4. 请使用正则匹配出邮箱及手机号

> ```
> import re
> re.findall(r'\w+\@\w+\.com','1324165132456@qq.com')     
> re.findall(r'1[0-9]{10}','12345678911')
> ```

## 三、编程题

1. 一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

   ```python
   # -*- coding:utf-8 -*-
   class Solution:
       def jumpFloorII(self, number):
           # 写下你的代码
           if number<2:
               return 1
           return self.jumpFloorII(number-1)+self.jumpFloorII(number-2)
           
   ```

2. 请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为`We%20Are%20Happy`。

   ```python
   # -*- coding:utf-8 -*-
   class Solution:
       # s 源字符串
       def replaceSpace(self, s):
           # 写下你的代码
           list01 = []
           for i in s:
               list01.append(i)
           for i in list01:
               if list01[i]==' ':
                   list01[i]='%20'
           return ''.join(list01)
   
   
   
           
   ```
3.  请用代码实现`TCP`或`UDP`的`Socket`通信

   ```python
   tcp服务端
   import socket
s = socket()
   s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
   s.bind(('0.0.0.0',8080))
   s.listen(5)
   connfd,addr=s.accept
   data = connfd.recv(1024)
   print("收到:",data.decode())
   n=connfd.send(b'Thanks')
   print("回复：" ,n)
   connfd.close()
   s.close()
   
   tcp客户端
   import socket
   s= socket()
   server_addr = ('127.0.0.1',8888) 
   s.connect(server_addr)
   data = input("输入内容：")
   s.send(data.encode())
   data = s.recv(1024)
   print("收到回复：",data.decode())
   s.close()
   
   
   ```
   
   