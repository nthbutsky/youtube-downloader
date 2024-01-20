import tkinter as tk
import customtkinter as ctk
from pytube import YouTube

def startDownload():
  try:
    ytlink = link.get()
    ytObject = YouTube(ytlink, on_progress_callback = on_progress)
    video = ytObject.streams.get_lowest_resolution()
    title.configure(text = ytObject.title, text_color = 'white')
    finishLabel.configure(text = '')
    show_progress_elements()
    video.download()
    finishLabel.configure(text = 'Download completed', text_color = 'green')
  except:
    finishLabel.configure(text = 'Download Error', text_color = 'red')

def on_progress(stream, chunk, bytes_remaining):
  total_size = stream.filesize
  bytes_downloaded = total_size - bytes_remaining
  percentage_of_completion = bytes_downloaded / total_size * 100
  per = str(int(percentage_of_completion))
  progressInfo.configure(text = per + '%')
  progressInfo.update()

  progressBar.set(float(percentage_of_completion) / 100)

def show_progress_elements():
  progressInfo.pack()
  progressBar.pack(padx = 10, pady = 10)

# system settings
ctk.set_appearance_mode('system')
ctk.set_default_color_theme('blue')

# main window
app = ctk.CTk()
app.geometry('720x280')
app.title('YouTube Downloader')

# ui elements
title = ctk.CTkLabel(app, text='Insert a youtube link')
title.pack(padx = 10, pady = 10)

url_var = tk.StringVar()
link = ctk.CTkEntry(app, width = 350, height = 40, textvariable = url_var)
link.pack()

finishLabel = ctk.CTkLabel(app, text='')
finishLabel.pack()

progressInfo = ctk.CTkLabel(app, text='0%')

progressBar = ctk.CTkProgressBar(app, width=400)
progressBar.set(0)

downloadBtn = ctk.CTkButton(app, text='Download', command = startDownload)
downloadBtn.pack(padx = 10, pady = 10)

# app running
app.mainloop()