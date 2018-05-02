# ThinkinginPython
A way to learn Python

## Python syntax:
 #### 一. 参数
 ##### 1. 默认参数
 比如两个参数的函数:
 ```
  def power(x, n = 2):
 ```
 当以上函数被调用时,如果只传入x的值,则n的值默认为2.若n和x的值都被传入,则使用传入的值.默认参数的数量是无限制的.
 可以不按照顺序提供默认参数,但是必须将变量的名字写上.
 ```
  def enroll(name, gender, age=6, city='Beijing')：
  //必须这样调用
  enroll('Adam', 'M', city='Tianjin')
 ```
 **默认参数必须指向不可变得对象,不能指向list之类的数据结构,因为默认参数的值在一开始就被计算出来了.**
 **必选参数在前，默认参数在后.**
 ##### 2. 可变参数
 在函数的parameter之前添加一个\*可以将函数变为支持可变参数的函数,在函数内部,可变参数将会转化为一个tuple.同样,在list和tuple之前加一个\*便可以将list和tuple转化为可变参数.
 ##### 3. 关键字参数
 关键字参数的函数允许传入任意个含参数名的参数，这些关键字参数在函数内部自动组装成一个dict.
 ```
  def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
  >>> person('Michael', 30)
  name: Michael age: 30 other: {}
 ```
 kw必定是一个dict的数据结构,注意如果传入一个kw的dict结构,获得的将是一份拷贝而非原来的kw,因此方法内部对kw的改造并不影响之前的object.
 ##### 4. 命名关键字参数
 命名关键字参数允许函数的参数只接受需要的关键字参数.
 ```
  def person(name, age, *, city, job):
    print(name, age, city, job)
  >>> person('Jack', 24, city='Beijing', job='Engineer')
  Jack 24 Beijing Enginee
 ```
 该函数只可以接受city和job作为key的参数.注意中间需要用\*分隔开.命名关键字参数必须要传入参数名.
 #### 参数部分总结
 **\*args是可变参数,接受的是一个tuple.<br>
 \*\*kw是关键字参数，接受的是一个dict.<br>
 可变参数和关键字参数都可以直接传入数值,或先组装成\*tuple和\*\*tw在传到方法里.<br>
 命名关键字参数是为了限制调用者可以传入的参数名,同时也可以提供默认值.<br>
 命名关键字参数必须要在中间添加\*.**<br>
 
 #### 二. 递归函数
 Python中的递归函数和Java类似,也应当注意防止栈溢出的问题.<br>
 栈溢出是指，在计算机中，所有的方法调用都是通过栈(stack)这种数据结构实现的,每当进入一个函数调用,就增加一层栈帧,每当一个函数返回,就减少一层栈帧.由于栈的大小并不是无限的,所以当递归函数的调用次数过多时,就会出现栈溢出(stackoverflow).<br>
 因此,解决栈溢出的方法是采用尾递归优化,尾递归是指,在函数返回时,调用函数本身,同时return语句中不能包含表达式.这样,无论编译器如何调用,递归函数始终只占用一个栈帧.
```
# 递归函数优化之前，容易出现栈溢出的问题
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
''' 
计算过程
===> fact(5)
===> 5 * fact(4)
===> 5 * (4 * fact(3))
===> 5 * (4 * (3 * fact(2)))
===> 5 * (4 * (3 * (2 * fact(1))))
===> 5 * (4 * (3 * (2 * 1)))
===> 5 * (4 * (3 * 2))
===> 5 * (4 * 6)
===> 5 * 24
===> 120
'''
# 优化后
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

''' 
计算过程
===> fact_iter(5, 1)
===> fact_iter(4, 5)
===> fact_iter(3, 20)
===> fact_iter(2, 60)
===> fact_iter(1, 120)
===> 120
'''
```
 从上面我们可以看出,栈的调用情况被简化了.
 #### 三. 高级特性
 ##### 1. 切片
 不同于Java,Python允许操作list就像操作字符串,对于一个list,可以直接使用切片取其中的一段元素.
 ```
 L = list(range(100))
 L[:10]
 L[5:50]
 L[-1:-20] #python支持负index,最后一个数的index是-1
 L[:10:2] #从0到10每2个数取一个
 ```
 切片可以运用于list,tuple和字符串,Java中的substring就类似于Python中切片对字符串的操作.
 ##### 2. 迭代
 Python的迭代不仅可用于list,也可以用于tuple和dict.
```
 d = {'a' : 1, 'b' : 2, 'c' : 3}
 for key in d:
    print(key)

 for value in d.values():
    print(value)

 for k, v in d.items():
    print(k,v)
```
 通过collections模块的Iterable类型来判断一个对象是否可以被迭代对象:
```
 from collections import Iterable
 isinstance('abc',Iterable)
```
 Python中也有类似Java里的下表循环,需要使用enumerate函数将list变成索引-元素对.
```
 for i,value in enumerate(['A','B','C']):
    print(i,value)
 ```
