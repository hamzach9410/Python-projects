# 🔔 Desktop Reminder App – Python Project

This is a **Python-based desktop reminder app** that sends system notifications at regular time intervals. It's built using the `plyer` library and runs in the terminal, making it lightweight and easy to use for daily reminders.

---

## ✅ Features

- ⏱️ Set reminder intervals (in minutes)
- 💬 Enter your custom reminder message
- 🔄 Shows live countdown until the next notification
- 🔔 Sends desktop notifications using system tray
- Works cross-platform (Windows, macOS, Linux)

---

## 🧠 What You'll Learn

- Working with the **`plyer`** notification library
- Countdown logic with `time.sleep()` and loops
- Terminal display refresh (`os.system('cls')` or `clear`)
- Input validation and infinite reminder loops

---

## 💻 How to Run

1. Make sure Python 3 is installed
2. Install the `plyer` library:

```bash
pip install plyer
```

3. Save the file as `desktop_reminder.py`
4. Run the script:

```bash
python desktop_reminder.py
```

5. Enter the reminder interval and message when prompted

---

## 🧪 Example Output

```text
⏱️ Enter reminder interval (in minutes): 1
💬 Enter reminder message: Drink Water

⏳ Time left for next reminder: 00:59
⏳ Time left for next reminder: 00:58
...
🔔 Notification: Drink Water
```

The notification will appear every 1 minute with the message "Drink Water."

---

## 📦 Technologies Used

- Python 3.x
- `plyer` – for desktop notifications
- `time` – for countdown timer
- `os` – for cross-platform terminal clearing

---

## 📌 Why I Built This

This project was made to help users stay productive and healthy by sending them reminders right on their desktop. It’s also a fun way to explore real-world Python automation.

---

## 📄 License

MIT License – Free to use, improve, and share with credit.

---

## 🙋‍♂️ About Me

I'm **Ali Hamza**, a creative Python developer building tools that solve small problems with smart code. This desktop reminder app is part of my daily productivity experiments.

> “Simple reminders lead to strong habits.”
