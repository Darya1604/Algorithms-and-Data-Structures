from math import sqrt
C = float(input())
def finding_x(C):
    l = 0
    r = sqrt(C)
    while r - l > 10**(-6):
        m = (l+r) / 2
        if m**2 + sqrt(m) < C:
            l = m
        elif m**2 + sqrt(m) >= C:
            r = m
    x = (r + l) / 2
    return x

x = finding_x(C)
print(f'{x:.6f}')