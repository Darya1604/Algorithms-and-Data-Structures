coef = list(map(int, input().split()))
def finding_cube_x(coef):
    a = coef[0]
    b = coef[1]
    c = coef[2]
    d = coef[3]
    l = -3000
    r = 3000
    while r - l > 10**(-4):
        m = (l + r) / 2
        f = a*m**3 + b*m**2 + c*m + d
        if f == 0:
            return m
        if a*f < 0:
            l = m
        else:
            r = m
    x = (r + l) / 2
    return x

x = finding_cube_x(coef)
print(f'{x:.15f}')