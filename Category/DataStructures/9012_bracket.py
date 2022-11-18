class Stack:
    def __init__(self, size):
        self.top = -1
        self.size = size
        self.stack = []
    def is_empty(self):
        return self.top == -1
    def is_full(self):
        return self.top == self.size - 1
    def push(self, item):
        if not self.is_full():
            self.stack.append(item)
            self.top += 1
        else:
            print("OverFlow Error")
    def pop(self):
        if not self.is_empty():
            self.top -= 1
            return self.stack.pop()
        else:
            print("UnderFlow Error")
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
    def display(self):
        return self.stack
  

def is_VPS(ps):
    s = Stack(len(ps))
    for i in range(len(ps)):
        if ps[i] == '(':
            s.push(ps[i])
        elif ps[i] == ')':
            if s.is_empty():
                print("NO")
                break
            else:
                s.pop()
    else:
        if s.is_empty():
            print("YES")
        else:
            print("NO")


T = int(input())
for _ in range(T):
    ps = input()
    is_VPS(ps)