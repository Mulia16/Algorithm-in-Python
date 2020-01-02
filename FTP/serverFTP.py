from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer()
authorizer.add_user("Mulia", "12345", "/data/ftp", perm="elradfmwMT", msg_login="Welcome Mulia", msg_quit="Bye Mulia")

handler = FTPHandler
handler.banner = "berhasil terhubung ke server"
handler.authorizer = authorizer

server = FTPServer(("127.0.0.1", 2019), handler)    
server.serve_forever()