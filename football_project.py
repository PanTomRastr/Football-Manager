from tkinter import *
from function import football_box, proverka
from PIL import ImageTk
import re

root = Tk()
image = ImageTk.PhotoImage(file="111.jpg")
root.title("Football")
root.geometry("800x500")

e = Entry(width=100)
b = Button(text="Статистика")
l = Label(bg='black', fg='white', width=100, height=20)
l1 = Label(bg='black', fg='white', width=100, height=20)
g = Button(text="Проверка")


def strToSortlist(event):
    s = e.get()
    s = s.split()
    for i in range(len(s)):
        s[i] = s[i].lower()
    if s == ['зенит']:
        a = football_box('http://wildstat.ru/p/7001/ch/all/club1/RUS_Terek_Groznyi/club2/RUS_Zenit_St_Petersburg')
        myString1 = ' '.join(a[0])
        myString2 = ' '.join(a[1])
        lst = []
        lst.append(myString1)
        lst.append(myString2)
        lst.append(a[2])
        l['text'] = '\n'.join(lst)
    else:
        l['text'] = 'нету комманд'


def chek(event):
    s = e.get()
    s = s.split()
    reg = re.compile('[^а-яА-Я ]')
    for i in range(len(s)):
        s[i] = s[i].lower()
        s[i] = reg.sub('', s[i])
    i = 0
    while i < len(s):
        if len(s[i]) == 0:
            del s[i]
        else:
            i += 1
    team1 = proverka(s[0], 0.67)
    team2 = proverka(s[1], 0.67)
    myString1 = ' '.join(team1)
    myString2 = ' '.join(team2)
    lst = []
    lst.append(myString1)
    lst.append(myString2)
    l['text'] = '\n'.join(lst)


b.bind('<Button>', strToSortlist)
g.bind('<Button>', chek)
e.pack()
b.pack()
l.pack()
g.pack()
root.mainloop()
