class Todo:
    def __init__(self):
        # This will store our tasks
        self.tasks = []

    def create_task(self, task_name):
        """Creates a new task and adds it to the list."""
        self.tasks.append(task_name)
        print(f"Task '{task_name}' has been created.")

    def update_task(self, old_task_name, new_task_name):
        """Updates an existing task."""
        if old_task_name in self.tasks:
            index = self.tasks.index(old_task_name)
            self.tasks[index] = new_task_name
            print(f"Task '{old_task_name}' has been updated to '{new_task_name}'.")
        else:
            print(f"Task '{old_task_name}' not found.")

    def delete_task(self, task_name):
        """Deletes a task from the list."""
        if task_name in self.tasks:
            self.tasks.remove(task_name)
            print(f"Task '{task_name}' has been deleted.")
        else:
            print(f"Task '{task_name}' not found.")

    def display_tasks(self):
        """Displays all tasks."""
        if self.tasks:
            print("Todo List:")
            for index, task in enumerate(self.tasks, 1):
                print(f"{index}. {task}")
        else:
            print("No tasks in the Todo List.")

# Example usage:
todo_list = Todo()

# Create tasks
todo_list.create_task("Finish homework")
todo_list.create_task("Buy groceries")
todo_list.create_task("Read a book")

# Display tasks
todo_list.display_tasks()

# Update a task
todo_list.update_task("Buy groceries", "Buy groceries and cook dinner")

# Display tasks after update
todo_list.display_tasks()

# Delete a task
todo_list.delete_task("Read a book")

# Display tasks after deletion
todo_list.display_tasks()
