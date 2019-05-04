import socket
import threading
import ctypes
import sys

print(ctypes.windll.shell32.IsUserAnAdmin())

class MyThread(threading.Thread):
    def run(self):
        create_server()

def create_server():
    s = socket.socket()
    host = socket.gethostname()
    port = 12345
    s.bind((host, port))
    s.listen(5)
    while True:
        c, addr = s.accept()
        print('Got connection from', addr)
        message = 'Thanks for your messages'
        c.send(message.encode())
        c.close()


def create_client():
    s = socket.socket()
    host = socket.gethostname()
    port = 12345
    s.connect((host, port))
    print(s.recv(1024))


def main():
    t = MyThread()
    t.start()
    create_client()

if __name__ == '__main__':
    main()

