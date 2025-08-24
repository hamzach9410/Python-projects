import tkinter as tk
from tkinter import messagebox
import re

# ---------------- Password Strength Logic ----------------
def check_strength(password):
    length = len(password) >= 8
    upper = re.search(r"[A-Z]", password)
    lower = re.search(r"[a-z]", password)
    digit = re.search(r"\d", password)
    special = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    score = sum([bool(length), bool(upper), bool(lower), bool(digit), bool(special)])

    if score <= 2:
        return "❌ Weak", "#e74c3c"   # Red
    elif score == 3 or score == 4:
        return "⚠️ Moderate", "#f39c12"  # Orange
    else:
        return "✅ Strong", "#27ae60"   # Green

def analyze():
    pwd = password_entry.get()
    if not pwd:
        messagebox.showwarning("Empty Field", "Please enter a password.")
        return

    result, color = check_strength(pwd)
    result_label.config(text=f"Password Strength: {result}", fg=color)

# ---------------- GUI Setup ----------------
root = tk.Tk()
root.title("🔐 Password Strength Checker")
root.geometry("450x250")
root.resizable(False, False)
root.configure(bg="#ecf0f1")  # Light gray background

# -------- Frame (Card Style) --------
card = tk.Frame(root, bg="white", bd=0, relief="flat")
card.place(relx=0.5, rely=0.5, anchor="center", width=380, height=180)

# -------- Title --------
title_label = tk.Label(card, text="🔐 Password Strength Checker",
                       font=("Helvetica", 14, "bold"), fg="#2c3e50", bg="white")
title_label.pack(pady=10)

# -------- Password Entry --------
tk.Label(card, text="Enter your password:", font=("Arial", 11), bg="white", fg="#2c3e50").pack()

password_entry = tk.Entry(card, show="*", width=30, font=("Arial", 12), bd=2, relief="groove", justify="center")
password_entry.pack(pady=5)

# -------- Button with Hover Effect --------
def on_enter(e):
    check_btn.config(bg="#2980b9")
def on_leave(e):
    check_btn.config(bg="#3498db")

check_btn = tk.Button(card, text="Check Strength", command=analyze,
                      font=("Arial", 12, "bold"), bg="#3498db", fg="white",
                      relief="flat", padx=10, pady=5, cursor="hand2")
check_btn.pack(pady=10)

check_btn.bind("<Enter>", on_enter)
check_btn.bind("<Leave>", on_leave)

# -------- Result Label --------
result_label = tk.Label(card, text="", font=("Arial", 12, "bold"), bg="white")
result_label.pack()

root.mainloop()
