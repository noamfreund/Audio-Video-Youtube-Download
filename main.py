from fileinput import filename
import os, sys
import speech_recognition as sr
from os import path
from pydub import AudioSegment

file_name = os.path.basename('./shay')
orig_song = os.path.splitext(file_name)[0]+'.ogg'
dest_song = os.path.splitext(file_name)[0]+'.wav'


def convert_ogg_to_wav():
    song = AudioSegment.from_ogg(orig_song)
    song.export(dest_song, format="wav")


def main():
    convert_ogg_to_wav()
    r = sr.Recognizer()
    # open the file
    with sr.AudioFile('shaked.wav') as source:
        # listen for the data (load audio to memory)
        audio_data = r.record(source)
        # recognize (convert from speech to text)
        text = r.recognize_google(audio_data)
        print(text)


if __name__ == "__main__":
    main()
