# Importing necessary packages
import tkinter as tk
from tkinter import *
from tkinter import ttk
from pytube import YouTube
from tkinter import messagebox, filedialog

from Functions import Browse,download,close


def Widgets():

    link_label_movie = Label(root,
                             text="Movie link :",
                             bg="pale turquoise",
                             pady=5,
                             padx=5)
    link_label_movie.grid(row=2,
                          column=0,
                          pady=5,
                          padx=5)

    link_label_mp3 = Label(root,
                           text="mp3 link :",
                           bg="pale turquoise",
                           pady=5,
                           padx=5)
    link_label_mp3.grid(row=3,
                        column=0,
                        pady=5,
                        padx=5)

    root.linkText = Entry(root,
                          width=30,
                          textvariable=video_Link,
                          font="Arial 14")
    root.linkText.grid(row=2,
                       column=1,
                       pady=5,
                       padx=5,
                       columnspan=2)

    root.linkText = Entry(root,
                          width=30,
                          textvariable=mp3_Link,
                          font="Arial 14")
    root.linkText.grid(row=3,
                       column=1,
                       pady=5,
                       padx=5,
                       columnspan=2)

    destination_label = Label(root,
                              text="Destination :",
                              bg="pale turquoise",
                              pady=5,
                              padx=9)
    destination_label.grid(row=4,
                           column=0,
                           pady=5,
                           padx=5)

    root.destinationText = Entry(root,
                                 width=27,
                                 textvariable=download_Path,
                                 font="Arial 12")
    root.destinationText.grid(row=4,
                              column=1,
                              pady=5,
                              padx=5)

    browse_B = Button(root,
                      text="Browse",
                      command=Browse,
                      width=10,
                      bg="blue",
                      relief=GROOVE)
    browse_B.grid(row=4,
                  column=2,
                  pady=1,
                  padx=1)

    Download = Button(root,
                      text="Download ",
                      command=download,
                      width=15,
                      bg="pale turquoise",
                      pady=0,
                      padx=0,
                      relief=GROOVE,
                      font="Georgia, 13")
    Download.grid(row=5,
                  column=0,
                  pady=1,
                  padx=1)

    exit_1 = Button(root,
                    text="Exit",
                    command=close,
                    width=5,
                    bg="pale turquoise",
                    pady=0,
                    padx=0,
                    # relief=GROOVE,
                    font="Georgia, 13")
    exit_1.grid(row=5,
                column=2,
                pady=1,
                padx=1)



root = tk.Tk()
root.geometry("520x280")
root.resizable(False, False)
root.title("YouTube Video Downloader")
root.config(background="grey")


video_Link = StringVar()
mp3_Link = StringVar()
download_Path = StringVar()
Widgets()
root.mainloop()
