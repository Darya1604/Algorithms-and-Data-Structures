import heapq

n = int(input())

cargo = []

for _ in range(n):
    arrival, processing = map(int, input().split())
    cargo.append((arrival, processing))

cargo.sort()
heap = []
for arrival, processing in cargo:
    if heap and heap[0] <= arrival:
        heapq.heapreplace(heap, arrival + processing)
    else:
        heapq.heappush(heap, arrival + processing)

print(len(heap))