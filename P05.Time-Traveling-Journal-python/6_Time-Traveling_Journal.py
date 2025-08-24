import os
import random
from datetime import datetime
import tkinter as tk
from tkinter import scrolledtext, simpledialog

# Create entries folder if not exists
if not os.path.exists("entries"):
    os.makedirs("entries")

# ------------------ Functions ------------------
def write_entry(date_str, text_widget):
    content = text_widget.get("1.0", tk.END).strip()
    if content:
        file_path = f"entries/{date_str}.txt"
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        status_label.config(text=f"✅ Entry saved for {date_str}", fg="#50fa7b")
    else:
        status_label.config(text="⚠️ Nothing to save!", fg="#ff5555")

def read_entry(date_str, text_widget):
    file_path = f"entries/{date_str}.txt"
    text_widget.delete("1.0", tk.END)
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            text_widget.insert(tk.END, f.read())
        status_label.config(text=f"📖 Entry loaded for {date_str}", fg="#f1fa8c")
    else:
        status_label.config(text="❌ No entry found for that date.", fg="#ff5555")

def random_entry(text_widget):
    files = os.listdir("entries")
    text_widget.delete("1.0", tk.END)
    if files:
        file = random.choice(files)
        with open(f"entries/{file}", "r", encoding="utf-8") as f:
            text_widget.insert(tk.END, f.read())
        status_label.config(text=f"🎲 Random entry from {file.replace('.txt','')}", fg="#8be9fd")
    else:
        status_label.config(text="🪹 No entries found.", fg="#ff5555")

def search_keyword(keyword, text_widget):
    text_widget.delete("1.0", tk.END)
    files = os.listdir("entries")
    found = False
    for file in files:
        with open(f"entries/{file}", "r", encoding="utf-8") as f:
            content = f.read()
            if keyword.lower() in content.lower():
                text_widget.insert(tk.END, f"📅 {file.replace('.txt','')}:\n{content}\n\n")
                found = True
    if found:
        status_label.config(text=f"🔍 Showing entries with '{keyword}'", fg="#ff79c6")
    else:
        status_label.config(text=f"❌ No entries found with '{keyword}'", fg="#ff5555")

# ------------------ GUI ------------------
class RumiApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📓 RUMI - Time-Traveling Journal")
        self.root.geometry("750x700")
        self.root.configure(bg="#1e1e2f")

        # Title
        tk.Label(root, text="RUMI - Time-Traveling Journal", font=("Helvetica", 22, "bold"),
                 fg="#ff79c6", bg="#1e1e2f").pack(pady=10)

        # Date Entry
        tk.Label(root, text="📅 Select Date (YYYY-MM-DD):", font=("Arial", 12, "bold"),
                 fg="#f8f8f2", bg="#1e1e2f").pack(pady=5)
        self.date_entry = tk.Entry(root, font=("Arial", 12), width=20, fg="gray")
        self.date_entry.pack()
        self.date_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))
        self.date_entry.bind("<FocusIn>", self.clear_placeholder)
        self.date_entry.bind("<FocusOut>", self.add_placeholder)

        # Pick date button
        tk.Button(root, text="📆 Pick Today", command=self.pick_today,
                  bg="#ffb86c", fg="black", font=("Arial", 12, "bold")).pack(pady=5)

        # Text Area
        self.text_area = scrolledtext.ScrolledText(root, width=90, height=25, font=("Arial", 12),
                                                   bg="#282a36", fg="#f8f8f2", insertbackground="white")
        self.text_area.pack(pady=10)

        # Buttons Frame
        btn_frame = tk.Frame(root, bg="#1e1e2f")
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="💾 Save Entry", command=lambda: write_entry(self.date_entry.get(), self.text_area),
                  bg="#50fa7b", fg="black", font=("Arial", 12, "bold")).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="📖 Load Entry", command=lambda: read_entry(self.date_entry.get(), self.text_area),
                  bg="#8be9fd", fg="black", font=("Arial", 12, "bold")).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="🎲 Random Entry", command=lambda: random_entry(self.text_area),
                  bg="#ff79c6", fg="black", font=("Arial", 12, "bold")).grid(row=0, column=2, padx=5)

        # Search Section
        search_frame = tk.Frame(root, bg="#1e1e2f")
        search_frame.pack(pady=10)
        tk.Label(search_frame, text="🔎 Search Keyword:", font=("Arial", 12, "bold"), fg="#f8f8f2", bg="#1e1e2f").grid(row=0, column=0)
        self.search_entry = tk.Entry(search_frame, font=("Arial", 12), width=25)
        self.search_entry.grid(row=0, column=1, padx=5)
        tk.Button(search_frame, text="Search", command=lambda: search_keyword(self.search_entry.get(), self.text_area),
                  bg="#ff79c6", fg="black", font=("Arial", 12, "bold")).grid(row=0, column=2, padx=5)

        # Status Label
        global status_label
        status_label = tk.Label(root, text="", font=("Arial", 12), bg="#1e1e2f")
        status_label.pack(pady=5)

    def clear_placeholder(self, event):
        if self.date_entry.get() == datetime.now().strftime("%Y-%m-%d"):
            self.date_entry.delete(0, tk.END)
            self.date_entry.config(fg="black")

    def add_placeholder(self, event):
        if not self.date_entry.get():
            self.date_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))
            self.date_entry.config(fg="gray")

    def pick_today(self):
        self.date_entry.delete(0, tk.END)
        self.date_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))
        self.date_entry.config(fg="black")
        status_label.config(text="📆 Date set to today", fg="#8be9fd")

# Run App
if __name__ == "__main__":
    root = tk.Tk()
    app = RumiApp(root)
    root.mainloop()
