import tkinter as tk

class RumiTodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📝 RUMI To-Do List App")
        self.root.geometry("600x500")
        self.root.config(bg="#2E3440")  # Dark background
        self.tasks = []

        # Title
        tk.Label(
            root, text="✨ Welcome to RUMI To-Do List ✨",
            font=("Helvetica", 18, "bold"),
            bg="#2E3440", fg="#88C0D0"
        ).pack(pady=15)

        # Entry field with placeholder
        self.task_entry = tk.Entry(
            root, width=40, font=("Arial", 14),
            fg="gray", bg="#3B4252", relief="flat", insertbackground="white"
        )
        self.task_entry.pack(pady=10, ipady=5)
        self.task_entry.insert(0, "Enter a new task here...")

        self.task_entry.bind("<Button-1>", self.clear_placeholder)
        self.task_entry.bind("<FocusIn>", self.clear_placeholder)
        self.task_entry.bind("<FocusOut>", self.add_placeholder)
        self.task_entry.bind("<Return>", lambda event: self.add_task())

        # Listbox with scrollbar
        list_frame = tk.Frame(root, bg="#2E3440")
        list_frame.pack(pady=10)

        self.task_listbox = tk.Listbox(
            list_frame, width=50, height=10,
            selectmode=tk.SINGLE, font=("Arial", 13),
            bg="#3B4252", fg="white", highlightthickness=0,
            selectbackground="#5E81AC", selectforeground="white", relief="flat"
        )
        self.task_listbox.pack(side="left", fill="both")

        scrollbar = tk.Scrollbar(list_frame, command=self.task_listbox.yview)
        scrollbar.pack(side="right", fill="y")
        self.task_listbox.config(yscrollcommand=scrollbar.set)

        # Key bindings
        self.task_listbox.bind("<Double-1>", lambda event: self.mark_done())
        self.task_listbox.bind("<Delete>", lambda event: self.delete_task())
        self.task_listbox.bind("<BackSpace>", lambda event: self.delete_task())
        self.task_listbox.bind("<Return>", lambda event: self.update_task())
        self.task_listbox.bind("<Up>", lambda event: self.navigate_listbox(-1))
        self.task_listbox.bind("<Down>", lambda event: self.navigate_listbox(1))

        # Remaining tasks label
        self.remaining_label = tk.Label(
            root, text="Remaining Tasks: 0",
            font=("Arial", 12, "italic"),
            bg="#2E3440", fg="#A3BE8C"
        )
        self.remaining_label.pack()

        # Info / status label
        self.info_label = tk.Label(
            root, text="", fg="#EBCB8B",
            font=("Arial", 11, "italic"), bg="#2E3440"
        )
        self.info_label.pack(pady=5)

        # Buttons frame
        btn_frame = tk.Frame(root, bg="#2E3440")
        btn_frame.pack(pady=15)

        self.create_button(btn_frame, "➕ Add Task", self.add_task, 0)
        self.create_button(btn_frame, "✏ Update", self.update_task, 1)
        self.create_button(btn_frame, "❌ Delete", self.delete_task, 2)
        self.create_button(btn_frame, "✔ Done", self.mark_done, 3)
        self.create_button(btn_frame, "🚪 Exit", root.quit, 4)

    # ---------- UI Helpers ----------
    def create_button(self, parent, text, command, col):
        btn = tk.Button(
            parent, text=text, command=command,
            font=("Arial", 11, "bold"),
            bg="#4C566A", fg="white", relief="flat", width=12, height=2,
            activebackground="#81A1C1", activeforeground="black", cursor="hand2"
        )
        btn.grid(row=0, column=col, padx=6)
        return btn

    def clear_placeholder(self, event):
        if self.task_entry.get() == "Enter a new task here...":
            self.task_entry.delete(0, tk.END)
            self.task_entry.config(fg="white")

    def add_placeholder(self, event):
        if not self.task_entry.get():
            self.task_entry.insert(0, "Enter a new task here...")
            self.task_entry.config(fg="gray")

    # ---------- Core Functions ----------
    def add_task(self):
        task = self.task_entry.get().strip()
        if task and task != "Enter a new task here...":
            self.tasks.append(task)
            self.refresh_listbox()
            self.task_entry.delete(0, tk.END)
            self.add_placeholder(None)
            self.update_remaining()
            self.info_label.config(text=f"Task '{task}' added ✅")
        else:
            self.info_label.config(text="⚠ Please enter a task before adding.")

    def update_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            new_task = self.task_entry.get().strip()
            if new_task and new_task != "Enter a new task here...":
                self.tasks[index] = new_task
                self.refresh_listbox()
                self.task_entry.delete(0, tk.END)
                self.add_placeholder(None)
                self.update_remaining()
                self.info_label.config(text=f"Task updated to '{new_task}' ✏")
            else:
                self.info_label.config(text="⚠ Please enter new task text before updating.")
        except IndexError:
            self.info_label.config(text="⚠ Select a task to update.")

    def delete_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            task = self.tasks.pop(index)
            self.refresh_listbox()
            self.update_remaining()
            self.info_label.config(text=f"Task '{task}' deleted ❌")
        except IndexError:
            self.info_label.config(text="⚠ Select a task to delete.")

    def mark_done(self):
        try:
            index = self.task_listbox.curselection()[0]
            task = self.tasks[index]
            if not task.startswith("✔ "):
                self.tasks[index] = f"✔ {task}"
                self.refresh_listbox()
                self.task_listbox.itemconfig(index, fg="#A3BE8C", font=("Arial", 12, "overstrike"))
                self.update_remaining()
                self.info_label.config(text=f"Task '{task}' marked as done 🎉")
        except IndexError:
            self.info_label.config(text="⚠ Select a task to mark as done.")

    def update_remaining(self):
        remaining = sum(1 for task in self.tasks if not str(task).startswith("✔"))
        self.remaining_label.config(text=f"Remaining Tasks: {remaining}")

    def refresh_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for i, task in enumerate(self.tasks, start=1):
            self.task_listbox.insert(tk.END, f"{i}. {task}")

    def navigate_listbox(self, step):
        if not self.tasks:
            return
        try:
            index = self.task_listbox.curselection()[0]
        except IndexError:
            index = 0
        new_index = max(0, min(len(self.tasks) - 1, index + step))
        self.task_listbox.selection_clear(0, tk.END)
        self.task_listbox.selection_set(new_index)
        self.task_listbox.activate(new_index)

# Run app
if __name__ == "__main__":
    root = tk.Tk()
    app = RumiTodoApp(root)
    root.mainloop()
