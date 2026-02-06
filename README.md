# 📝 Mini Task Manager v3

A modern desktop task manager built with Python and CustomTkinter. Manage your tasks efficiently with tags/categories, search, and a light/dark mode toggle. Perfect for personal productivity or showcasing Python GUI skills in your portfolio.

## 🚀 Features:
Add, Complete, Delete Tasks
Search Tasks: Filter tasks by keywords in real-time.
Tags / Categories: Assign multiple tags to each task (e.g., Work, Personal, Urgent).
Filter by Tags: Show tasks belonging to a specific tag or “All”.
Light/Dark Mode: Toggle between themes for a modern look and feel.
Persistent Storage: Tasks are saved in a JSON file and restored on app launch.
Interactive GUI: Clean, scrollable interface with intuitive buttons and task selection.

## 📂 JSON Task Structure
[
  {
    "text": "Finish portfolio update",
    "done": false,
    "tags": ["Work", "Urgent"]
  },
  {
    "text": "Buy groceries",
    "done": false,
    "tags": ["Personal"]
  }
]

## 💻 Technologies Used:
Python 3.14+
CustomTkinter: Modern GUI framework for Python
JSON: Persistent storage for tasks
Optional: GitHub for version control and portfolio showcase

## ⚙️ Installation
Clone the repository
git clone https://github.com/lmakweya9/mini-task-manager.git
cd mini-task-manager

### Install dependencies
pip install customtkinter
⚠️ Make sure your Python version is 3.10+ for CustomTkinter compatibility.

### Run the app
python main.py

## 🏷 Usage
Add a Task: Enter task text and optional comma-separated tags, then press Enter or click “Add”.
Complete a Task: Select a task and click “✔ Complete”.
Delete a Task: Select a task and click “🗑 Delete”.
Search Tasks: Type keywords in the search bar to filter tasks in real-time.
Filter by Tags: Use the dropdown to show tasks of a specific tag.
Toggle Theme: Click the 🌙 / 🌞 button to switch between dark and light mode.

## 📸 Screenshots
Light Mode	Dark Mode
	
## 🏗 Project Structure
mini-task-manager/
├─ main.py
├─ tasks.json
├─ README.md
├─ requirements.txt
├─ screenshots/
│  ├─ mark-as-done-screen.png
│  ├─ main-screen.png
│  └─ light-mode.png
│  └─ delete-task-screen.png
│  └─ dark-mode.png
│  └─ add-task-screen.png

🔗 Links

GitHub Repository

Portfolio Project Page

✨ Future Enhancements

Clickable tags for quick filtering

Task prioritization / deadlines

Drag & drop task reordering

Export tasks to CSV or PDF