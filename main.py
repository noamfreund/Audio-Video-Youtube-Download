import subprocess
from fileinput import filename
import os, sys
import speech_recognition as sr
from os import path
from pydub import AudioSegment

file_name = os.path.basename('shoko.ogg')
dest_song = os.path.splitext(file_name)[0] + '.wav'


def convert_ogg_to_wav():

    orig_song = os.path.splitext(file_name)[0] + '.ogg'
   # subprocess.call(['ffmpeg', '-i', file_name, dest_song])
    song = AudioSegment.from_ogg(orig_song)
    song.export(dest_song, format="wav")

def convert_mp3_to_wav():

    subprocess.call(['ffmpeg', '-i', file_name,  dest_song])

def convert_wav_to_wav():
    orig_song = os.path.splitext(file_name)[0] + '.wav'
    song = AudioSegment.from_wav(orig_song)
    song.export(dest_song, format="wav")


def main():

    if file_name == '*.wav':
        print("wav")
        convert_wav_to_wav()
    elif file_name == '*.ogg':
        print("ogg")
        convert_ogg_to_wav()
    elif file_name == '*.mp3':
        print("mp3")
        convert_mp3_to_wav()
    else:
        print("Format of File Unknown")
        exit()
    r = sr.Recognizer()
    # open the file
    with sr.AudioFile(dest_song) as source:
        # listen for the data (load audio to memory)
        audio_data = r.record(source)
        # recognize (convert from speech to text)
        text = r.recognize_google(audio_data)
        print(text)


if __name__ == "__main__":
    main()
