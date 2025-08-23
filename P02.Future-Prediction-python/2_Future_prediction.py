import tkinter as tk
from tkinter import messagebox
import random
import datetime

# --- Prediction Generator ---
def gen_random_prediction():
    prediction = [
        "You will meet someone who will change your life soon!",
        "A big opportunity is coming your way, stay ready!",
        "Unexpected money will come to you when you least expect it!",
        "You will travel to a place you've always wanted to visit!",
        "A new skill you learn this year will bring success!",
        "Your hard work will pay off in ways you never imagined!",
        "You will find joy in the little things this week!",
        "A new friendship will blossom in the coming days!",
        "You will overcome a challenge that has been bothering you!",
        "Your creativity will shine in a project you undertake!",
        "A surprise gift will bring you immense joy!",
        "You will discover a hidden talent that will amaze you!",
        "A long-lost friend will reconnect with you soon!",
        "You will find peace in a situation that has been troubling you!",
        "You will inspire someone with your actions!",
        "A positive change in your life is on the horizon!",
        "You will experience a breakthrough in your personal growth!",
        "Your kindness will be rewarded in unexpected ways!",
        "You will find love in the most unexpected place!",
        "A new adventure awaits you, embrace it!",
        "You will achieve a goal you have been working towards!",
        "A new chapter in your life will begin soon!",
        "You will receive good news that will brighten your day!",
        "Your intuition will guide you to make the right choice!",
        "You will find balance and harmony in your life!"
    ]
    return random.choice(prediction)

def gen_lucky_number(birth_year):
    return (birth_year * random.randint(1, 9)) % 100

def gen_personality_trait(name):
    traits = ["Brave", "Creative", "Intelligent", "Kind", "Adventurous", "Focused", "Visionary"]
    return traits[sum(ord(char) for char in name) % len(traits)]

# --- GUI App ---
class FuturePredictorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🔮 RUMI Future Predictor")
        self.prediction_count = 0
        self.max_predictions = 3

        # Labels & Inputs
        tk.Label(root, text="Welcome to RUMI Future Predictor 🔮", font=("Arial", 14, "bold")).pack(pady=10)
        tk.Label(root, text="Enter your name:").pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        tk.Label(root, text="Enter your birth year (e.g. 2004):").pack()
        self.birth_entry = tk.Entry(root)
        self.birth_entry.pack()

        # Predict Button
        self.predict_btn = tk.Button(root, text="Reveal My Future ✨", command=self.show_prediction)
        self.predict_btn.pack(pady=15)

    def show_prediction(self):
        if self.prediction_count >= self.max_predictions:
            messagebox.showinfo("Limit Reached", "You have already predicted 3 times. Come back tomorrow! 🌙")
            return

        name = self.name_entry.get().strip()
        birth_year = self.birth_entry.get().strip()

        if not name or not birth_year.isdigit():
            messagebox.showerror("Error", "Please enter valid name and birth year.")
            return

        birth_year = int(birth_year)
        age = datetime.datetime.now().year - birth_year
        lucky_number = gen_lucky_number(birth_year)
        personality = gen_personality_trait(name)
        prediction = gen_random_prediction()

        self.prediction_count += 1

        messagebox.showinfo("🔮 Your Future",
            f"Name: {name}\n"
            f"Age: {age}\n"
            f"Lucky Number: {lucky_number}\n"
            f"Personality Trait: {personality}\n\n"
            f"✨ Prediction: {prediction}\n\n"
            f"({self.prediction_count}/3 Predictions Used)"
        )

# --- Run App ---
if __name__ == "__main__":
    root = tk.Tk()
    app = FuturePredictorApp(root)
    root.mainloop()
# Future Prediction App by RUMI
# Enjoy your journey into the future!  🌟