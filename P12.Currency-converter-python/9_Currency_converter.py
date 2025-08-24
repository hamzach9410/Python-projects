import tkinter as tk
from tkinter import messagebox
import requests

def convert_currency():
    from_curr = from_entry.get().upper()
    to_curr = to_entry.get().upper()
    try:
        amount = float(amount_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Amount must be a number.")
        return

    url = f"https://api.exchangerate-api.com/v4/latest/{from_curr}"
    response = requests.get(url)

    if response.status_code != 200:
        messagebox.showerror("Error", "Failed to fetch data.")
        return

    data = response.json()
    rate = data['rates'].get(to_curr)

    if rate:
        converted = amount * rate
        result_label.config(
            text=f"{amount:.2f} {from_curr} = {converted:.2f} {to_curr}",
            fg="green"
        )
    else:
        messagebox.showerror("Error", f"Currency code '{to_curr}' not found.")

# ---------------- GUI Setup ----------------
root = tk.Tk()
root.title("Currency Converter")
root.geometry("350x300")
root.configure(bg="#f5f5f5")

tk.Label(root, text="Currency Converter 💱", font=("Arial", 16, "bold"), bg="#f5f5f5").pack(pady=10)

tk.Label(root, text="From Currency (e.g. USD):", bg="#f5f5f5").pack()
from_entry = tk.Entry(root)
from_entry.pack()

tk.Label(root, text="To Currency (e.g. PKR):", bg="#f5f5f5").pack()
to_entry = tk.Entry(root)
to_entry.pack()

tk.Label(root, text="Amount:", bg="#f5f5f5").pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

tk.Button(root, text="Convert", command=convert_currency, bg="#007ACC", fg="white").pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), bg="#f5f5f5")
result_label.pack(pady=10)

root.mainloop()
