import os

FILE_NAME = "tasks.txt"


def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        tasks = file.read().splitlines()

    return tasks


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")


def show_tasks(tasks):
    if len(tasks) == 0:
        print("\nNo tasks found.\n")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        print()


def add_task(tasks):
    task = input("Enter task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!\n")


def delete_task(tasks):
    show_tasks(tasks)

    if len(tasks) == 0:
        return

    try:
        num = int(input("Enter task number to delete: "))
        tasks.pop(num - 1)
        save_tasks(tasks)
        print("Task deleted successfully!\n")
    except (ValueError, IndexError):
        print("Invalid task number.\n")


def main():
    tasks = load_tasks()

    while True:
        print("====== TO-DO LIST ======")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks(tasks)

        elif choice == "2":
            add_task(tasks)

        elif choice == "3":
            delete_task(tasks)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option.\n")


if __name__ == "__main__":
    main()