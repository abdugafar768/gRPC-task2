import core_pb2_grpc
import core_pb2
import grpc
import server1


channel = grpc.insecure_channel('127.0.0.1:50051')
stub = core_pb2_grpc.TestServiceStub(channel)

class _Getch:
    """Gets a single character from standard input.  Does not echo to the
screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()


getch = _Getch()

while True:
        
    request = core_pb2.LetterRequest(b = getch())
    response_stream = stub.ServiceOneMethod(request)

    for response in response_stream:
        print(response.a, end='')
