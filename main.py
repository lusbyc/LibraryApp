library_inventory = ['How to Win Friends and Influence People', 'Keys to Higher Consciousness', 'The Laws of Success']
user_selection = ""

print(f"""
Welcome to The Library of Higher Consciousness!
""")

while user_selection != "3":
    print("What would you like to do today?")
    user_selection = input("""
    1 - See Library Inventory
    2 - Donate a Book 
    3 - Exit
    
    """)

    print()
    if user_selection == "1":
        for book in library_inventory:
            print(book)
        print("\n\nWhich book would you like to read?\n")
        book_selection = int(input("""
    [1] How to Win Friends and Influence People
    [2] Keys to Higher Consciousness
    [3] The Laws of Success
    
    """))    
        print("\nYou've selected " + library_inventory[(book_selection)-1]+ "\n\n")
        library_inventory.pop(book_selection-1)

    elif user_selection == "2":
        book_donation = input("Thanks for your generosity. Which book are you donating to the library? \n")
        library_inventory.append(book_donation)
        print(f"\nExcellent! The library now contains the following selections:\n")
        for book in library_inventory:
            print(book)
        print()
    elif user_selection == "3":
        print("Thank you for visiting the Library of Higher Consciousness!")
