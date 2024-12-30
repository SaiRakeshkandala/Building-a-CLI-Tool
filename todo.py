import argparse
import json
import os

# File to store tasks
TASKS_FILE = "tasks.json"

# Initialize the tasks file if it doesn't exist
if not os.path.exists(TASKS_FILE):
    with open(TASKS_FILE, 'w') as f:
        json.dump([], f)

# Load tasks from file
def load_tasks():
    with open(TASKS_FILE, 'r') as f:
        return json.load(f)

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

# Add a new task
def add_task(description):
    tasks = load_tasks()
    tasks.append({"description": description, "completed": False})
    save_tasks(tasks)
    print(f"✅ Task added: '{description}'")

# View all tasks
def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📋 No tasks available.")
        return
    print("\n📋 To-Do List:")
    for i, task in enumerate(tasks, 1):
        status = "✅" if task["completed"] else "❌"
        print(f"{i}. {task['description']} [{status}]")

# Mark a task as completed
def complete_task(index):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        tasks[index - 1]["completed"] = True
        save_tasks(tasks)
        print(f"✅ Task {index} marked as completed.")
    else:
        print("❌ Invalid task index.")

# Delete a task
def delete_task(index):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        removed_task = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"🗑️ Task removed: '{removed_task['description']}'")
    else:
        print("❌ Invalid task index.")

# Main function to handle CLI arguments
def main():
    parser = argparse.ArgumentParser(description="Simple To-Do List Manager")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Add task command
    parser_add = subparsers.add_parser("add", help="Add a new task")
    parser_add.add_argument("description", type=str, help="Task description")

    # View tasks command
    parser_view = subparsers.add_parser("view", help="View all tasks")

    # Complete task command
    parser_complete = subparsers.add_parser("complete", help="Mark a task as completed")
    parser_complete.add_argument("index", type=int, help="Task index to mark as completed")

    # Delete task command
    parser_delete = subparsers.add_parser("delete", help="Delete a task")
    parser_delete.add_argument("index", type=int, help="Task index to delete")

    # Parse arguments
    args = parser.parse_args()

    # Execute commands
    if args.command == "add":
        add_task(args.description)
    elif args.command == "view":
        view_tasks()
    elif args.command == "complete":
        complete_task(args.index)
    elif args.command == "delete":
        delete_task(args.index)

if __name__ == "__main__":
    main()
