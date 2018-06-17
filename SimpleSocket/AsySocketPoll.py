import socket, select
s = socket.socket()
host = socket.gethostname()
port = 1234
s.bind((host, port))
s.listen(5)
fdmap = {s.fileno(): s}
p = select.poll()
p.register(s)
while True:
    events = p.poll()
    for fd, event in events:
        if fd == s.fileno():
            c, addr = s.accept()
            print('Got connection from ', addr)
            p.register(c)
            fdmap[c.fileno()] = c
        elif event & select.POLLIN:
            data = fdmap[fd].recv(1024)
            if not data:
                print(fdmap[fd].getpeername(), ' disconnected')
                p.unregister(fd)
                del fdmap[fd]
        else:
            print(data)