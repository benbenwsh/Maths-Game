import tkinter as tk
from start_frame import StartFrame
from maths_game import MathsGame

# Trim whitespaces and other stuffs
class Window(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.wm_title("Maths Game")

        container = tk.Frame(self, height=400, width=600)
        # specifying the region where the frame is packed in root
        container.pack(side="top", fill="both", expand=True)

        # configuring the location of the container using grid
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartFrame, MathsGame):
            frame = F(container, self)

            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartFrame)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def start_game(self):
        self.show_frame(MathsGame)
        self.frames[MathsGame].next_question()

if __name__ == "__main__":
    window = Window()
    window.mainloop()