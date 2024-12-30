# ✅ CLI To-Do List Manager  

A simple and practical Command-Line Interface (CLI) tool built with Python to manage your daily tasks. It allows you to add, view, mark as complete, and delete tasks directly from the terminal.  

---

## 🎯 Features  
- 📝 Add a new task.  
- 📋 View all tasks with their status.  
- ✅ Mark tasks as completed.  
- 🗑️ Delete tasks from the list.  

---

## 🛠️ Requirements  
- Python 3.6 or later  
- Libraries: None (built using Python’s standard library)  

---

## 🚀 How to Use  

1. Clone the repository:  
   ```bash
   git clone https://github.com/yourusername/todo-cli.git
   cd todo-cli
   ```

2. Run the script:  
   ```bash
   python todo.py <command> [options]
   ```

### Commands  

#### 1. Add a Task  
   Add a new task to the to-do list.  
   ```bash
   python todo.py add "Task description"
   ```
   **Example**:  
   ```bash
   python todo.py add "Buy groceries"
   ```
   **Output**:  
   ```plaintext
   ✅ Task added: 'Buy groceries'
   ```

#### 2. View Tasks  
   Display all tasks with their completion status.  
   ```bash
   python todo.py view
   ```
   **Example Output**:  
   ```plaintext
   📋 To-Do List:
   1. Buy groceries [❌]
   2. Finish project report [❌]
   ```

#### 3. Mark Task as Completed  
   Mark a specific task as completed using its index.  
   ```bash
   python todo.py complete <task_index>
   ```
   **Example**:  
   ```bash
   python todo.py complete 1
   ```
   **Output**:  
   ```plaintext
   ✅ Task 1 marked as completed.
   ```

#### 4. Delete a Task  
   Remove a task from the list using its index.  
   ```bash
   python todo.py delete <task_index>
   ```
   **Example**:  
   ```bash
   python todo.py delete 1
   ```
   **Output**:  
   ```plaintext
   🗑️ Task removed: 'Buy groceries'
   ```

---

## 💾 Data Storage  
The tasks are stored in a `tasks.json` file in the project directory. This ensures task persistence between script executions.

---

## 🛡️ License  
This project is licensed under the **MIT License**.  

---

## 🤝 Contributions  
Contributions are welcome! If you have suggestions or want to improve the tool, feel free to fork the repository and submit a pull request.  

---

## 📬 Contact  
For any queries, reach out to:  
📧 **your-email@example.com**  

---

Enjoy managing your tasks efficiently! 🚀
