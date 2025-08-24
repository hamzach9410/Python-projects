from plyer import notification
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def remind_every(minutes, message):
    seconds = minutes * 60
    while True:
        for remaining in range(seconds, 0, -1):
            mins_left = remaining // 60
            secs_left = remaining % 60
            clear_screen()
            print(f"⏳ Time left for next reminder: {mins_left:02}:{secs_left:02}")
            time.sleep(1)

        notification.notify(
            title="🔔 Reminder",
            message=message,
            timeout=10
        )

if __name__ == "__main__":
    try:
        mins = int(input("⏱️ Enter reminder interval (in minutes): "))
        msg = input("💬 Enter reminder message: ")
        remind_every(mins, msg)
    except ValueError:
        print("❌ Please enter a valid number for minutes.")
