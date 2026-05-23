"""
To-Do List Application
----------------------
A simple command-line To-Do List app built with Python.

Features:
- Add tasks
- View tasks
- Delete tasks
- Input validation
- Error handling using try, except, else, and finally
"""

# List used to store tasks
tasks = []


def display_menu():
    """Display the main menu options."""
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Quit")


def add_task():
    """Add a new task to the list."""
    try:
        task = input("Enter a new task: ").strip()

        if not task:
            raise ValueError("Task cannot be empty.")

    except ValueError as error:
        print(f"Error: {error}")

    else:
        tasks.append(task)
        print(f'Task "{task}" added successfully!')

    finally:
        print("Returning to main menu...")


def view_tasks():
    """Display all tasks in the list."""
    try:
        if len(tasks) == 0:
            raise IndexError("There are no tasks to view.")

    except IndexError as error:
        print(f"Error: {error}")

    else:
        print("\n===== YOUR TASKS =====")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

    finally:
        print("Finished viewing tasks.")


def delete_task():
    """Delete a task from the list."""
    try:
        if len(tasks) == 0:
            raise IndexError("There are no tasks to delete.")

        view_tasks()

        task_number = int(input("Enter the task number to delete: "))

        if task_number < 1 or task_number > len(tasks):
            raise ValueError("Task number does not exist.")

    except ValueError as error:
        print(f"Error: {error}")

    except IndexError as error:
        print(f"Error: {error}")

    else:
        removed_task = tasks.pop(task_number - 1)
        print(f'Task "{removed_task}" deleted successfully!')

    finally:
        print("Returning to main menu...")


def main():
    """Main program loop."""
    print("Welcome to the To-Do List Application!")

    while True:
        display_menu()

        try:
            choice = input("Select an option (1-4): ").strip()

            if choice not in ["1", "2", "3", "4"]:
                raise ValueError("Invalid menu option selected.")

        except ValueError as error:
            print(f"Error: {error}")

        else:
            if choice == "1":
                add_task()

            elif choice == "2":
                view_tasks()

            elif choice == "3":
                delete_task()

            elif choice == "4":
                print("Thank you for using the To-Do List App. Goodbye!")
                break

        finally:
            print("-" * 35)


# Run the program
main()