books=[]

while True:
    print("----K.P.P.R. Library----")
    print("6,New Katra Road, Prayagraj")
    print("Library Timimg: 7AM-7PM")
    print("fees:500.00")
    print("\n----Libraru Menu----")
    print("\n1.Add Book")
    print("2.View Book")
    print("3.Search Book")
    print("4.Exit")

    choice = input("Enter your choice:")
    
    if choice== "1":
        name = input("Enter book name:")
        books.append(name)
        print("Book add successfully!")

    elif choice == "2":
        if len(books) == 0:
          print(" No Books Available:")
        else:
           print("Available Books:")
           for book in books:
              print(book)
    elif choice == "3":
        name =input("Enter book name to search:")

        if name in books:
          print("Book found")
        else:
         print("Book not found.")

    elif choice == "4":
       print("Thank-You!")

    else:
       print("Invalid choice!")