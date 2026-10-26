L1 = [1, 2, 3, 4, 5]
L2 = [3, 4, 5, 6, 7]

L3 = []

for i in L1:
    if i not in L3:
        L3.append(i)

for i in L2:
    if i not in L3:
        L3.append(i)

print("Union:", L3)