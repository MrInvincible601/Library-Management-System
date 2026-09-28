library = []

def add_book():
    title = input("book title: ")
    author = input("author: ")
    library.append([title, author, "available"])
    print("book added successfully.")

def search_book():
    query = input("enter keyword to search: ").lower()
    matches = 0
    for book in library:
        title, author, status = book
        if query in title.lower() or query in author.lower():
            print("Found:", title, "by", author, "(Status:", status + ")")
            matches += 1
    if matches == 0:
        print("no books found matching that term.")

def issue_book():
    target = input("exact title to issue: ").lower()
    for book in library:
        if book[0].lower() == target:
            if book[2] == "issued":
                print("already issued out.")
            else:
                book[2] = "issued"
                print("issued successfully.")
            return
    print("could not find that title in the system.")

def return_book():
    target = input("exact title to return: ").lower()
    for book in library:
        if book[0].lower() == target:
            if book[2] == "available":
                print("that book was not issued.")
            else:
                book[2] = "available"
                print("book returned.")
            return
    print("title not found.")

def menu():
    while True:
        print("\n--- LIBRARY MENU ---")
        print("1. Add Book\n2. Search\n3. Issue\n4. Return\n5. Exit")
        option = input("select choice (1-5): ")

        if option == "1":
            add_book()
        elif option == "2":
            search_book()
        elif option == "3":
            issue_book()
        elif option == "4":
            return_book()
        elif option == "5":
            print("closing program.")
            break
        else:
            print("invalid selection.")

menu()
