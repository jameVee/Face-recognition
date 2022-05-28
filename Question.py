from tkinter import *
from  tkinter import ttk , messagebox
import facedetect
from datetime import datetime
import sqlite3

con = sqlite3.connect('data_stu.db')
cur = con.cursor()
number = 0
def btcheck_click():
    global number
    Q = facedetect.face_detect()
    mb = messagebox.askyesno('accept',f'YOU ARE {Q}?')
    if mb == True:
        sql = 'UPDATE student SET status = ? WHERE Number = ?'
        cur.execute(sql,['ARRVIED',Q])
        con.commit()
        number += 1
        Labelt.config(text=f'จำนวนคนเข้าเรียน {number} คน')
    else:
       btcheck_click()

def reset_click():
    sql = 'UPDATE student SET status = ? WHERE status = ? '
    cur.execute(sql,['NULL','ARRVIED'])
    con.commit()
    print('DONE')




def t():
    global ti
    ti = datetime.now().time()
    ti_f = ti.strftime('%H:%M:%S')
    Labelt.config(text=ti_f)
    Labelt.after(1000,t)



windows = Tk()
windows.title('โอเคซึ้ง')
ws = windows.winfo_screenwidth()
hs = windows.winfo_screenheight()
x = (ws/2) - (700/2)
y = (hs/2) - (500/2)
windows.geometry(f'750x500+{x:.0f}+{y:.0f}')
frame = Frame(windows,bg='lightgray')
frame.place(x=250,y=100)

label = Label(frame,text='Click for check name',font='Harrington 20')
label.pack(ipady=50,expand=YES)

Labelt = Label(frame,font='times 16')
Labelt.pack()

button = ttk.Button(frame,text='click',command= lambda : btcheck_click())
button.pack(ipady=10,expand=YES)



#reset = ttk.Button(frame,text='reset',command= lambda : reset_click())
#reset.pack()
t()
mainloop()
