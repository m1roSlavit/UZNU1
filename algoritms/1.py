for num in range(100, 1000):
    num_p = list(map(int, list(str(num))))
    if (num_p[0]**3 + num_p[1]**3 + num_p[2]**3 == num):
        print(num)