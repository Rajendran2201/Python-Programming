def moveZeros(a):
    i = 0
    for j in range(len(a)):
        if(a[j] != 0):
            a[i], a[j] = a[j], a[i]
            i += 1

a = [0, 1, 0, 3, 12]
moveZeros(a)
print(a)
