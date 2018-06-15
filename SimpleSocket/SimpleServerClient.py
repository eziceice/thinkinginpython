import socket
import threading

class MyThread(threading.Thread):
    def run(self):
        create_server()

def create_server():
    s = socket.socket()
    host = socket.gethostname()
    port = 1234
    s.bind((host, port))
    s.listen(5)
    notconnect = True
    while notconnect:
        c, addr = s.accept()
        print('Got connection from', addr)
        c.send('Thank you for connecting')
        c.close()
        notconnect = False

def create_client():
    s = socket.socket()
    host = socket.gethostname()
    port = 1234
    s.connect((host, port))
    print(s.recv(1024))


def main():
    t = MyThread()
    t.start()
    create_client()

if __name__ == '__main__':
    main()

