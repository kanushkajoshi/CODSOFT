import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("ONLY FOR YOU")  # The string is the name of the application

        self.tasks = []

        # Set background color for the main window
        self.master.config(bg="#2c3e50")  # Dark blue

        # Title label
        self.title_label = tk.Label(master, text="Your To Do List", font=("Helvetica", 20), bg="#3498db", fg="white")  # Light blue background, white text
        self.title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Task entry
        self.task_entry = tk.Entry(master, width=40, font=("Helvetica", 12), bg="#ecf0f1")  # Light grey
        self.task_entry.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        # Add button
        self.add_button = tk.Button(master, text="Add Your Task", command=self.add_task, bg="#2ecc71", fg="white", font=("Helvetica", 12))  # Green background, white text
        self.add_button.grid(row=1, column=1, padx=5, pady=10, sticky="ew")

        # Task listbox
        self.task_listbox = tk.Listbox(master, width=50, height=15, font=("Helvetica", 12), bg="#ecf0f1")  # Light grey
        self.task_listbox.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

        # Delete button
        self.delete_button = tk.Button(master, text="Delete Task", command=self.delete_task, bg="#e74c3c", fg="white", font=("Helvetica", 12))  # Red background, white text
        self.delete_button.grid(row=3, column=0, padx=5, pady=10, sticky="ew")

        # Update button
        self.update_button = tk.Button(master, text="Update Task", command=self.update_task, bg="#f1c40f", fg="black", font=("Helvetica", 12))  # Yellow background, black text
        self.update_button.grid(row=3, column=1, padx=5, pady=10, sticky="ew")

        
        self.refresh_tasks()

    def refresh_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task['title'])

    def add_task(self):
        task_title = self.task_entry.get()
        if task_title:
            self.tasks.append({'title': task_title})
            self.refresh_tasks()
            self.task_entry.delete(0, tk.END)

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            del self.tasks[selected_index[0]]
            self.refresh_tasks()

    def update_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            new_title = self.task_entry.get()
            if new_title:
                self.tasks[selected_index[0]]['title'] = new_title
                self.refresh_tasks()

def main():
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

