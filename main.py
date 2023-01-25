tasks = []

while True:
  try: 
    print(f"Enter one of the following commands: add, view, delete, clear or quit. (Currently {len(tasks)} tasks).")
    command = input()
    if command == "add":
        task = input("Enter a task to add: ")
        tasks.append(task)
        print(f"Task '{task}' added.")
    elif command == "view":
            if len(tasks) == 0:
                print("No task to display.")
            else:
                print("Here are the tasks in your list: ")
                for i, task in enumerate(tasks):
                    print(f"{i+1}. {task}")
    elif command == "delete":
            if len(tasks) == 0:
                print("No task to delete.")
            else:
                print("What would you like to delete?")
                delete = input()
                if delete in tasks:
                    tasks.remove(delete)
                    print(f"The following task was deleted: {delete}")
                else:
                    print(f"{delete} is not in the list.")
    elif command == "clear":
        tasks.clear()
        print("All tasks have been cleared.")
    elif command == "quit": 
        break
    else: 
        print("Invalid input")
  except: 
    print("There is an unexpected error")
    break 
