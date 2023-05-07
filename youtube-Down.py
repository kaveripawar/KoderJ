
import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import messagebox,filedialog
root=tk.Tk()
root.geometry("500x300")
root.resizable(4,4)
root.title("yt dl")
root.config(background="palegreen1")
video_Link=StringVar()
download_Path=StringVar()

def Widgets():
    title=Label(root,text="youtube downloader using tkinter",padx=15,
                pady=15,fg="red",bg="green")
    title.grid(row=1,column=1,padx=5,pady=5,columnspan=1)
    
    link=Label(root,text="yt link",bg="salmon",padx=5,pady=5)
    link.grid(row=2,column=1,pady=5,padx=5,columnspan=2)
    #linklable
    [[]]
    #destination
    D_lable=Label(root,text="destination",bc="salmon",padx=5,pady=5)
    D_lable.grid(row=3,column=0,pady=5,padx=5)
    #destination text
    root
    
def Browse():
    download_Directory=filedialog.askdirectory(initialdir="your directory path",title="save video")
    download_Path.Set(download_Directory)
def Download():
    youtube_link=video_Link.get()
    download_Folder=download_Path.get()
    getVideo=YouTube(youtube_link)
    videoStream=getVideo.streams.first()
    videoStream.download(download_Folder)
    messagebox.showinfo("Successfully","dounloaded and saved"+download_Folder)
    
Widgets()   
root.mainloop()

