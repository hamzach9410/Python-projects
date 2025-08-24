import tkinter as tk
import time
import random

sentences = [
    "Python is a powerful programming language.",
    "Typing fast is a great skill to have.",
    "Practice makes perfect when learning code.",
    "Always write clean and readable code.",
    "Automation saves time and effort."
]

class TypingSpeedTest:
    def __init__(self, master):
        self.master = master
        master.title("⌨️ Typing Speed Tester")
        master.geometry("700x300")
        master.config(padx=20, pady=20)

        self.sentence = random.choice(sentences)
        self.start_time = 0

        self.label = tk.Label(master, text="Type the sentence below:", font=("Arial", 14))
        self.label.pack()

        self.sentence_label = tk.Label(master, text=self.sentence, font=("Arial", 16, "bold"), wraplength=650, fg="blue")
        self.sentence_label.pack(pady=10)

        self.entry = tk.Entry(master, font=("Arial", 14), width=70)
        self.entry.pack()
        self.entry.bind("<FocusIn>", self.start_timer)
        self.entry.bind("<Return>", self.calculate_speed)

        self.result_label = tk.Label(master, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

    def start_timer(self, event):
        if self.start_time == 0:
            self.start_time = time.time()

    def calculate_speed(self, event):
        end_time = time.time()
        time_taken = end_time - self.start_time
        typed_text = self.entry.get()

        words = len(typed_text.split())
        characters = len(typed_text)

        wpm = round((words / time_taken) * 60)
        cpm = round((characters / time_taken) * 60)

        accuracy = self.calculate_accuracy(typed_text, self.sentence)

        self.result_label.config(
            text=f"🕒 Time: {round(time_taken, 2)}s | ⌨️ WPM: {wpm} | 🔠 CPM: {cpm} | 🎯 Accuracy: {accuracy}%"
        )

    def calculate_accuracy(self, typed, original):
        correct_chars = sum(1 for i, c in enumerate(typed) if i < len(original) and c == original[i])
        return round((correct_chars / len(original)) * 100)

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTest(root)
    root.mainloop()
