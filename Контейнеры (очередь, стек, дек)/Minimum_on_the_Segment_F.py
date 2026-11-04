class MinStack:
    def __init__(self):
        self.values = []
        self.mins = []

    def push(self, item):
        self.values.append(item)

        if not self.mins:
            self.mins.append(item)
        else:
            self.mins.append(min(item, self.mins[-1]))

    def pop(self):
        self.mins.pop()
        return self.values.pop()

    def get_min(self):
        return self.mins[-1]


class MinQueue:
    def __init__(self):
        self.left = MinStack()
        self.right = MinStack()

    def push(self, item):
        self.right.push(item)

    def pop(self):
        if not self.left.values:
            while self.right.values:
                self.left.push(self.right.pop())

        return self.left.pop()

    def get_min(self):
        if not self.left.values:
            return self.right.get_min()

        if not self.right.values:
            return self.left.get_min()

        return min(self.left.get_min(), self.right.get_min())


n, k = map(int, input().split())
a = list(map(int, input().split()))

q = MinQueue()

for i in range(k):
    q.push(a[i])

print(q.get_min())

for i in range(k, n):
    q.pop()
    q.push(a[i])
    print(q.get_min())