# ThinkinginPython
A way to learn Python

## Python syntax:
 #### 一.参数
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
