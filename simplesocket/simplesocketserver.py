from socketserver import TCPServer, StreamRequestHandler
import socket

class Handler(StreamRequestHandler):
    def handle(self):
        addr = self.request.getpeername()
        print('Got connection from', addr)
        self.wfile.write('Thank you for connecting'.encode())

server = TCPServer((socket.gethostname(),1234), Handler)
server.serve_forever()