def add_task(tasks):
    task = input("Enter a task: ")
    tasks.append(task)
    print(f"Task added: {task}")

def display_tasks(tasks):
    if tasks:
        print("Here are your tasks:")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")
    else:
        print("No tasks found.")

def delete_task(tasks):
    display_tasks(tasks)
    task_number = int(input("Enter task number to delete: ")) - 1
    if 0 <= task_number < len(tasks):
        removed_task = tasks.pop(task_number)
        print(f"Task deleted: {removed_task}")
    else:
        print("Invalid task number")

def main():
    tasks = []
    while True:
        print("\n1. Add Task")
        print("2. Display Tasks")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            display_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()