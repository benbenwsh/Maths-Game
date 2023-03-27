import tkinter as tk
from maths_game import MathsGame
from audio_manager import AudioManager as am

class ResultFrame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # paddings, centering,
        self.correct_label = tk.Label(self, text="haha", font=("Roboto", 57))
        self.correct_label.pack(fill=None, expand=True)


    def correct(self):
        def end_method():
            self.controller.show_frame(MathsGame)
            self.controller.frames[MathsGame].correct()

        self.configure(bg="#04F06A")
        self.correct_label.configure(text="CORRECT", bg="#04F06A")

        self.controller.after(1000, end_method)

    def incorrect(self):
        def end_method():
            self.controller.show_frame(MathsGame)
            self.controller.frames[MathsGame].incorrect()

        self.configure(bg="#F24236")
        self.correct_label.configure(text="INCORRECT", bg="#F24236")

        self.controller.after(1000, end_method)


    def incorrect_last_attempt(self, text):
        def end_method():
            answer_label.destroy()
            next_question_button.destroy()
            self.controller.show_frame(MathsGame)
            self.controller.frames[MathsGame].correct()

        self.configure(bg="#F24236")
        self.correct_label.configure(text=text, bg="#F24236")

        answer_label = tk.Label(self, text="Answer: answer", font=("Roboto", 22), bg="#F24236")
        answer_label.pack()

        next_question_button = tk.Button(self, text="Next Question", font=("Roboto", 14), bg="#F24236", command=end_method, state="disabled")
        next_question_button.pack()

        duration = am.play_audio()

        def enable_button():
            next_question_button.configure(state="normal")

        self.controller.after(duration, enable_button)
