library_inventory = ['How to Win Friends and Influence People', 'Keys to Higher Consciousness', 'The Law of Success']
user_selection = ""

print(f"""
Welcome to The Library of Higher Consciousness!

""")

print("What would you like to do today?")
user_selection = input("""
1 - See a list of books
2 - Donate a book 
3 - Exit

""")

print()
if user_selection == "1":
    for book in library_inventory:
        print(book)
    print()
elif user_selection == "2":
    book_donation = input("Thanks for your generosity. Which book are you donating to the library? \n")
    library_inventory.append(book_donation)
    print(f"\nExcellent! The library now contains the following selections:\n")
    for book in library_inventory:
        print(book)
    print()
elif user_selection == "3":
    print("Thank you for coming to the Library of Higher Consciousness!")
