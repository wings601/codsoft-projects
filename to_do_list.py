def task():
    tasks = []  # Empty list
    print("Welcome to the to-do list") #here we welcome the user 

    total_task = int(input("Enter the number of tasks you want to add: "))#here user give the total number of taks they want
    for i in range(1, total_task + 1):
        task_name = input(f"Enter the task {i}: ")
        tasks.append(task_name)#here the taks add to to empty list 

    # All tasks are now saved
    print("Today's total tasks:")
    for task in tasks:
        print(task)

    while True:
        operation = int(input("\nEnter 1 to ADD\n2 to UPDATE\n3 to DELETE\n4 to VIEW\n5 to EXIT: ")) # here perform the operation on the tasks
        
        if operation == 1:
            add = input("Enter the task you want to add: ")
            tasks.append(add)
            print(f"Task '{add}' has been successfully added.")
        
        elif operation == 2:
            update_val = input("Enter the name of the task to update: ")
            if update_val in tasks:
                up = input("Enter the new task: ")
                ind = tasks.index(update_val)  # Find index of the task
                tasks[ind] = up  # Update the task
                print(f"Task '{update_val}' has been updated to '{up}'.")
            else:
                print(f"Task '{update_val}' not found.")
        
        elif operation == 3:
            delete_val = input("Enter the name of the task to delete: ")
            if delete_val in tasks:
                tasks.remove(delete_val)
                print(f"Task '{delete_val}' has been deleted.")
            else:
                print(f"Task '{delete_val}' not found.")
        
        elif operation == 4:
            print("Current tasks:")
            for task in tasks:
                print(task)
        
        elif operation == 5:
            print("Exiting the to-do list.")
            break
        
        else:
            print("Invalid operation, please try again.")
