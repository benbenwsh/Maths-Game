from gtts import gTTS
from playsound import playsound
from mutagen.mp3 import MP3

class AudioManager:

    # Returns the time of the audio
    @staticmethod
    def play_audio():
        playsound("expression.mp3", False)
        return int(MP3("expression.mp3").info.length * 1000)

    @staticmethod
    def create_audio(speech):
        tts = gTTS(speech, lang="en-us")
        tts.save("expression.mp3")
