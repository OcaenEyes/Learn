import tkinter
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
window = tkinter.Tk()
window.title('Just A Joker')
window.geometry('800x600')

var = tkinter.StringVar()
l=tkinter.Label(window,
                textvariable=var,
                bg='#70f3ff',
                font=('Arial',20),
                width=10,
                heigt=10,

                )
l.pack()


on_hit =False
def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('you hit me')
    else:
        on_hit =False
        var.set('')

b=tkinter.Button(window,
                 text='hit me',
                 command = hit_me,
                 )
b.pack()

window.mainloop()