#import numpy as np
import cv2 as c
import tkinter as t
from tkinter.filedialog import askopenfilename
from PIL import Image
from PIL import ImageTk
import imutils
class video_player :
     def __init__(self):
        self.m = t.Tk()
        self.m.title('Video Player')
        self.gui()
     def gui(self):
        menu=t.Menu(self.m)
        self.m.config(menu=menu)
        subM = t.Menu(menu)
        menu.add_cascade(label='Menu',menu=subM)
        subM.add_command(label="Open file",command= self.open_file)
        subM.add_command(label="Clear all history",command=self.open_file)
        subM.add_separator()
        subM.add_command(label="Exit",command=self.m.destroy)
        self.canvas = t.Canvas(self.m, width = 640, height = 480)
        self.canvas.pack()
        
     def open_file(self):
        self.filename = askopenfilename(initialdir = "C:/Users/gurpr/Documents/Dropbox",title = "Choose your Video File",filetypes = (("AVI files","*.avi"),("MP4 files","*.mp4"),("3Gp files","*.3gp"),("MKV files","*.mkv"),("all files","*.*")))
        self.vd=video_capture(self.filename)
        self.tot_frames=self.vd.vid.get(c.CAP_PROP_FRAME_COUNT)
        self.i=0
        self.delay=15
        self.w= t.Scale(self.m, from_=0, to=self.tot_frames,relief=t.RIDGE,length=600,tickinterval=int(self.tot_frames/20),orient=t.HORIZONTAL)
        self.w.pack(side=t.BOTTOM,pady=10)
        print(self.w)
        self.video_loop()
        c.destroyAllWindows()
     def video_loop(self):

         check,image=self.vd.get_frame()
         if (self.i%3==0):
             self.w.set(self.i)
         self.i=self.i+1
         #image = imutils.resize(image, width=640)
         self.pic = Image.fromarray(image)
         self.pic= ImageTk.PhotoImage(self.pic)
         self.canvas.create_image(0, 0, image =self.pic, anchor = t.NW)
         self.m.after(self.delay,self.video_loop)
        

class video_capture:
     def __init__(self, video_source=0):
         self.vid = c.VideoCapture(video_source)
         if not self.vid.isOpened():
             raise ValueError("Unable to open video source", video_source)
         self.width = self.vid.get(c.CAP_PROP_FRAME_WIDTH)
         self.height = self.vid.get(c.CAP_PROP_FRAME_HEIGHT)
 
     def get_frame(self):
       if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                 # Return a boolean success flag and the current frame converted to BGR
                return (ret, c.cvtColor(frame, c.COLOR_BGR2RGB))
            else:
                return (ret, None)
       else:
            return (ret, None)
     def __del__(self):
         if self.vid.isOpened():
             self.vid.release()
 
                
        
        
root = video_player()
root.m.mainloop()