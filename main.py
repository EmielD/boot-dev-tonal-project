import sounddevice as sd
import numpy as np
from window import Window 

win = Window(1920, 1080)
win.wait_for_close()


# # Generate a sine wave for a longer duration (e.g., 5 seconds)
# fs = 44100  # Sample rate
# duration = 5  # Duration in seconds
# t = np.linspace(0, duration, int(fs * duration))  # Adjust length based on duration
# sine_wave = 1 * np.sin(2 * np.pi * 9000 * t)  # 440 Hz sine wave (A4)

# # Play the sine wave
# sd.play(sine_wave, samplerate=fs)
# sd.wait()  # Wait until the sound has finished
