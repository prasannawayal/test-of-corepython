
D = [2000, 500, 200, 100, 50, 20, 10, 5]

amount = int(input("Enter amount: "))

for note in D:
    count = amount // note

    if count > 0:
        print(note, ":", count)
        amount = amount % note

