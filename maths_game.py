import tkinter as tk
import random
from maths_expression_generator import MathsExpressionGenerator as meg
from audio_manager import AudioManager as am

class MathsGame(tk.Frame):

    EXPRESSION_TYPES = [
        meg.addition,
        meg.subtraction,
        meg.multiplication,
        meg.division
    ]

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.curr_expression = ""
        self.curr_answer = ""
        self.last_attempt = False
        self.question_no = 0

        # GUI
        # Bug: The frames did not stack on top of each other because I forgot to put self here
        self.question_no_label = tk.Label(self, text=self.question_no)
        self.question_no_label.pack()

        # Helper function
        def validate(value):
            return str.isdigit(value) or value == ""

        vcmd = (self.register(validate), "%P")
        self.entry = tk.Entry(
            self,
            width=50,
            validate="key",
            validatecommand=vcmd
        )
        self.entry.bind("<Return>", self.check_answer)
        self.entry.pack()

        self.bottom_button = tk.Button(self, text="Try Again", command=self.incorrect)
        self.bottom_button.pack()


    def check_answer(self, event=None):
        # What happens if user did not enter no
        response = self.entry.get()
        if response != "":
            response = int(self.entry.get())

            self.controller.show_result(response == self.curr_answer, self.last_attempt)


    def correct(self):
        self.last_attempt = False
        self.question_no += 1

        self.question_no_label.configure(text=self.question_no)
        self.bottom_button.configure(command=self.incorrect)
        self.bottom_button.configure(text="Try Again")

        self.curr_expression, self.curr_answer = random.choice(self.EXPRESSION_TYPES)()
        print(self.curr_answer)
        am.create_audio(self.curr_expression)
        self.reset_ui_and_play_audio()


    def incorrect(self):
        def give_up_command():
            self.controller.show_result(False, self.last_attempt, ":(")

        self.last_attempt = True
        self.bottom_button.configure(text="Give Up :(", command=give_up_command)
        self.reset_ui_and_play_audio()


    def reset_ui_and_play_audio(self):
        self.entry.delete(0, tk.END)
        self.entry.configure(state="disabled")
        self.bottom_button.configure(state="disabled")

        duration = am.play_audio()

        def enable_entry():
            self.entry.configure(state="normal")
            self.bottom_button.configure(state="normal")

        self.controller.after(duration, enable_entry)