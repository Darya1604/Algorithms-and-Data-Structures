import heapq

heap = []

while True:
    try:
        command = input().split()
    except EOFError:
        break

    if command[0] == "CLEAR":
        heap.clear()

    elif command[0] == "ADD":
        n = int(command[1])
        heapq.heappush(heap, -n)

    elif command[0] == "EXTRACT":
        if len(heap) == 0:
            print("CANNOT")
        else:
            print(-heapq.heappop(heap))