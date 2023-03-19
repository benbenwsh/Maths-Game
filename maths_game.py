import tkinter as tk
from gtts import gTTS
import random
from playsound import playsound
from maths_expression_generator import MathsExpressionGenerator as meg
from mutagen.mp3 import MP3


class MathsGame(tk.Frame):
    EXPRESSION_TYPES = [
        meg.addition,
        meg.subtraction,
        meg.multiplication,
        meg.division()
    ]

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.curr_expression = ""
        self.curr_answer = ""
        self.last_attempt = False

        # GUI
        # Bug: The frames did not stack on top of each other because I forgot to put self here
        self.correct_label = tk.Label(self, text="")
        self.correct_label.pack()

        # Remove button after game has started, or do similar actions (e.g. turn it into an end game button)
        # Disable this field when the mp3 is playing, but no colour wheel thingy when playing sound


        vcmd = (self.register(self.validate), "%P")
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

        self.answer_label = tk.Label(self, text="")
        self.answer_label.pack()


    def validate(self, value):
        return str.isdigit(value) or value == ""

    def play_audio(self):
        playsound("expression.mp3", False)

    def create_audio(self, speech):
        tts = gTTS(speech, lang="en-us")
        tts.save("expression.mp3")
        self.audio = MP3("expression.mp3")

    def enable_entry(self):
        self.entry.configure(state="normal")
        self.bottom_button.configure(state="normal")

    def check_answer(self, event=None):
        # What happens if user did not enter no
        response = int(self.entry.get())

        if response == self.curr_answer:
            self.correct()
        else:
            self.incorrect()

    def correct(self):
        print("correct")
        self.correct_label.configure(text="Correct:)")
        self.next_question()

    def next_question(self):
        self.last_attempt = False

        self.bottom_button.configure(command=self.incorrect)
        self.bottom_button.configure(text="Try Again")
        self.answer_label.configure(text="")

        self.curr_expression, self.curr_answer = random.choice(self.EXPRESSION_TYPES)()
        print(self.curr_answer)
        self.create_audio(self.curr_expression)
        self.reset_ui_and_play_audio()

    def incorrect(self):
        if self.last_attempt:
            self.show_answer()
        else:
            self.last_attempt = True
            self.correct_label.configure(text="Incorrect:(")
            self.bottom_button.configure(text="Give Up :(")
            self.reset_ui_and_play_audio()

    def reset_ui_and_play_audio(self):
        self.entry.delete(0, tk.END)
        self.entry.configure(state="disabled")
        self.bottom_button.configure(state="disabled")

        self.play_audio()
        self.controller.after(int(self.audio.info.length * 1000), self.enable_entry)

    def show_answer(self):
        # Disable button or hide it
        self.last_attempt = False
        self.answer_label.configure(text=f"Answer: {self.curr_answer}")
        self.bottom_button.configure(text="Next Question", command=self.next_question)
        self.reset_ui_and_play_audio()