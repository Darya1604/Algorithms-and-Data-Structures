import heapq

n = int(input())
heap = list(map(int, input().split()))

heapq.heapify(heap)

cost = 0

while len(heap) > 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)

    summa = a + b
    cost += summa

    heapq.heappush(heap, summa)

print(f"{cost * 0.05:.2f}")