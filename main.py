import todo


def print_menu():
    print("\n=== TO-DO LIST APP ===")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("0. Exit")


def show_tasks():
    tasks = todo.get_tasks()
    if not tasks:
        print("\n📭 No tasks yet. Add some!")
        return

    print("\n--- Your Tasks ---")
    for i, t in enumerate(tasks):
        status = "✓" if t["done"] else "✗"
        print(f"{i}. {t['title']} [{status}]")


def ask_index():
    try:
        return int(input("Enter task number: "))
    except:
        return -1


if __name__ == "__main__":
    while True:
        print_menu()
        choice = input("Choose option: ")

        if choice == "1":
            title = input("Task name: ")
            if todo.add_task(title):
                print("✔ Task added successfully!")
            else:
                print("❌ Task title invalid.")

        elif choice == "2":
            show_tasks()

        elif choice == "3":
            show_tasks()
            index = ask_index()
            if todo.complete_task(index):
                print("✔ Task marked as completed!")
            else:
                print("❌ Invalid index.")

        elif choice == "4":
            show_tasks()
            index = ask_index()
            if todo.delete_task(index):
                print("🗑 Task deleted.")
            else:
                print("❌ Invalid index.")

        elif choice == "0":
            print("👋 Goodbye! Try to be productive.")
            break

        else:
            print("⚠️ Invalid option, try again.")
