# Importing necessary packages
from pytube import YouTube
from tkinter import messagebox, filedialog


video_Link = ""
mp3_Link = ""
download_Path = ""

def close():
    exit()


def download():
    if len(video_Link.get()) != 0:
        MovieDownload()
    else:
        AudioDownload()


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
                        "DOWNLOADED AND SAVED IN\n"
                        + download_Folder)


def AudioDownload():
    Youtube_link = mp3_Link.get()
    download_Folder = download_Path.get()
    getVideo = YouTube(Youtube_link)
    videoStream = getVideo.streams.filter()
    videoStream.get_highest_resolution().download(download_Folder)
    messagebox.showinfo("SUCCESSFULLY",
                        "DOWNLOADED AND SAVED IN\n"
                        + download_Folder)
