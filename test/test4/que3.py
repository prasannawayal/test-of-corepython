n = 10

# Top row
print("*" * n)

# Diagonal
for i in range(n - 2):
    print(" " * (n - i) + "*")

# Bottom row
print("*" * n)