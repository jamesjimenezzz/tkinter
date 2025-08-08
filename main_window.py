import tkinter as tk
from db import database as db
font_default = ("Arial", 14)


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("1366x768")

        self.task_entry = tk.Entry(self.root, width=30, font=(font_default))
        self.task_entry.pack(pady=10)

        tk.Button(self.root, text="Add Task", font=(font_default), command=(self.add_task)).pack(pady=5)
        tk.Button(self.root, text="Delete Task", font=(font_default), command=(self.delete_task)).pack(pady=5)

        self.task_listbox = tk.Listbox(self.root, width=40, height=15, font=(font_default))
        self.task_listbox.pack(pady=10)
        self.task_ids = []
        self.load_tasks()

    def load_tasks(self):
        self.task_listbox.delete(0, tk.END)
        self.task_ids.clear()
        for  task_id, title in db.get_tasks():
            self.task_listbox.insert(tk.END, f"{title}")
            self.task_ids.append(task_id)
    def add_task(self):
        title = self.task_entry.get().strip()
        if title:
            db.add_task(title)
            self.task_entry.delete(0, tk.END)
            self.load_tasks()
    
    def delete_task(self):
        selection = self.task_listbox.curselection()

        if selection:
            idx = selection[0]
            f = self.task_ids[idx]
            db.del_tasks(int(f))
            self.load_tasks()

