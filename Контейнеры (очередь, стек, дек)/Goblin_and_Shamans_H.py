import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

left = deque()
right = deque()

for _ in range(n):
    command = input().split()

    if command[0] == '+':
        right.append(int(command[1]))
    elif command[0] == '*':
        right.appendleft(int(command[1]))
    elif command[0] == '-':
        print(left.popleft())

    if len(left) < len(right):
        left.append(right.popleft())
    elif len(left) > len(right) + 1:
        right.appendleft(left.pop())