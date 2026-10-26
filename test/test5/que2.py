n = int(input())
L = list(map(int, input().split()))

for i in L:
    if L.count(i) % 2 != 0:
        print(i)
        break

