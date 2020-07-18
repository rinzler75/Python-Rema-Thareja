class SocketError(RuntimeError):
    def __init__(self, *arg):
        self.args=arg
try:
    raise SocketError('Socket','Establishment','Error')
except SocketError as e:
    print(e.args)