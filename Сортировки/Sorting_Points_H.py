class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance_squared(point):
    return point.x ** 2 + point.y ** 2

def Merge_Sort(arr):
    if len(arr) <= 1:
        return arr
    ind = len(arr) // 2
    left = Merge_Sort(arr[:ind])
    right = Merge_Sort(arr[ind:])
    res = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if distance_squared(left[i]) < distance_squared(right[j]):
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res.extend(left[i:])
    res.extend(right[j:])
    return res

n = int(input())
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append(Point(x, y))
points = Merge_Sort(points)
for point in points:
    print(point.x, point.y)