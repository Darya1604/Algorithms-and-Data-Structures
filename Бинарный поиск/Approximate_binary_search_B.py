N, K = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def approximate_binary_search(arr,x):
    l = 0
    r = len(arr) - 1
    while l <= r:
        m = (l + r) // 2
        if arr[m] == x:
            return x
        elif arr[m] < x:
            l = m + 1
        else:
            r = m - 1
    if r == -1 and l == 0:
        return arr[l]
    if l == len(arr) and r == len(arr) - 1:
        return arr[r]
    if abs(arr[r]-x) > abs(arr[l]-x):
        return arr[l]
    else:
        return arr[r]

for i in range(K):
    x = b[i]
    print(approximate_binary_search(a, x))