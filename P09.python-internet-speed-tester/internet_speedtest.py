import tkinter as tk
from tkinter import ttk, messagebox
import speedtest
import threading

# Function to run speed test
def test_speed():
    try:
        # Disable button during test
        test_button.config(state="disabled")
        status_label.config(text="Testing your internet speed... Please wait ⏳")
        progress.start()

        st = speedtest.Speedtest()
        st.get_best_server()

        download_speed = st.download() / 1024 / 1024  # Mbps
        upload_speed = st.upload() / 1024 / 1024      # Mbps
        ping = st.results.ping

        # Update labels with results
        download_label.config(text=f"{download_speed:.2f} Mbps")
        upload_label.config(text=f"{upload_speed:.2f} Mbps")
        ping_label.config(text=f"{ping:.2f} ms")

        status_label.config(text="✅ Test Completed Successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong: {e}")
        status_label.config(text="❌ Test Failed. Try Again!")
    finally:
        progress.stop()
        test_button.config(state="normal")

# Threaded function so GUI doesn't freeze
def start_test():
    thread = threading.Thread(target=test_speed)
    thread.start()

# ----------------- GUI -----------------
root = tk.Tk()
root.title("🌐 RUMI Internet Speed Test")
root.geometry("600x400")
root.config(bg="#1e1e2f")

# Title
title = tk.Label(root, text="🚀 RUMI Speed Test Tool", 
                 font=("Segoe UI", 18, "bold"), bg="#1e1e2f", fg="#00ffcc")
title.pack(pady=10)

# Status Label
status_label = tk.Label(root, text="Click below to check your internet speed", 
                        font=("Segoe UI", 12), bg="#1e1e2f", fg="white")
status_label.pack(pady=5)

# Progress bar
progress = ttk.Progressbar(root, mode="indeterminate", length=300)
progress.pack(pady=10)

# Test Button
style = ttk.Style()
style.configure("TButton", font=("Segoe UI", 12, "bold"), padding=10)

test_button = ttk.Button(root, text="Start Speed Test", command=start_test)
test_button.pack(pady=10)

# Frame for results
frame = tk.Frame(root, bg="#2a2a40", bd=2, relief="ridge")
frame.pack(pady=20, padx=20, fill="x")

# Download Speed
tk.Label(frame, text="⬇ Download Speed", font=("Segoe UI", 12, "bold"), 
         bg="#2a2a40", fg="#00ffcc").grid(row=0, column=0, padx=20, pady=10)
download_label = tk.Label(frame, text="-- Mbps", font=("Segoe UI", 12), 
                          bg="#2a2a40", fg="white")
download_label.grid(row=0, column=1, padx=20)

# Upload Speed
tk.Label(frame, text="⬆ Upload Speed", font=("Segoe UI", 12, "bold"), 
         bg="#2a2a40", fg="#ffcc00").grid(row=1, column=0, padx=20, pady=10)
upload_label = tk.Label(frame, text="-- Mbps", font=("Segoe UI", 12), 
                        bg="#2a2a40", fg="white")
upload_label.grid(row=1, column=1, padx=20)

# Ping
tk.Label(frame, text="📶 Ping", font=("Segoe UI", 12, "bold"), 
         bg="#2a2a40", fg="#ff6666").grid(row=2, column=0, padx=20, pady=10)
ping_label = tk.Label(frame, text="-- ms", font=("Segoe UI", 12), 
                      bg="#2a2a40", fg="white")
ping_label.grid(row=2, column=1, padx=20)

# Exit button
exit_btn = ttk.Button(root, text="Exit", command=root.quit)
exit_btn.pack(pady=10)

root.mainloop()
