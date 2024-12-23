import tkinter as tk
from logic import Logic

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = tk.Tk()
        self.__root.title("Vietnam Tonal Practice Tool")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = tk.Canvas(height=height, width=width, bg="white")
        self.__logic = Logic(self.__root)

        self.__canvas.pack()
        self.create_gui()

    def wait_for_close(self):
        self.__root.mainloop()

    def close(self):
        self.__root.destroy()

    def create_gui(self):
        # Create record sound button
        record_sound_button = tk.Button(self.__root, text="Record sound", width=25, command=lambda: self.__logic.record_sound())
        record_sound_button.place(x=200, y=500)
        
        # Create play sound button
        play_sound_button = tk.Button(self.__root, text="Play sound", width=25, command= self.__logic.play_sound)
        play_sound_button.place(x=500, y=500)

        # Bind the spacebar to the play_sound method
        self.__root.bind("<space>", self.spacebar_handler)

        # Bind the r button to the record_sound method
        self.__root.bind("<r>", lambda event: self.__logic.record_sound())

    def spacebar_handler(self, event):
        # When spacebar is pressed, call the play_sound method
        if not self.__logic._is_playing_sound:
            self.__logic.play_sound()
