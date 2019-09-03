# coding=utf-8
# Author:Tommy_Sea
# Time:2019-9
'''

'''
from tkinter import *
from PIL import ImageTk
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


def Text_Prompt():
    'The whole is divided into two frames, \
    one is a text prompt and the other is a button function, \
    so two frames should be used.'

    # Here is the codes of text prompt.
    var.set("万里晴空!\n情寄草原！")  # Here is the value of text,the type is StringVar.
    # The textvariable is different from text, it will show a variable whose type is 'StringVar'.
    # We can set is via the ver.set().
    Text_label = Label(frame_text,
                       textvariable=var,
                       justify=LEFT,
                       fg='black',
                       image=photo,
                       compound=CENTER,
                       font=('华文行楷', 40)
                       )
    Text_label.pack()


# Here is the codes of button.
def Button_frame():
    The_Button = Button(frame_button,
                        text='Follow your heart！',
                        fg='black',
                        font=('华文楷体',40),
                        command = Go_now
                        )
    The_Button.pack()


if __name__ == '__main__':
    root = Tk()  # Creat the window
    var = StringVar()  # Set the textvariable
    # Get the photo here, or we cann't see the photo there.
    photo = ImageTk.PhotoImage(file=r"I:\Learning_of_Python\pictures\glass.jpg")  # Get the picture here

    frame_text = Frame(root)  # This is the frame of text prompt.
    frame_button = Frame(root)  # This is the frame of button.

    Text_Prompt()  # Get the Text_Prompt
    Button_frame()  # Get the Button_frame

    frame_text.pack(padx=10, pady=10)
    frame_button.pack(padx=10, pady=10)
    root.mainloop()
