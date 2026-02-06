import customtkinter as ctk
import json
import os

# ------------------------
# App Settings
# ------------------------
ctk.set_appearance_mode("Dark")  # default
ctk.set_default_color_theme("blue")

FILE = "tasks.json"


class TaskApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Mini Task Manager")
        self.geometry("600x750")
        self.resizable(False, False)

        self.tasks = self.load_tasks()
        self.filtered_tasks = self.tasks.copy()
        self.selected_index = None
        self.all_tags = self.get_all_tags()
        self.current_filter_tag = "All"

        # ------------------------
        # Header
        # ------------------------
        header_frame = ctk.CTkFrame(self, fg_color="transparent")
        header_frame.pack(pady=10, fill="x", padx=10)

        self.title_label = ctk.CTkLabel(header_frame, text="📝 Mini Task Manager", font=("Arial", 26, "bold"))
        self.title_label.pack(side="left", padx=5)

        # Theme toggle button
        self.theme_toggle_btn = ctk.CTkButton(header_frame, text="🌙", width=60, command=self.toggle_theme)
        self.theme_toggle_btn.pack(side="right")

        # ------------------------
        # Search Entry
        # ------------------------
        self.search_entry = ctk.CTkEntry(self, placeholder_text="Search tasks...", width=500, height=35)
        self.search_entry.pack(pady=5)
        self.search_entry.bind("<KeyRelease>", lambda e: self.search_tasks())

        # ------------------------
        # Tag Filter Dropdown
        # ------------------------
        self.tag_filter_var = ctk.StringVar(value="All")
        self.tag_filter_menu = ctk.CTkOptionMenu(self, values=["All"] + self.all_tags, variable=self.tag_filter_var,
                                                 command=lambda v: self.search_tasks())
        self.tag_filter_menu.pack(pady=5)

        # ------------------------
        # Task Entry + Tags
        # ------------------------
        self.task_entry = ctk.CTkEntry(self, placeholder_text="Add a new task...", width=400, height=35)
        self.task_entry.pack(pady=5)
        self.task_entry.bind("<Return>", lambda e: self.add_task())

        self.tags_entry = ctk.CTkEntry(self, placeholder_text="Tags (comma-separated)", width=400, height=35)
        self.tags_entry.pack(pady=5)
        self.tags_entry.bind("<Return>", lambda e: self.add_task())

        # ------------------------
        # Buttons
        # ------------------------
        self.btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.btn_frame.pack(pady=10)

        self.add_btn = ctk.CTkButton(self.btn_frame, text="➕ Add", command=self.add_task, width=120)
        self.add_btn.grid(row=0, column=0, padx=8)

        self.complete_btn = ctk.CTkButton(self.btn_frame, text="✔ Complete", fg_color="#22c55e", command=self.complete_task,
                                          width=120)
        self.complete_btn.grid(row=0, column=1, padx=8)

        self.delete_btn = ctk.CTkButton(self.btn_frame, text="🗑 Delete", fg_color="#ef4444", command=self.delete_task,
                                        width=120)
        self.delete_btn.grid(row=0, column=2, padx=8)

        # ------------------------
        # Task List Area
        # ------------------------
        self.task_frame = ctk.CTkScrollableFrame(self, width=550, height=480, corner_radius=12)
        self.task_frame.pack(pady=10)

        self.refresh()

    # ------------------------
    # Data
    # ------------------------
    def load_tasks(self):
        if not os.path.exists(FILE):
            return []
        with open(FILE, "r") as f:
            return json.load(f)

    def save_tasks(self):
        with open(FILE, "w") as f:
            json.dump(self.tasks, f, indent=4)

    def get_all_tags(self):
        tags = set()
        for task in self.tasks:
            tags.update(task.get("tags", []))
        return sorted(list(tags))

    # ------------------------
    # Task Logic
    # ------------------------
    def add_task(self):
        text = self.task_entry.get().strip()
        tags_text = self.tags_entry.get().strip()
        tags = [t.strip() for t in tags_text.split(",") if t.strip()]

        if not text:
            return

        self.tasks.append({"text": text, "done": False, "tags": tags})
        self.task_entry.delete(0, "end")
        self.tags_entry.delete(0, "end")
        self.save_tasks()

        self.all_tags = self.get_all_tags()
        self.tag_filter_menu.configure(values=["All"] + self.all_tags)

        self.search_tasks()

    def complete_task(self):
        if self.selected_index is None:
            return
        real_index = self.filtered_tasks[self.selected_index]["index"]
        self.tasks[real_index]["done"] = True
        self.save_tasks()
        self.search_tasks()

    def delete_task(self):
        if self.selected_index is None:
            return
        real_index = self.filtered_tasks[self.selected_index]["index"]
        self.tasks.pop(real_index)
        self.selected_index = None
        self.save_tasks()
        self.all_tags = self.get_all_tags()
        self.tag_filter_menu.configure(values=["All"] + self.all_tags)
        self.search_tasks()

    # ------------------------
    # Search + Tag Filter
    # ------------------------
    def search_tasks(self):
        query = self.search_entry.get().lower()
        self.current_filter_tag = self.tag_filter_var.get()
        self.filtered_tasks = []

        for idx, task in enumerate(self.tasks):
            text_match = query in task["text"].lower()
            tag_match = self.current_filter_tag == "All" or self.current_filter_tag in task.get("tags", [])
            if text_match and tag_match:
                self.filtered_tasks.append({"index": idx, **task})

        self.refresh()

    # ------------------------
    # UI Refresh
    # ------------------------
    def refresh(self):
        for widget in self.task_frame.winfo_children():
            widget.destroy()
        self.selected_index = None

        for i, task in enumerate(self.filtered_tasks):
            bg = "#1f2937" if not task["done"] else "#14532d"
            frame = ctk.CTkFrame(self.task_frame, fg_color=bg, corner_radius=12)
            frame.pack(fill="x", pady=6, padx=5)

            label_text = task["text"]
            label = ctk.CTkLabel(frame, text=label_text, anchor="w", font=("Arial", 14))
            label.pack(side="top", padx=15, pady=5, fill="x", expand=True)

            # Tags display
            if task.get("tags"):
                tags_str = ", ".join(task["tags"])
                tags_label = ctk.CTkLabel(frame, text=f"🏷 {tags_str}", anchor="w", font=("Arial", 12, "italic"),
                                          text_color="#fbbf24")
                tags_label.pack(side="top", padx=15, pady=(0, 10), fill="x", expand=True)

            frame.bind("<Button-1>", lambda e, index=i: self.select_task(index))
            label.bind("<Button-1>", lambda e, index=i: self.select_task(index))

    def select_task(self, index):
        self.selected_index = index
        for i, frame in enumerate(self.task_frame.winfo_children()):
            task = self.filtered_tasks[i]
            if i == index:
                frame.configure(fg_color="#2563eb")
            else:
                frame.configure(fg_color="#14532d" if task["done"] else "#1f2937")

    # ------------------------
    # Theme Toggle
    # ------------------------
    def toggle_theme(self):
        current = ctk.get_appearance_mode()
        new_mode = "Light" if current == "Dark" else "Dark"
        ctk.set_appearance_mode(new_mode)
        self.theme_toggle_btn.configure(text="🌞" if new_mode == "Light" else "🌙")


# ------------------------
# Run
# ------------------------
app = TaskApp()
app.mainloop()
