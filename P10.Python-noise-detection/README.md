Noise Level Meter 🎙️📊

This Python program measures the surrounding noise level in real-time using your microphone. It calculates the decibel value (dB), classifies the sound environment (Quiet, Normal, or Noisy), and gives useful suggestions based on the results.

🔧 Features

Records sound input from your microphone.

Calculates sound levels in decibels (dBFS).

Displays a visual noise meter bar in the terminal.

Classifies sound environment into:

Quiet → Good for study, reading, or focus.

Normal → Good for conversation or light work.

Noisy → Too noisy! Not good for study.

Shows average noise level after measurement.

📦 Requirements

Make sure you have the following installed:

pip install sounddevice numpy

Python version: 3.7+ recommended

▶️ How to Run

Save the program as Noise_level.py.

Open a terminal in the same directory.

Run the script:

python Noise_level.py

Enter the number of seconds you want to measure noise.

Watch the live noise meter update in real-time.

📊 Example Output
Seconds to measure: 5

Measuring noise level...

[##########--------------------] -32.5 dB | Quiet
[###############---------------] -24.0 dB | Normal

Done
Average level: -28.3 dB → Normal
Good for conversation or light work.

📌 Notes

Works best with a working microphone.

Values are in dBFS (Decibels relative to full scale), so don’t expect exact SPL meter accuracy.

Useful for testing ambient sound in study/work environments.
