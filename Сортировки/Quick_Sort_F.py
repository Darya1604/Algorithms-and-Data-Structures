from random import randint

def Quick_Sort(arr, left_border, right_border):
    if left_border < right_border:
        val = arr[randint(left_border, right_border)]
        l_ind, r_ind = left_border, right_border
        while l_ind <= r_ind:
            while arr[l_ind] < val:
                l_ind += 1
            while arr[r_ind] > val:
                r_ind -= 1
            if l_ind <= r_ind:
                arr[l_ind], arr[r_ind] = arr[r_ind], arr[l_ind]
                l_ind += 1
                r_ind -= 1
        if left_border < r_ind:
            Quick_Sort(arr, left_border, r_ind)
        if right_border > l_ind:
            Quick_Sort(arr, l_ind, right_border)

n = int(input())
arr = list(map(int, input().split()))
Quick_Sort(arr, 0, n-1)
print(*arr)


