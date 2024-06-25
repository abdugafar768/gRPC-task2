import grpc
import core_pb2_grpc
import core_pb2
import concurrent.futures

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


class TestService(core_pb2_grpc.TestServiceServicer):
    def ServiceOneMethod(self, request_iterator, context):
        while True:
            yield core_pb2.LetterResponse(a=self.check(getch()))

    def check(self, ch):
      
        if ch == '\u0003':
            exit()
        return ch
            

def server():
    server = grpc.server(concurrent.futures.ThreadPoolExecutor(max_workers=10))
    core_pb2_grpc.add_TestServiceServicer_to_server(TestService(), server)
    server.add_insecure_port("127.0.0.1:50051")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    server()