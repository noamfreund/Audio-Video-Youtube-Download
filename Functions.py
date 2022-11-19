# Importing necessary packages
from pytube import YouTube
from tkinter import messagebox, filedialog
import tkinter as tk
from tkinter import *


def close():
    exit()


def download():

    MovieDownload()


def Browse():  # Paste your Destination Folder here
    download_Directory = filedialog.askdirectory(
        initialdir="E:/1-my folders/movies/", title="Save Video")

    download_Path.set(download_Directory)


def MovieDownload():
    Youtube_link = video_Link.get()
    download_Folder = download_Path.get()
    getVideo = YouTube(Youtube_link)
    videoStream = getVideo.streams.filter()
    videoStream.get_highest_resolution().download(download_Folder)
    messagebox.showinfo("SUCCESSFULLY",
                        "DOWNLOADED AND SAVED IN\n" + download_Path)


def AudioDownload():
    Youtube_link = mp3_Link.get()
    download_Folder = download_Path.get()
    getVideo = YouTube(Youtube_link)
    videoStream = getVideo.streams.filter()
    videoStream.get_highest_resolution().download(download_Folder)
    messagebox.showinfo("SUCCESSFULLY",
                        "DOWNLOADED AND SAVED IN\n"
                        + download_Folder)
