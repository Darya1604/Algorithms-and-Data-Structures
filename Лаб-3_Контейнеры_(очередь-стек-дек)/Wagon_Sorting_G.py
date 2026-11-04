n = int(input())
wagons = list(map(int, input().split()))
stack = []
need = 1
i = 0
answer = True

while i < n or stack:
    if stack and stack[-1] == need:
        stack.pop()
        need += 1

    elif i < n:
        stack.append(wagons[i])
        i  += 1

    else:
        answer = False
        break

if answer:
    print("YES")
else:
    print("NO")