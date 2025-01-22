def display_menu():
    print("To-Do List Menu:")
    print("1. View To-Do List")
    print("2. Add To-Do Item")
    print("3. Remove To-Do Item")
    print("4. Exit")

def view_list(todo_list):
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("Your To-Do List:")
        for idx, item in enumerate(todo_list, 1):
            print(f"{idx}. {item}")

def add_item(todo_list):
    item = input("Enter the to-do item: ")
    todo_list.append(item)
    print(f"'{item}' has been added to your to-do list.")

def remove_item(todo_list):
    view_list(todo_list)
    if todo_list:
        try:
            item_number = int(input("Enter the number of the item to remove: "))
            if 1 <= item_number <= len(todo_list):
                removed_item = todo_list.pop(item_number - 1)
                print(f"'{removed_item}' has been removed from your to-do list.")
            else:
                print("Invalid item number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    todo_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            view_list(todo_list)
        elif choice == '2':
            add_item(todo_list)
        elif choice == '3':
            remove_item(todo_list)
        elif choice == '4':
            print("Exiting the to-do list application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()