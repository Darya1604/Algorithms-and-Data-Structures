class Max_Heap:
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def shift_up(self, i): #просеивание вверх
        while i // 2 > 0 and self.heap[i] > self.heap[i // 2]:
            self.heap[i], self.heap[i // 2] = self.heap[ i // 2], self.heap[i]
            i = i // 2

    def insert(self, x):
        self.heap.append(x)
        self.size += 1
        self.shift_up(self.size)

    def shift_down(self, i): #просеивание вниз
        while i * 2 <= self.size:
            j = self.index_max_child(i)
            if self.heap[i] < self.heap[j]:
                self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
            i = j

    def index_max_child(self, i):
        if i * 2 + 1 > self.size:
            return i * 2
        if self.heap[i * 2] > self.heap[i * 2 + 1]:
            return i * 2
        return i * 2 + 1

    def extract(self):
        if self.size == 0:
            return None
        removed = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.shift_down(1)
        return removed

    def get_max(self):
        if self.size == 0:
            return None
        return self.heap[1]

n = int(input())
heap = Max_Heap()

for _ in range(n):
    command = input().split()
    if command[0] == "0":
        heap.insert(int(command[1]))
    elif command[0] == "1":
        print(heap.extract())