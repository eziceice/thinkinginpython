from configparser import *

CONFIGFILE = 'config.txt'
config = ConfigParser()
config.read(CONFIGFILE)

print(config.get('numbers', 'pi'))
print(config.get('messages', 'greeting')) #第一个参数是所要获取的区块, 第二个参数则是config的名字