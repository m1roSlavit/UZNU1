def maxx(a, b, c):
    max_val = a
    if b > max_val:
        max_val = b
    if c > max_val:
        max_val = c
    return max_val

x, y, z = map(float, input("input x y z: ").split(" "))

u = (maxx(x, y, z) + maxx(x + y, x*y, 4*z))/(maxx(maxx(x + y, x*y, x**2)**2, 7, z**2))

print(u)