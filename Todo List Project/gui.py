import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont
from todo_list import ToDoList

# TO DO APP

class ToDoApp:
    def __init__(self, root):
        self.todo_list = ToDoList()
        self.root = root
        self.root.title("To-Do List")

        # Define color scheme
        self.bg_color = "#2e2e2e"
        self.fg_color = "#ffffff"
        self.button_bg_color = "#4d4d4d"
        self.button_fg_color = "#ffffff"
        self.entry_bg_color = "#3e3e3e"
        self.entry_fg_color = "#ffffff"
        self.listbox_bg_color = "#3e3e3e"
        self.listbox_fg_color = "#ffffff"
        self.scrollbar_bg_color = "#4d4d4d"

        self.root.config(bg=self.bg_color)

        self.heading_font = tkfont.Font(family="Helvetica", size=20, weight="bold", slant="italic")

        self.heading = tk.Label(root, text="To-Do List", font=self.heading_font, fg="blue")
        self.heading.pack(pady=10)

        self.heading.bind("<Enter>", self.on_heading_enter)
        self.heading.bind("<Leave>", self.on_heading_leave)

        # Frame for tasks
        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.task_listbox = tk.Listbox(self.frame, width=70, height=10, bg=self.listbox_bg_color, fg=self.listbox_fg_color)
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        self.entry = tk.Entry(root, width=50, bg=self.entry_bg_color, fg=self.entry_fg_color)
        self.entry.pack(pady=5)


        self.add_task_button = tk.Button(root, text="Add Task", command=self.add_task, bg=self.button_bg_color, fg=self.button_fg_color)
        self.add_task_button.pack(pady=5)

        self.remove_task_button = tk.Button(root, text="Remove Task", command=self.remove_task, bg=self.button_bg_color, fg=self.button_fg_color)
        self.remove_task_button.pack(pady=5)

        self.update_task_button = tk.Button(root, text="Update Task", command=self.update_task, bg=self.button_bg_color, fg=self.button_fg_color)
        self.update_task_button.pack(pady=5)

        self.mark_complete_button = tk.Button(root, text="Mark Complete", command=self.mark_complete, bg=self.button_bg_color, fg=self.button_fg_color)
        self.mark_complete_button.pack(pady=5)

        self.mark_incomplete_button = tk.Button(root, text="Mark Incomplete", command=self.mark_incomplete, bg=self.button_bg_color, fg=self.button_fg_color)
        self.mark_incomplete_button.pack(pady=5)

        self.refresh_task_list()

    def on_heading_enter(self, event):
        self.heading.config(fg="red")

    def on_heading_leave(self, event):
        self.heading.config(fg="blue")

    def refresh_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.todo_list.tasks:
            display_text = task.description
            if task.completed:
                display_text = f"{display_text:<60} ✓"
            self.task_listbox.insert(tk.END, display_text)

    def add_task(self):
        description = self.entry.get()
        if description:
            self.todo_list.add_task(description)
            self.refresh_task_list()
            self.entry.delete(0, tk.END)

    def remove_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.todo_list.remove_task(selected_task_index[0])
            self.refresh_task_list()

    def update_task(self):
        selected_task_index = self.task_listbox.curselection()
        description = self.entry.get()
        if selected_task_index and description:
            self.todo_list.update_task(selected_task_index[0], description)
            self.refresh_task_list()
            self.entry.delete(0, tk.END)

    def mark_complete(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.todo_list.mark_task_complete(selected_task_index[0])
            self.refresh_task_list()

    def mark_incomplete(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.todo_list.mark_task_incomplete(selected_task_index[0])
            self.refresh_task_list()

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()

