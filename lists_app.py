print("\nWelcome to your Lists")
print("Select a function")

def display():
    print("\n1. Create List")
    print("2. Add items/tasks to list")
    print("3. View list")
    print("4. Delete items/tasks in list")
    print("5. Exit \n")

def create():
    ls_name = input("List Name: ")

    with open(ls_name + '.txt', 'w') as f:
        f.write("") 

def add():
    add_to = input("Enter the list name you want to add items/tasks: ")
    
    while True:
        print('\nEnter "-" to exit out of add function')
        task_name = input("Item/Task Name: ")

        with open(add_to + '.txt', 'a') as f: 
            f.write("- " + task_name + "\n")
        
        if task_name == "-":
            break

    with open(add_to + '.txt', "r+") as fp:
        lines = fp.readlines()
        fp.seek(0)
        fp.truncate()
        fp.writelines(lines[:-1])

def view():
    viewing = input("Enter the name of the list you want to view: ")
    with open(viewing + '.txt', 'r') as f:
        contents = f.read()
        print(contents)

def delete():
    list_name =input("Enter the name of the list you want to delete items/tasks from: ")


    with open(list_name + '.txt', "r+") as fp:
        lines = fp.readlines()
        fp.seek(0)
        fp.truncate()
        # fp.writelines(lines[:-1])
        item_num = int(input("Enter the line number of the item you want to delete: "))
        item_num -= 1
        for number, line in enumerate(lines):
            if number not in [item_num]:
                fp.write(line)

while True:
    display()

    choice = input("Enter your choice: ")
    print("")

    if choice == "1":
        create()
    elif choice == "2":
        add()
    elif choice == "3":
        view()
    elif choice == "4":
        delete()
    elif choice == "5":
        break
    else:
        print("Invalid choice \n")
        continue
