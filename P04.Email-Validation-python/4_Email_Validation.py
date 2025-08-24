import tkinter as tk
import re
from difflib import get_close_matches

# Common email domains for suggestions
COMMON_DOMAINS = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "icloud.com"]

def suggest_domain(user_domain):
    matches = get_close_matches(user_domain, COMMON_DOMAINS, n=1, cutoff=0.6)
    return matches[0] if matches else None

def validate_email(email):
    warnings = []

    if len(email) < 6:
        warnings.append("Email must be at least 6 characters long.")
    if not email[0].isalpha():
        warnings.append("Email must start with a letter.")
    if email.count("@") != 1:
        warnings.append("Email must contain exactly one '@' symbol.")
    if " " in email:
        warnings.append("Email must not contain spaces.")
    if not re.match(r"^[A-Za-z0-9._@]+$", email):
        warnings.append("Email contains invalid characters.")

    if "@" in email:
        domain = email.split("@")[-1]
        if not (domain.endswith(".com") or domain.endswith(".net") or domain.endswith(".org")):
            warnings.append("Email domain must end with .com, .net, or .org.")
        suggestion = suggest_domain(domain)
        if suggestion and domain != suggestion:
            warnings.append(f"Did you mean: {email.split('@')[0]}@{suggestion}?")
    return warnings

# -------------------- Tkinter UI --------------------
class EmailValidatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📧 RUMI Email Validator")
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        self.root.config(bg="#121212")  # dark grey/black background

        # Title
        title = tk.Label(root, text="Email Validator RUMI v2", 
                         font=("Helvetica", 20, "bold"), fg="#ffa500", bg="#121212")
        title.pack(pady=25)

        # Entry field
        self.email_entry = tk.Entry(root, font=("Arial", 14), width=30, fg="gray", bg="#1e1e1e", insertbackground="white")
        self.email_entry.insert(0, "Enter your email here...")
        self.email_entry.bind("<FocusIn>", self.clear_placeholder)
        self.email_entry.bind("<FocusOut>", self.add_placeholder)
        self.email_entry.pack(pady=15)

        # Validate button
        self.validate_btn = tk.Button(root, text="Validate Email", command=self.check_email,
                                      font=("Arial", 12, "bold"), bg="#333333", fg="#ffa500", activebackground="#444444", activeforeground="#ffffff")
        self.validate_btn.pack(pady=10)

        # Output / warning area
        self.output_label = tk.Label(root, text="", font=("Arial", 12), justify="left", bg="#121212")
        self.output_label.pack(pady=20)

    def clear_placeholder(self, event):
        if self.email_entry.get() == "Enter your email here...":
            self.email_entry.delete(0, tk.END)
            self.email_entry.config(fg="white")

    def add_placeholder(self, event):
        if not self.email_entry.get():
            self.email_entry.insert(0, "Enter your email here...")
            self.email_entry.config(fg="gray")

    def check_email(self):
        email = self.email_entry.get().strip()
        warnings = validate_email(email)
        if not warnings:
            self.output_label.config(text="✅ Email is valid!", fg="#50fa7b")
        else:
            warning_text = "⚠️ Issues found:\n" + "\n".join([f"• {w}" for w in warnings])
            self.output_label.config(text=warning_text, fg="#ff5555")

# Run app
if __name__ == "__main__":
    root = tk.Tk()
    app = EmailValidatorApp(root)
    root.mainloop()
