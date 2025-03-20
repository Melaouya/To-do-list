# To-Do list program 

tasks = []  # List to store tasks

while True:
    # Displaying options
    print("\nChoose an option Bro:")
    print("1. Add a task")
    print("2. Delete a task")
    print("3. View tasks")
    print("4. Exit")

    # Taking user input
    choice = input("Enter your choice Bro: ")

    if choice == "1":
        # Add a task
        task = input("Enter task: ")
        tasks.append(task)  # Adding task to the list
        print(f"Task '{task}' added successfully.")
    
    elif choice == "2":
        # Delete a task
        if not tasks:
            print("Your to-do list is empty Bro. Nothing to delete here.")
        else:
            print("Tasks to delete:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            try:
                task_index = int(input("Enter the task to delete: "))
                if 1 <= task_index <= len(tasks):
                    deleted_task = tasks.pop(task_index - 1)  # Deleting the task by index
                    print(f"Task '{deleted_task}' deleted successfully.")
                else:
                    print("Invalid input Bro.")
            except ValueError:
                print("Invalid input. Please enter a valid task index number.")
    
    elif choice == "3":
        # View all tasks
        if not tasks:
            print("Your to-do list is empty Bro.")
        else:
            print("To-Do List:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
    
    elif choice == "4":
        # Exit the program
        print("Exiting program.")
        break
    
    else:
        print("Invalid choice. Try again Bro.")
