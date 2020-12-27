with open("text.txt") as data:
    res = 0
    for row in data:
        res += row.count("A")
    print(res)