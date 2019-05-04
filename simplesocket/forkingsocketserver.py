from socketserver import TCPServer, ForkingMixIn, StreamRequestHandler
import socket

class Server(ForkingMixIn, TCPServer):
    pass

class Handler(StreamRequestHandler):
    def handle(self):
        addr = self.request.getpeername()
        print('Got connection from', addr)
        self.wfile.wirte('Thank you for connecting'.encode())

server = Server((socket.gethostname(), 1234), Handler)
server.serve_forever()