from tkinter import *
from pywebio import *
from pywebio.input import *
from pywebio.output import *
from pywebio import start_server
from pywebio import config
import webbrowser
app =Tk()
app.geometry('1000x600+200+50')
app.title('AMIR')
#app.iconbitmap('images/my.icon')
app.configure(background='whitesmoke')


def facebook():
  

    url ='https://www.facebook.com/'
 
    webbrowser.open(url)

def Tiktok():
    
    url ='https://www.tiktok.com/'
 
    webbrowser.open(url)
def instagram():    

    url ='https://www.instagram.com/'
 
    webbrowser.open(url)
def telgram():
        
   url ='https://www.telegram.com/'
    #gram.com/'
 
   webbrowser.open(url)

title1 = Label (app , text='تطبيقات اجتماعيه',
                fg='black',bg='white',
                font=('courier',16)
               )
title1.pack(fill=X)  

logo =PhotoImage(file='images/logo1.png')   
pan =Label(app,image=logo,bg='whitesmoke')
pan.place(x=240,y=85,width=700,height=400)

title2 = Label (app , text='تطبيقات التواصل الاجتماعي اجتماعيه',
                fg='black',bg='whitesmoke',
                font=('courier',26,'bold')
               )
title2.place(x=290,y=520)

side = Frame(app , width=180,height=590,bg='white',bd=0,relief=GROOVE)
side.place(x=0,y=24)

side_title1 =Label(side,text='امير مبارك',fg='black',font=('courier',13))
side_title1.place(x=5,y=10)

amir = PhotoImage(file='images/amir1.png')

face = PhotoImage(file='images/fac.png')
tik  = PhotoImage(file='images/tik.png')
insta = PhotoImage(file='images/insta.png')
tal = PhotoImage(file='images/tel.png')

B= Button(side ,
          text='مبارك عواده',
          cursor='hand2',
          image= amir,
          compound =TOP,
          width=130,
          #height=50,
          bd=0,
          relief=RIDGE,
          bg='white'
          )
B.place(x=25,y=50)

side_title2=Label(side,text='social app',fg='black',bg='white',font=('courier',13))
side_title2.place(x=35,y=220)

B1 =Button(side ,text='FACE BOOK',cursor='hand2',image=face , width=130 , compound=TOP ,bd=0 , bg='white' ,relief=RIDGE , command=facebook)
B1.place(x=20,y=250)

B2 =Button(side ,text='TIKTOK',cursor='hand2',image=tik , width=130 , compound=TOP ,bd=0 , bg='white' ,relief=RIDGE,command=Tiktok)
B2.place(x=20,y=330)

B3 =Button(side ,text='INASTIGRAM',cursor='hand2',image=insta , width=130 , compound=TOP ,bd=0 , bg='white' ,relief=RIDGE,command=instagram)
B3.place(x=20,y=400)

B4 =Button(side ,text='TALGRAM',cursor='hand2',image=tal , width=130 , compound=TOP ,bd=0 , bg='white' ,relief=RIDGE,command=telgram)
B4.place(x=20,y=480)


app.mainloop()