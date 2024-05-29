inventory = []


def add_item(item):
    inventory.append(item.capitalize())


def view_inventory():
    if inventory:
        item_count = {}
        for item in inventory:
            item_count[item] = item_count.get(item, 0) + 1

        for item, count in item_count.items():
            print(f"{item}: {count}")
    else:
        print("Inventory is empty.")


def remove_item(item):
    item = item.capitalize()
    if item in inventory:
        inventory.remove(item)
        print(f"Item '{item}' removed from inventory.")
    else:
        print(f"Item '{item}' not found in inventory.")


def menu():
    while True:
        print("\nMenu:")
        print("1. Add")
        print("2. View")
        print("3. Remove")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the item to add: ")
            add_item(item)
        elif choice == '2':
            view_inventory()
        elif choice == '3':
            item = input("Enter the item to remove: ")
            remove_item(item)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")


menu()