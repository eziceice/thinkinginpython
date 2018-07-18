import logging
logging.basicConfig(level=logging.INFO, filename='mylog.log')
logging.info('program start')
logging.info('Trying to divide 1 by 0')
print(1/0)
