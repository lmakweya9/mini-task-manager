## Import Libraries (Foundation)
import tkinter as tk
from tkinter import messagebox
import json
import os

class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini Task Manager")
        self.root.geometry("400x500")

        # File where tasks will be saved
        self.file_name = "tasks.json"

        # List to store tasks in memory
        self.tasks = []

        # Build UI
        self.create_widgets()

        # Load saved tasks
        self.load_tasks()

    def create_widgets(self):

        # Input field
        self.task_entry = tk.Entry(self.root, width=30, font=("Arial", 14))
        self.task_entry.pack(pady=10)

        # Add button
        self.add_btn = tk.Button(
            self.root,
            text="Add Task",
            width=20,
            command=self.add_task
        )
        self.add_btn.pack(pady=5)

        # Task list
        self.task_listbox = tk.Listbox(
            self.root,
            width=40,
            height=15,
            font=("Arial", 12)
        )
        self.task_listbox.pack(pady=10)

        # Complete button
        self.complete_btn = tk.Button(
            self.root,
            text="Mark as Done",
            width=20,
            command=self.complete_task
        )
        self.complete_btn.pack(pady=5)

        # Delete button
        self.delete_btn = tk.Button(
            self.root,
            text="Delete Task",
            width=20,
            command=self.delete_task
        )
        self.delete_btn.pack(pady=5)

    def add_task(self):

        task = self.task_entry.get()

        if task == "":
            messagebox.showwarning("Warning", "Task cannot be empty!")
            return

        # Create task object
        task_data = {
            "text": task,
            "done": False
        }

        self.tasks.append(task_data)

        self.update_listbox()
        self.save_tasks()

        self.task_entry.delete(0, tk.END)

    def update_listbox(self):

        self.task_listbox.delete(0, tk.END)

        for task in self.tasks:

            display = task["text"]

            if task["done"]:
                display += " ✅"

            self.task_listbox.insert(tk.END, display)

    def complete_task(self):

        selected = self.task_listbox.curselection()

        if not selected:
            messagebox.showwarning("Warning", "Select a task first!")
            return

        index = selected[0]

        self.tasks[index]["done"] = True

        self.update_listbox()
        self.save_tasks()

    def save_tasks(self):

        with open(self.file_name, "w") as file:
            json.dump(self.tasks, file, indent=4)

    def load_tasks(self):

        if os.path.exists(self.file_name):

            with open(self.file_name, "r") as file:
                self.tasks = json.load(file)

            self.update_listbox()

    def delete_task(self):

        selected = self.task_listbox.curselection()

        if not selected:
            messagebox.showwarning("Warning", "Select a task first!")
            return

        index = selected[0]

        del self.tasks[index]

        self.update_listbox()
        self.save_tasks()

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()
