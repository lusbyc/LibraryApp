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
        print("**************************************************************************")
        print(f"There are currently {len(library_inventory)} books available in the library.\n\n")
        for i in range(0,len(library_inventory)):
            print("[" + str(i+1) + "] " + library_inventory[i])
        
        print("**************************************************************************")
        book_selection = int(input("\n\nPlease select the number that corresponds to the book you'd like to read: \n"))

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
