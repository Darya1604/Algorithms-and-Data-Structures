class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return "error"
        return self.items.pop()

    def front(self):
        if self.is_empty():
            return "error"
        return self.items[-1]

    def size(self):
        return len(self.items)

    def clear(self):
        self.items = []

class Queue:
    def __init__(self):
        self.left = Stack()
        self.right = Stack()

    def is_empty(self):
        return self.left.is_empty() and self.right.is_empty()

    def push(self, item):
        self.left.push(item)

    def pop(self):
        if self.is_empty():
            return "error"
        if self.right.is_empty():
            while not self.left.is_empty():
                self.right.push(self.left.pop())
        return self.right.pop()

    def front(self):
        if self.is_empty():
            return "error"
        if self.right.is_empty():
            while not self.left.is_empty():
                self.right.push(self.left.pop())
        return self.right.front()

    def size(self):
        return self.left.size() + self.right.size()

    def clear(self):
        self.left.clear()
        self.right.clear()

q = Queue()

command = input().split()
while command[0] != "exit":

    if command[0] == "push":
        q.push(int(command[1]))
        print("ok")

    elif command[0] == "pop":
        print(q.pop())

    elif command[0] == "front":
        print(q.front())

    elif command[0] == "size":
        print(q.size())

    elif command[0] == "clear":
        q.clear()
        print("ok")

    command = input().split()

print("bye")
