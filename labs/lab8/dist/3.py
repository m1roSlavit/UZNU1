def get_rec_val(i):
    if i == 0:
        return 0
    if i == 1 or i == 2:
        return 9
    return get_rec_val(i-1) + 4*get_rec_val(i-3)


print(get_rec_val(10))
