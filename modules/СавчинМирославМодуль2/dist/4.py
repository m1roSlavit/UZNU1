X = None
Y = None

with open("text.txt") as data:
    for row in data:
        if not X:
            X = row
        else:
            Y = row
            break

print(X,Y)