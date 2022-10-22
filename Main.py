import tkinter as tk
from tkinter import filedialog
from pytube import YouTube
import os
u_name = os.getlogin()
def Download_Video():
    url = YouTube(str(link.get()))
    video = url.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    try:
        a =filedialog.askdirectory() 
        if a=="":
            a = f"C:\\Users\\{u_name}\\Videos\\YourTube-video-Downloader\\"   
        video.download(a)
        tk.Label(window, text = 'Your Video is downloaded!', font = 'arial 15',fg="White",bg="#EC7063").place(x= 10 , y = 140)  
    except Exception as e:
        print("error ")
        print("error ")
        print("error ")
        print("error ")
        print("error ")
        print(e)

window = tk.Tk()
window.geometry("600x400")
window.config(bg="#EC7063")
window.resizable(width=False,height=False)
window.title('YouTube Video Downloader')
link = tk.StringVar()
tk.Label(window,text = '                   Youtube Video Downloader                    ', font ='arial 20 bold',fg="White",bg="#EC7063").pack()
tk.Label(window, text = 'Enter the link of youtube video ', font = 'arial 20 bold',fg="Black",bg="#EC7063").place(x= 5 , y = 60)
link_enter = tk.Entry(window, width = 53,textvariable = link,font = 'arial 15 bold',bg="lightgreen").place(x = 5, y = 100)
tk.Button(window,text = 'DOWNLOAD', font = 'arial 15 bold' ,fg="white",bg = 'black', padx = 2,command=Download_Video).place(x=400 ,y = 142)
window.mainloop()
