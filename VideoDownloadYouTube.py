# importing the module
from pytube import YouTube

SAVE_PATH = "E:/1-my folders/movies/"
link="https://www.youtube.com/watch?v=wJjzVvmUdb4"

try:
	yt = YouTube(link)
except:
	print("Connection Error")

mp4files = yt.streams.filter()

try:
	mp4files.get_highest_resolution().download(SAVE_PATH)
except:
	print("Some Error!")

print('Task Completed!')
