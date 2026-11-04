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

    def back(self):
        if self.is_empty():
            return "error"
        return self.items[-1]

    def size(self):
        return len(self.items)

    def clear(self):
        self.items = []

s = Stack()

command = input().split()
while command[0] != "exit":

    if command[0] == "push":
        s.push(int(command[1]))
        print("ok")

    elif command[0] == "pop":
        print(s.pop())

    elif command[0] == "back":
        print(s.back())

    elif command[0] == "size":
        print(s.size())

    elif command[0] == "clear":
        s.clear()
        print("ok")

    command = input().split()

print("bye")