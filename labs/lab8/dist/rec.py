def get_rec(i):
    if i == 0:
        return 7
    if i == 1:
        return 5
    return 2*get_rec(i-1) + 3*get_rec(i-2)

print(get_rec(5))