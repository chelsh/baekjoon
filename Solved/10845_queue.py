import sys

class Queue:
    def __init__(self):
        self.data = []
        self.front = -1
        self.back = -1
    def push(self, n):
        self.data.append(n)
        self.back += 1
    def pop(self):
        if self.empty():
            return -1
        else:
            self.front += 1
            return self.data[self.front]
    def size(self):
        return self.back - self.front
    def empty(self):
        if self.size() == 0:
            return 1
        else:
            return 0
    def Front(self):
        if self.empty():
            return -1
        else:
            return self.data[self.front + 1]
    def Back(self):
        if self.empty():
            return -1
        else:
            return self.data[self.back]

queue = Queue()
N = int(sys.stdin.readline())
for _ in range(N):
    command = sys.stdin.readline().rstrip()
    if command[:4] == "push":
        command = command.split()
        queue.push(int(command[-1]))
    elif command == "pop":
        print(queue.pop())
    elif command == "size":
        print(queue.size())
    elif command == "empty":
        print(queue.empty())
    elif command == "front":
        print(queue.Front())
    elif command == "back":
        print(queue.Back())