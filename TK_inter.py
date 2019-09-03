# coding=utf-8
# Author:Tommy_Sea
# Time:2019-9
'''

'''
from tkinter import *
from PIL import Image, ImageTk
#——————————————————————————————————————————————————————————————————————————————————————————————————
# app = tk.Tk()
# app.title('Tommy_Sea')
# theLable = tk.Label(app,text = 'This is the second one')#文本与图标
# theLable.pack()#自动调节组件之间的位置与大小
# app.mainloop()
#——————————————————————————————————————————————————————————————————————————————————————————————————

# class App():
#     def __init__(self,master):
#         frame = tk.Frame(master)
#         frame.pack(side = tk.LEFT,padx = 100,pady = 200)
#         self.tick = tk.Button(frame,text = '点我有惊喜！',
#                               fg='blue',bg='pink',
#                               command=self.hello)
#         self.tick.pack()
#
#     def hello(self):
#         print("Hello every one.")
#
#
# root = tk.Tk()
# app = App(root)
#
# root.mainloop()
#——————————————————————————————————————————————————————————————————————————————————————————————————

# root = Tk()#生成一个root窗口
#
# textLabel = Label(root, text = 'Something \nis Here!',justify = LEFT,padx=10)#左对齐，边距为10
# textLabel.pack(side = LEFT)
# photo = ImageTk.PhotoImage(file = r"I:\Learning_of_Python\pictures\ink.jpg")
# imgLabel = Label(root, image = photo)
# imgLabel.pack()
#
# mainloop()
#——————————————————————————————————————————————————————————————————————————————————————————————————

def Go_now():
    'This is the function of button command.'
    var.set("Where would you wanna go?")

def Home_page():
    'The whole is divided into two frames, \
    one is a text prompt and the other is a button function, \
    so two frames should be used.'
    frame1 = Frame(root)#This is the frame of text prompt
    frame2 = Frame(root)#This is the frame of button of function

    #Here is the codes of text prompt.
    photo = ImageTk.PhotoImage(file=r"I:\Learning_of_Python\pictures\glass.jpg")#Get the picture here
    var.set("万里晴空!\n情寄草原！")#Here is the value of text,the type is StringVar.
    #The textvariable is different from text, it will show a variable whose type is 'StringVar'.
    #We can set is via the ver.set().
    theLabel = Label(frame1,
                     textvariable=var,
                     justify=LEFT,
                     fg='black',
                     image=photo,
                     compound=CENTER,
                     font=('华文行楷', 40)
                     )

    #Here is the codes of button.
    theButton = Button(frame2,
                       text='现在出发！',
                       command=Go_now)
    
    theLabel.pack()
    theButton.pack()
    frame1.pack(padx=10, pady=10)
    frame2.pack(padx=10, pady=10)


root = Tk()
var = StringVar()
Home_page()
root.mainloop()
