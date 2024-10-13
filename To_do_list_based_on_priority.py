# To-Do List Application with Priority

# Initialize an empty list to store tasks
tasks = []
def add_task(task, priority):
    tasks.append({"task": task, "priority": priority})
    print(f"Task '{task}' with {priority} priority added successfully!")
def view_tasks(sort_by_priority=False):
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("Your To-Do List:")
        sorted_tasks = sorted(tasks, key=lambda x: ["Low", "Medium", "High"].index(x["priority"]), reverse=True) if sort_by_priority else tasks
        for index, task in enumerate(sorted_tasks, start=1):
            print(f"{index}. [{task['priority']}] {task['task']}")
def remove_task(index):
    if 1 <= index <= len(tasks):
        removed_task = tasks.pop(index - 1)
        print(f"Task '{removed_task['task']}' removed successfully!")
    else:
        print("Invalid task number.")
def main():
    try:
        while True:
            print("\n-----------Welcome to task management system-------------")
            print("\n--- To-Do List Menu ---")
            print("1. Add a task")
            print("2. View tasks")
            print("3. View tasks sorted by priority")
            print("4. Remove a task")
            print("5. Quit")
        
            choice = input("Enter your choice (1-5): ")
        
            if choice == '1':
                task = input("Enter the task: ")
                while True:
                    priority = input("Enter priority (High/Medium/Low): ").capitalize()
                    if priority in ["High", "Medium", "Low"]:
                        break
                    print("Invalid priority. Please enter High, Medium, or Low.")
                add_task(task, priority)
            elif choice == '2':
                view_tasks()
            elif choice == '3':
                view_tasks(sort_by_priority=True)
            elif choice == '4':
                view_tasks()
                if tasks:
                    index = int(input("Enter the number of the task to remove: "))
                    remove_task(index)
            elif choice == '5':
                print("Thank you for using the To-Do List application. Have a good day!!!")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 5.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    except IndexError:
        print("Invalid task number. Please choose a number from the list.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()