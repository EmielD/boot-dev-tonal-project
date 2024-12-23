import numpy as np
import sounddevice as sd
import threading
import time

class Logic:
    def __init__(self, window_root):
        self.__window_root = window_root
        self._is_playing_sound = False
        self._is_recording_sound = False
        self._current_recorded_sound = None

    def play_sound(self):
        if self._is_playing_sound:
            return  # Don't play sound if already playing

        self._is_playing_sound = True  # Set flag to indicate sound is playing

        # Stop any sound currently playing before starting a new one
        sd.stop()

        # Generate a sine wave for the sound
        fs = 44100  # Sample rate
        duration = 2  # Duration in seconds
        t = np.linspace(0, duration, int(fs * duration))  # Time vector
        sine_wave = 1 * np.sin(2 * np.pi * 440 * t)  # 440 Hz sine wave (A4)

        # Play the sine wave sound
        sd.play(sine_wave, samplerate=fs, blocking=False)

        # Use sd.wait() to block until the sound finishes
        # Schedule an 'after' call to reset _is_playing_sound after the sound finishes
        self.__window_root.after(int(duration * 1000), self.sound_finished)  # Duration in milliseconds

    def sound_finished(self):
        # Called after the sound finishes playing
        self._is_playing_sound = False
        print("Sound finished playing.")

    def record_sound(self):
        print("Recording sound...")