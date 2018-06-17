import socket, select
s = socket.socket()
host = socket.gethostname()
port = 1234
s.bind((host, port))
s.listen(5)
inputs = [s]
while True:
    rs, ws, es = select.select(inputs,[],[]) #如果没有输入会阻塞
    for r in rs:
        if r is s: #如果是新的服务器,那么就进行监听
            c, addr = s.accept()
            print('Got connection from ', addr)
            inputs.append(r) #将新连接过来的client放入输出队列
        else: #如果client端准备就绪,则尝试读取数据
            try:
                data = r.receive(1024)
                disconnected = not data
            except socket.error:
                disconnected = True
            if disconnected:
                print(r.getpeername(), ' disconnected')
                inputs.remove(r)
            else:
                print(data)