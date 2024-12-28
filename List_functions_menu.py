my_list = []

def append_to_list():
    element = input("Enter the element to append: ")
    my_list.append(element)
    print(f"{element} added to the list.")

def sequential_search():
    element = input("Enter the element to search for: ")
    for i in range(len(my_list)):
        if my_list[i] == element:
            print(f"Element '{element}' found at index {i}.")
            return
    print(f"Element '{element}' not found.")

while True:
    print("\n1. Append to List")
    print("2. Search in List")
    print("3. Display List")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        append_to_list()
    elif choice == "2":
        sequential_search()
    elif choice == "3":
        print("Current List:", my_list)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
