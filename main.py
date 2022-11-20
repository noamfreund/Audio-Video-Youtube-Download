from tkinter import ttk, messagebox, filedialog
import tkinter as tk
from tkinter import *
from pytube import YouTube


def Widgets():
    # === WIDGETS FOR TAB ONE
    firstLabelTabOne_Movie = tk.Label(tab1, text="Movie link :", bg="pale turquoise", pady=5, padx=5)
    secondLabelTabOne_Dest = tk.Label(tab1, text="Destination :", bg="pale turquoise", pady=5, padx=9)
    firstEntryTabOne_Movie = tk.Entry(tab1, width=30, textvariable=video_Link, font="Arial 12")
    secondEntryTabOne_Dest = tk.Entry(tab1, width=22, textvariable=download_Path, font="Arial 12")

    buttonBack = tk.Button(tab1, text="Exit", command=close, width=10, bg="grey", font="Georgia, 13")
    buttonBrowse = tk.Button(tab1, text="Browse", command=Browse, width=10, bg="pale turquoise", font="Georgia, 13")
    buttonDownload = tk.Button(tab1, text="Download", command=download, width=10, bg="light green", font="Georgia, 13")

    # === ADD WIDGETS TO GRID ON TAB ONE
    firstLabelTabOne_Movie.grid(row=0, column=0, padx=15, pady=15)
    firstEntryTabOne_Movie.grid(row=0, column=1, columnspan=2, sticky="E", padx=15, pady=15)
    secondLabelTabOne_Dest.grid(row=3, column=0, padx=5, pady=5)
    secondEntryTabOne_Dest.grid(row=3, column=1, padx=5, pady=5)
    buttonBack.grid(row=4, column=2, padx=1, pady=40)
    buttonBrowse.grid(row=3, column=2, padx=1, pady=10)
    buttonDownload.grid(row=4, column=0, padx=1, pady=40)

    # === WIDGETS FOR TAB TWO
    firstLabelTabTwo_Movie = tk.Label(tab2, text="Audio link :", bg="pale turquoise", pady=5, padx=5)
    secondLabelTabTwo_Dest = tk.Label(tab2, text="Destination :", bg="pale turquoise", pady=5, padx=9)
    firstEntryTabTwo_Movie = tk.Entry(tab2, width=30, textvariable=mp3_Link, font="Arial 12")
    secondEntryTabTwo_Dest = tk.Entry(tab2, width=22, textvariable=download_Path, font="Arial 12")

    buttonBack = tk.Button(tab2, text="Exit", command=close, width=10, bg="grey", font="Georgia, 13")
    buttonBrowse = tk.Button(tab2, text="Browse", command=Browse, width=10, bg="pale turquoise", font="Georgia, 13")
    buttonDownload = tk.Button(tab2, text="Download", command=download, width=10, bg="light green", font="Georgia, 13")

    # === ADD WIDGETS TO GRID ON TAB ONE
    firstLabelTabTwo_Movie.grid(row=0, column=0, padx=15, pady=15)
    firstEntryTabTwo_Movie.grid(row=0, column=1, columnspan=2, sticky="E", padx=15, pady=15)
    secondLabelTabTwo_Dest.grid(row=3, column=0, padx=5, pady=5)
    secondEntryTabTwo_Dest.grid(row=3, column=1, padx=5, pady=5)
    buttonBack.grid(row=4, column=2, padx=1, pady=40)
    buttonBrowse.grid(row=3, column=2, padx=1, pady=10)
    buttonDownload.grid(row=4, column=0, padx=1, pady=40)


def close():
    exit()


def download():
    if len(video_Link.get()) != 0:
        MovieDownload()
    else:
        AudioDownload()


def Browse():  # Paste your Destination Folder here
    download_Directory = filedialog.askdirectory(
        initialdir="C:", title="Save Video")

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


form = tk.Tk()
form.title("Audio/Video-download/convert")
form.geometry("450x240")
tab_parent = ttk.Notebook(form)
tab_parent.pack(expand=1, fill='both')

# All the different tabs and their names
tab1 = ttk.Frame(tab_parent)
tab2 = ttk.Frame(tab_parent)
tab_parent.add(tab1, text="Movie")
tab_parent.add(tab2, text="Audio")
video_Link = StringVar()
mp3_Link = StringVar()
download_Path = StringVar()

Widgets()
form.mainloop()
