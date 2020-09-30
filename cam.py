import ctypes
#qqqimport time
import cv2 as c
user32 = ctypes.windll.User32
class secureMe:
    def __init__(self):
        self.cap=None
        self.fourcc=None
        while True:
            print(self.isLocked())
            if self.isLocked()==True and self.cap!=None:
                pass
            elif (self.isLocked()==False and self.cap!=None):
                pass
            elif (self.isLocked()==True):
                self.webone()
    def isLocked(self):
        return user32.GetForegroundWindow() == 0
    def webone(self):
        self.cap=c.VideoCapture(0)
        self.fourcc=c.VideoWriter_fourcc(*'MJPG')
        self.out = c.VideoWriter('output1.avi',self.fourcc,20.0,(640,480))
        while True:
            check,frame=self.cap.read()
            #gray=c.cvtColor(frame,c.COLOR_BGR2GRAY)
            print('recording')
            self.out.write(frame)
            c.imshow('capturing',frame)
            if c.waitKey(1) & 0xFF==ord('q'):
                break
            print(self.isLocked())
            if self.isLocked()==True and self.cap!=None:
                pass
            elif (self.isLocked()==False and self.cap!=None):
                pass
            elif (self.isLocked()==True):
                self.webone()
        self.cap.release()
        self.out.release()
        c.destroyAllWindows()


s=secureMe()
