class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
        else:
            print("Invalid index")

    def update_task(self, index, new_task):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["task"] = new_task
        else:
            print("Invalid index")

    def mark_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
        else:
            print("Invalid index")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            for i, task in enumerate(self.tasks):
                status = "Completed" if task["completed"] else "Not Completed"
                print(f"{i}: {task['task']} [{status}]")

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Update Task")
        print("4. Mark Task as Completed")
        print("5. Display Tasks")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input, please enter a number between 1 and 6.")
            continue

        if choice == 1:
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == 2:
            try:
                index == int(input("Enter the index of the task to remove: "))
                todo_list.remove_task(index)
            except ValueError:
                print("Invalid input, please enter a valid index.")
        elif choice == 3:
            try:
                index = int(input("Enter the index of the task to update: "))
                new_task = input("Enter the new task: ")
                todo_list.update_task(index, new_task)
            except ValueError:
                print("Invalid input, please enter a valid index.")
        elif choice == 4:
            try:
                index = int(input("Enter the index of the task to mark as completed: "))
                todo_list.mark_completed(index)
            except ValueError:
                print("Invalid input, please enter a valid index.")
        elif choice == 5:
            todo_list.display_tasks()
        elif choice == 6:
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
