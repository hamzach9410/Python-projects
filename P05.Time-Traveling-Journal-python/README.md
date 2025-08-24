# ⏳ Time-Traveling Journal – Python Project

This is a creative and interactive Python project that allows users to write personal journal entries, read old ones, and even write messages to their **future self**. It combines file handling, date management, and a bit of fun randomness.

---

## 📖 What This App Can Do

- ✅ Write your journal entry for today
- 📅 Read any entry by entering a specific date
- 🎲 Read a random entry from the past
- 🔮 Write a message to your future self for a specific date
- ❌ Exit anytime safely

All entries are saved in `.txt` files, automatically organized by date in a folder named `entries`.

---

## 🧠 Why I Built This

I wanted to create something personal and practical while learning:

- File handling in Python
- Working with `datetime` and `os` modules
- Taking user input
- Random file selection logic
- Menu-driven console apps

This app is like your **personal time machine for thoughts**.

---

## 💻 How to Run

1. Make sure you have Python installed (Python 3.x)
2. Download the script: `6_Time-Traveling Journal.py`
3. Open terminal or command prompt
4. Run this command:

```bash
python "6_Time-Traveling Journal.py"
```

The script will create a folder named `entries` and store all journal files inside it.

---

## 🧪 Sample Run

```text
========== 📓 Time-Traveling Journal ==========
1. ✍️ Write Today's Entry
2. 🔍 Read Entry by Date
3. 🎲 Read Random Past Entry
4. 🗓️ Write Message to Future
5. ❌ Exit
Choose an option (1-5): 1

🖊️ Write your journal entry for 2025-06-18:
→ Had a productive day learning Python and building a time-traveling journal app.
✅ Entry saved successfully!
```

---

## 📦 Technologies Used

- Python 3.x
- `os` module (to create folders, manage files)
- `datetime` (to handle date inputs)
- `random` (to pick a random file)
- Terminal/command-line interface

---

## 📂 File Structure

```
entries/
├── 2025-06-18.txt
├── 2025-07-01.txt
├── 2025-12-31.txt
...
```

Each file stores a single journal entry based on the date.

---

## 📄 License

MIT License – This project is free to use, modify, and share with credit.

---

## 🙋‍♂️ About the Author

I'm **Ali Hamza**, a Full stack ai Developer passionate about building creative and meaningful tools.  
This project is a mix of creativity and coding — and I hope it inspires others to document their journey too.

> “Don’t just travel through time — write in it.”
