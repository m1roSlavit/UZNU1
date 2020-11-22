arr = [float(x) for x in input("ВВедіть масив елементів через пробіл: ").split(" ")]

for i in range(len(arr)):
    if abs(arr[i]) < 1:
        arr.insert(0, arr.pop(i))

print(arr)