tasks = []
def show_menu():
    print("\n====== To Do List ======")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Enter your choice:")

    if choice =="5":
        print("Goddbye!")
        break
    elif choice == "1":
        task = input("Enter task: ")
        tasks.append({"task": task, "done": False})
        print("Task added!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks yet!")
        else:
            print("\nYour Tasks:")
            for i, t in enumerate(tasks):
                status = "✓" if t["done"] else "✗"
                print(f"{i+1}. [{status}] {t['task']}")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks yet!")
        else:
            show_menu_flag = input("Enter task number to mark as done: ")
            index = int(show_menu_flag) - 1
            tasks[index]["done"] = True
            print("Task marked as done!")

    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks yet!")
        else:
            num = input("Enter task number to delete: ")
            index = int(num) - 1
            removed = tasks.pop(index)
            print(f"Deleted: {removed['task']}")