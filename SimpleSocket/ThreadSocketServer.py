from socketserver import TCPServer, ThreadingMixIn, StreamRequestHandler
import socket
class Server(ThreadingMixIn, TCPServer):
    pass

class Handler(StreamRequestHandler):
    def handle(self):
        addr = self.request.getpeername()
        print('Got connection from', addr)
        self.wfile.write('Thank you for connecting'.encode())

server = Server((socket.gethostname(), 1234), Handler)
server.serve_forever()