import tkinter as tk
import json
import os

FILENAME = "tasks.json"
tasks = []

def load_tasks():
    global tasks
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            try:
                tasks = json.load(f)
            except json.JSONDecodeError:
                tasks = []

def save_tasks():
    with open(FILENAME, "w") as f:
        json.dump(tasks, f)

def add_task():
    title = entry.get()
    if title:
        tasks.append({"title": title, "done": False})
        save_tasks()
        update_listbox()
        entry.delete(0, tk.END)

def toggle_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        tasks[index]["done"] = not tasks[index]["done"]
        save_tasks()
        update_listbox()

def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        status = "✔" if task["done"] else "✘"
        listbox.insert(tk.END, f"[{status}] {task['title']}")

# GUI setup
root = tk.Tk()
root.title("To-Do List")

entry = tk.Entry(root, width=40)
entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

toggle_button = tk.Button(root, text="Mark Complete / Incomplete", command=toggle_task)
toggle_button.pack(pady=5)

load_tasks()
update_listbox()

root.mainloop()
