from pydub import AudioSegment
import os; print(os.environ["PATH"].split(os.pathsep))

def soma():

    audio1 = AudioSegment.from_wav("coin.wav")
    audio2 = AudioSegment.from_wav("audio.wav")
    audio2 = audio2 + audio1

    audio2.export("soma.wav", format="wav")

def multi():
    audio1 = AudioSegment.from_wav("coin.wav")
    audio2 = AudioSegment.from_wav("audio.wav")

    audio2 = audio2 * audio1

    audio2.export("multi.wav", format="wav")

def lowpass():
    song = AudioSegment.from_wav("audio.wav")
    song = song.low_pass_filter(5000)
    song.export("lowpass.wav", format="wav")

def highpass():
    song2 = AudioSegment.from_wav("audio.wav")
    song2 = song2.high_pass_filter(5000)
    song2.export("highpass.wav", format="wav")
