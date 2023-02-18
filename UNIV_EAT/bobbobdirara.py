import tkinter
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
import numpy as np
import datetime as dt
import calendar
from PIL import Image
import PIL.ImageTk
def gongdae():
    res_num = 85
    now = dt.datetime.today().weekday()
    label.config(text='점심:\n'+menu_select(res_num)[0][now]+'\n'+'\n'+'저녁:\n'+menu_select(res_num)[1][now])
def gpgam():
    res_num = 46
    now = dt.datetime.today().weekday()
    label.config(text='점심:\n'+menu_select(res_num)[0][now])
def welfare():
    res_num = 36
    now = dt.datetime.today().weekday()
    label.config(text='점심:\n'+menu_select(res_num)[0][now]) 
       
def menu_select(res_num):
    menu =[]
    html = urlopen(f'https://coop.knu.ac.kr/sub03/sub01_01.html?shop_sqno={res_num}')
    soup = BeautifulSoup(html.read(),'html.parser')
    x =  soup.select('tbody > tr > td> ul > li.first > p')
    for i in x:
        menu.append(i.text)
    menu = menu[:21:2]
    lunch_menu = menu[:5]
    dinner_menu = menu[5:]
    return lunch_menu, dinner_menu

window=tkinter.Tk()
window.title("밥밥디라라")
window.geometry("640x400+100+100")
window.resizable(False, False)
window.tk.call('wm', 'iconphoto', window._w, tkinter.PhotoImage(file='./bab.png'))
label=tkinter.Label(window, text="오늘의 식당메뉴를 확인하세요!", width=40, height=3, fg="black", relief="solid",font= 'D2Coding')
label.pack()

imageicon = PIL.ImageTk.PhotoImage(Image.open('./bab.png'))

labelicon = tkinter.Label(window, image=imageicon)
labelicon.pack()


# canvas = tkinter.Canvas(window, width=500, height=320, background='white')
# canvas.pack(padx=10, pady=10)
# canvas.create_rectangle(10, 5, 250, 310, outline='black', width=1)
# canvas.create_rectangle(260, 5, 490, 310, outline='black', width=1)
# frame1=tkinter.Frame(window, relief="groove", bd=3)
# frame1.pack(side="left", fill="both", expand=True)

button1 = tkinter.Button(window, overrelief="solid", width=15, command=gongdae,text = '공대식당', repeatdelay=1000, repeatinterval=100)
button1.pack()
button2 = tkinter.Button(window, overrelief="solid", width=15, command=gpgam,text = 'GP감꽃푸드코트',repeatdelay=1000, repeatinterval=100)
button2.pack()
button3 = tkinter.Button(window, overrelief="solid", width=15, command=welfare, text = '복지관 교직원식당',repeatdelay=1000, repeatinterval=100)
button3.pack()
quit_bnt = tkinter.Button(window, overrelief="solid", width=15, command=window.quit, text = '나가기',repeatdelay=1000, repeatinterval=100)
quit_bnt.pack()
label = tkinter.Label(window, text="메뉴생성",bg = 'white')
label.pack()
labelres=tkinter.Label(window, text="식당목록", width=10, height=2, fg="black",bg = 'white',relief='solid',font= 'D2Coding')
labelres.pack()
button1.place(x=85, y=160, relwidth=0.35)

button2.place(x=85, y=210, relwidth=0.35)
button3.place(x=85, y=260, relwidth=0.35)
quit_bnt.place(x=85, y=310, relwidth=0.35)
labelres.place(x=85,y=80,relwidth=0.35)
label.place(x=330, y=80, relwidth=0.35)
window.mainloop()




