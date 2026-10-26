L = [1, 2, 3, 2, 1, 4, 2, 3, 1]

D = {}

for i in L:
    if i in D:
        D[i] = D[i] + 1
    else:
        D[i] = 1

print(D)

