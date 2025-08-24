import tkinter as tk
from tkinter import scrolledtext
import requests
import re
import os

# ------------------ Functions ------------------
def download_instagram_reel(url, output_text):
    output_text.delete("1.0", tk.END)
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            output_text.insert(tk.END, "❌ Failed to fetch URL. Make sure the link is public.\n")
            return
        
        video_url_match = re.search(r'"playable_url":"([^"]+)"', response.text)
        if not video_url_match:
            output_text.insert(tk.END, "❌ Cannot find video URL. Possibly private or removed.\n")
            return
        
        video_url = video_url_match.group(1).replace("\\u0026", "&")
        file_name = url.split("/")[-2] + ".mp4"
        
        # Download video
        with requests.get(video_url, headers=headers, stream=True) as r:
            r.raise_for_status()
            with open(file_name, "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        output_text.insert(tk.END, f"✅ Reel downloaded as {file_name}\n")
        
    except Exception as e:
        output_text.insert(tk.END, f"❌ Error: {e}\n")

# ------------------ GUI ------------------
root = tk.Tk()
root.title("📥 Instagram Reel Downloader")
root.geometry("650x400")
root.configure(bg="#1e1e2f")

# Title
tk.Label(root, text="Instagram Reel Downloader", font=("Helvetica", 18, "bold"),
         fg="#ff79c6", bg="#1e1e2f").pack(pady=10)

# URL Entry
tk.Label(root, text="Paste Public Reel URL:", font=("Arial", 12, "bold"),
         fg="#f8f8f2", bg="#1e1e2f").pack(pady=5)
url_entry = tk.Entry(root, font=("Arial", 12), width=60, fg="black")
url_entry.pack(pady=5)

# Download Button
tk.Button(root, text="⬇️ Download Reel", command=lambda: download_instagram_reel(url_entry.get(), output_text),
          font=("Arial", 12, "bold"), bg="#50fa7b", fg="black").pack(pady=10)

# Output Area
output_text = scrolledtext.ScrolledText(root, width=75, height=12,
                                        font=("Arial", 12), bg="#282a36", fg="#f8f8f2",
                                        insertbackground="white")
output_text.pack(pady=10)

# Run App
root.mainloop()
