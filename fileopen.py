import os
f = open('resource/IOTEST.txt', 'r+', True)
f.read()

print(f.read()) #可以在read中指定数字来标注需要读取的字符数
f.write('this is more test\r')
f.seek(int) #找到文件中字符的index并且从此处开始
f.tell() #可以获得当前游标的位置
f.write('123455') #从当前游标的位置开始写入,注意,会覆盖后面的部分
f.readline(int) #int代表当前行中你想获取的字符数.
f.readlines() #可以读取一个文件中的所有行并将其作为list返回.

f.write('\rthis is a test')
f.writelines(['\rthis is', '\ra stupid', '\r12345165151'])