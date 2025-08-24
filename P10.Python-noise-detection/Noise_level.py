import sounddevice as sd
import numpy as np
import time
import math

SAMPLE_RATE = 44100
BLOCK_SIZE = 2048
METER_WIDTH = 30  # bar length in characters

def dbfs(block):
    if block.ndim > 1:
        block = np.mean(block, axis=1)
    rms = np.sqrt(np.mean(block**2))
    if rms <= 1e-12:
        return -120.0
    return 20 * math.log10(rms)

def classify(db):
    if db <= -35:
        return "Quiet"
    elif db <= -20:
        return "Normal"
    else:
        return "Noisy"

def suggestion(label):
    if label == "Quiet":
        return " Good for study, reading, or focus."
    elif label == "Normal":
        return " Good for conversation or light work."
    else:
        return " Too noisy! Not good for study."

def render_meter(db):
    clamped = max(-60, min(0, db))
    fill = int(((clamped + 60) / 60) * METER_WIDTH)
    bar = "#" * fill + "-" * (METER_WIDTH - fill)
    return f"[{bar}] {db:5.1f} dB"

def main():
    duration = int(input("Seconds to measure: "))
    print("\nMeasuring noise level...\n")

    levels = []
    start = time.time()
    with sd.InputStream(samplerate=SAMPLE_RATE, blocksize=BLOCK_SIZE, channels=1, dtype="float32") as stream:
        while time.time() - start < duration:
            block, _ = stream.read(BLOCK_SIZE)
            level = dbfs(block)
            levels.append(level)
            print(f"\r{render_meter(level)} | {classify(level):>6}", end="", flush=True)
    avg = np.mean(levels)
    label = classify(avg)
    print("\n\nDone")
    print(f"Average level: {avg:.1f} dB → {label}")
    print(suggestion(label))

if __name__ == "__main__":
    main()
