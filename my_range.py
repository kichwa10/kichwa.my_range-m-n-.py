list = []

m, n = 10, 21
while m < n:

    list.extend(range(m, n, 1))
    print(list)
    list += 1
