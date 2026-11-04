import heapq

n = int(input())

heap = []

for i in range(n):
    population = int(input())
    time = max(1, 1000 - population)
    heapq.heappush(heap, (time, i, population))

current_time = 0
current_aquarium = 0

while heap:
    time, aquarium, population = heapq.heappop(heap)

    distance = abs(aquarium - current_aquarium)

    if current_time + distance > time:
        print(time)
        break

    current_time = time
    current_aquarium = aquarium

    population += 1
    next_time = max(1, 1000 - population)

    heapq.heappush(heap, (time + next_time, aquarium, population))