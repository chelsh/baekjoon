import sys

N = int(sys.stdin.readline())
L = [n for n in sys.stdin.readline().split()]
a, s, m, d = [int(n) for n in sys.stdin.readline().split()]

operator = ['+'] * a + ['-'] * s + ['*'] * m + ['//'] * d

