# 🧾 To-Do List (Python)

A simple command-line To-Do List Application built with Python.  
This app allows you to add tasks, list them, mark tasks as completed, and delete them.
The tasks are stored in a JSON file so the data remains even after closing the app.

---

## 🚀 Features

✔ Add a new task  
✔ View all tasks  
✔ Mark a task as complete  
✔ Delete a task  
✔ Persistent storage using JSON  
✔ Beginner-friendly and modular file structure

---

## 📦 Project Structure

todo_app/
│
├─ data/
│ └─ tasks.json # Stored tasks
│
├─ utils/
│ ├─ file_manager.py # Read/Write JSON file
│ └─ validator.py # Validate input
│
├─ todo.py # Core functions (CRUD)
└─ main.py # Command Line Interface
