N, K = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def binary_search(arr, x):
    l = 0
    r = len(arr) - 1
    while l <= r:
        m = (l+r) // 2
        if arr[m] == x:
            return True
        elif arr[m] < x:
            l = m + 1
        else:
            r = m - 1
    return False

for i in range(K):
    x = b[i]
    if binary_search(a, x) == True:
        print('YES')
    else:
        print('NO')

