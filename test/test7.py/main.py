from book import Book

books = {}

while True:
    print("\n----- BOOK MENU -----")
    print("1. Add Book")
    print("2. Delete Book")
    print("3. Display All Books")
    print("4. Search Book")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        bid = int(input("Enter Book ID: "))

        if bid in books:
            print("Book ID already exists!")

        else:
            name = input("Enter Book Name: ")
            price = float(input("Enter Book Price: "))
            author = input("Enter Author Name: ")

            b = Book(bid, name, price, author)
            books[bid] = b

            print("Book Added Successfully!")

    elif choice == 2:
        bid = int(input("Enter Book ID to delete: "))

        if bid in books:
            del books[bid]
            print("Book Deleted Successfully!")

        else:
            print("Book Not Found!")

    elif choice == 3:
        if len(books) == 0:
            print("No Books Available!")

        else:
            for b in books.values():
                b.display()
                print("------------------")

    elif choice == 4:
        bid = int(input("Enter Book ID to search: "))

        if bid in books:
            books[bid].display()

        else:
            print("Book Not Found!")

    elif choice == 5:
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")

        