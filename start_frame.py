import tkinter as tk
from maths_game import MathsGame

class StartFrame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # GUI
        self.title = tk.Label(self, text="Maths Game")
        self.title.pack()

        self.button = tk.Button(
            self,
            text="Start Game",
            width=25,
            height=5,
            fg="black",
            command=lambda: controller.start_game()
        )
        self.button.pack()