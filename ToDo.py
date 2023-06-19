def add_task(task):
    with open("Todo.txt", "a") as file:
        file.write(task + "\n")

def remove_task(task):
    with open("Todo.txt", "r") as file:
        lines = file.readlines()
    with open("Todo.txt", "w") as file:
        for line in lines:
            if line.strip("\n") != task:
                file.write(line)

def view_tasks():
    with open("Todo.txt", "r") as file:
        tasks = file.readlines()
    if tasks:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task.strip()}")
    else:
        print("No tasks found.")

while True:
    print("\n1. Add task\n2. Remove task\n3. View tasks\n4. Exit..")
    choice = input("Enter your choice: ")
    if choice == "1":
        task = input("Enter task: ")
        add_task(task)
        print("Task added.")
    elif choice == "2":
        task = input("Enter task to remove: ")
        remove_task(task)
        print("Task removed.")
    elif choice == "3":
        view_tasks()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")
