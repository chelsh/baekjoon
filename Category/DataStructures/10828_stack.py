import sys

class Stack:
    def __init__(self):
        self.stack = [None] * 10000
        self.top = -1
    def push(self, X):
        self.top += 1
        self.stack[self.top] = X
    def pop(self):
        if self.empty():
            return -1
        else:
            temp = self.stack[self.top]
            self.stack[self.top] = None
            self.top -= 1
            return temp
    def size(self):
        return self.top + 1
    def empty(self):
        if self.top == -1:
            return 1
        else:
            return 0
    def Top(self):
        if self.empty():
            return -1
        else:
            return self.stack[self.top]
            
N = int(sys.stdin.readline())
s = Stack()
for _ in range(N):
    command = sys.stdin.readline().rstrip()
    if command[:4] == "push":
        command = command.split()
        s.push(int(command[-1]))
    elif command == "pop":
        print(s.pop())
    elif command == "size":
        print(s.size())
    elif command == "empty":
        print(s.empty())
    elif command == "top":
        print(s.Top())