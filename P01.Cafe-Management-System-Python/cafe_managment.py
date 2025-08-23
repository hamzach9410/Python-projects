import tkinter as tk
from tkinter import messagebox

def restaurant_management():
    # Restaurant Name
    root = tk.Tk()
    root.title("RUMI Restaurant - Menu")
    root.geometry("400x400")
    
    # Menu Items with Prices
    menu = {
        "Pizza": 1500,
        "Coffee": 80,
        "Zinger Burger": 320,
        "Hot Wings": 600,
        "Cake": 450,
        "Chips": 150,
        "Coke": 70,
        "Pasta": 400,
        "Ice Cream": 200
    }
    
    cart = []  # store ordered items
    
    # Add item to cart
    def add_to_cart(item):
        cart.append(item)
        messagebox.showinfo("Added to Cart", f"{item} added to cart!")
    
    # Show final bill
    def checkout():
        if not cart:
            messagebox.showwarning("Empty Cart", "You haven't ordered anything yet!")
            return
        total = sum(menu[item] for item in cart)
        order_summary = "\n".join([f"{item} - Rs {menu[item]}" for item in cart])
        messagebox.showinfo("Final Bill", f"Your Order:\n{order_summary}\n\nTotal: Rs {total}")
    
    # Heading
    tk.Label(root, text="_____WELCOME TO RUMI RESTAURANT_____", font=("Arial", 14, "bold")).pack(pady=10)
    
    # Menu Buttons
    for item, price in menu.items():
        btn = tk.Button(root, text=f"{item} - Rs {price}", width=25, command=lambda i=item: add_to_cart(i))
        btn.pack(pady=5)
    
    # Checkout Button
    tk.Button(root, text="Checkout", bg="green", fg="white", width=20, command=checkout).pack(pady=20)
    
    root.mainloop()


restaurant_management()


print("Thank you for visiting RUMI Restaurant!")# Thank you message


# Code by RUMI  
