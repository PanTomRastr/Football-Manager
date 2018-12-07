import tkinter as tk
from tkinter import ttk
from function import  football_box, proverka, chek, sait, music, open_game_now, open_game_club
import requests, bs4
import playsound
import threading
import random
from pingpong import  *

t = threading.Thread(target=music, name='Thread1')

class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.text = ''

    def init_main(self):

        toolbar = tk.Frame(bg='#d7d8e0', bd=2)
        toolbar.pack(side=tk.TOP,fill=tk.X)

        self.flag = False
        self.add_img = tk.PhotoImage(file="soccer-game.png")
        self.add_img2 = tk.PhotoImage(file="football.png")
        self.add_img3 = tk.PhotoImage(file="schedule.png")
        self.add_img4 = tk.PhotoImage(file="strategy.png")
        self.add_img5 = tk.PhotoImage(file="foosball.png")
        self.add_img6 = tk.PhotoImage(file="music-player.png")

        btn_open_dialog = tk.Button(toolbar, text='Сравните команды', command=self.open_dialog, bg='#d7d8e0', bd=0,
                                    compound=tk.TOP, image=self.add_img)
        btn_open_dialog.pack(side=tk.LEFT)

        btn_open_game = tk.Button(toolbar, text='Последние игры 2-х комманд', command=self.open_game, bg='#d7d8e0',
                                  bd=0, compound=tk.TOP, image=self.add_img2)
        btn_open_game.pack(side=tk.LEFT)

        btn_open_game_now = tk.Button(toolbar, text='Последние игры клубов', command=self.open_year_club, bg='#d7d8e0',
                                  bd=0, compound=tk.TOP, image=self.add_img3)
        btn_open_game_now.pack(side=tk.LEFT)

        btn_open_club = tk.Button(toolbar, text='Игры между странами', command=self.open_year, bg='#d7d8e0',
                                      bd=0, compound=tk.TOP, image=self.add_img4)
        btn_open_club.pack(side=tk.LEFT)

        btn_open_pinpong = tk.Button(toolbar, text='Мини игра', command=self.open_ping, bg='#d7d8e0',
                                     bd=0, compound=tk.TOP, image=self.add_img5)
        btn_open_pinpong.pack(side=tk.LEFT)

        btn_open_music = tk.Button(toolbar, text='музыка', command=self.open_music, bg='#d7d8e0',
                                  bd=0, compound=tk.TOP, image=self.add_img6)
        btn_open_music.pack(side=tk.LEFT)

        self.label_teams = tk.Label(bg='black', fg='white', width=182, height=15, text= 'Добро пожаловать в ' + '\n' +
                                                                                        'football manager 2018')
        self.label_teams.pack()

    def open_dialog(self):
        Child(self)

    def open_game(self):
        Game(self)

    def open_year(self):
        Year(self)

    def open_year_club(self):
        Year_club(self)

    def open_ping(self):
        if self.flag:
            self.tree1.destroy()
            self.tree2.destroy()
            flag = False
        c.pack()
        main()

    def print_text(self):
        self.flag = True
        football_teams = self.text.split()
        football_teams = chek(football_teams)
        if len(football_teams) != 2:
            global1 = 'Нету комманд'
            self.label_teams['text'] = global1
        else:
            global1 = sait(football_teams[0], football_teams[1])

        if len(football_teams) == 2 and global1 != 'Нету комманд':

            self.label_teams['text'] = '\n'.join(football_teams)
            self.tree1 = ttk.Treeview(self, columns=('ID'))
            self.tree1.column("ID", width=440, anchor=tk.CENTER)

            self.tree1.insert('', '0', 'item1', text='Игры')
            self.tree1.insert('', '1', 'item2', text='Победы')
            self.tree1.insert('', '2', 'item3', text='Ничьи')
            self.tree1.insert('', '3', 'item4', text='Проигрыши')

            self.tree1.pack(side=tk.LEFT)

            self.tree2 = ttk.Treeview(self, columns=('ID'))
            self.tree2.column("ID", width=440, anchor=tk.CENTER)

            self.tree2.insert('', '0', 'item1', text='Игры')
            self.tree2.insert('', '1', 'item2', text='Победы')
            self.tree2.insert('', '2', 'item3', text='Ничьи')
            self.tree2.insert('', '3', 'item4', text='Проигрыши')

            self.tree2.pack(side=tk.LEFT)

            self.tree1.heading("ID", text=global1[0][0])
            self.tree2.heading("ID", text=global1[1][0])

            self.tree1.set('item1', 'ID', global1[0][1][0])
            self.tree1.set('item2', 'ID', global1[0][1][1])
            self.tree1.set('item3', 'ID', global1[0][1][2])
            self.tree1.set('item4', 'ID', global1[0][1][3])

            self.tree2.set('item1', 'ID', global1[1][1][0])
            self.tree2.set('item2', 'ID', global1[1][1][1])
            self.tree2.set('item3', 'ID', global1[1][1][2])
            self.tree2.set('item4', 'ID', global1[1][1][3])

    def print_game(self):
        football_teams = self.text.split()
        football_teams = chek(football_teams)

        if len(football_teams) != 2:
            global1 = 'Нету комманд'
            self.label_teams['text'] = global1
        else:
            global1 = sait(football_teams[0], football_teams[1])
            show_Game(self, var=global1)

    def print_year(self):
        football_year = self.text
        if football_year == '2019':
            global1 = open_game_club('http://wildstat.ru/p/60/ch/WRL_FR_2019/stg/all/tour/all')
            Game_club(self, var=global1)

        if football_year == '2018':
            global1 = open_game_club('http://wildstat.ru/p/6')
            Game_club(self, var=global1)

        if football_year == '2017':
            global1 = open_game_club('http://wildstat.ru/p/60/ch/WRL_FR_2017/stg/all/tour/all')
            Game_club(self, var=global1)

        if football_year == '2016':
            global1 = open_game_club('http://wildstat.ru/p/60/ch/WRL_FR_2016/stg/all/tour/all')
            Game_club(self, var=global1)

        if football_year == '2015':
            global1 = open_game_club('http://wildstat.ru/p/60/ch/WRL_FR_2015/stg/all/tour/all')
            Game_club(self, var=global1)

        if football_year == '2014':
            global1 = open_game_club('http://wildstat.ru/p/60/ch/WRL_FR_2014/stg/all/tour/all')
            Game_club(self, var=global1)

        if football_year == '2013':
            global1 = open_game_club('http://wildstat.ru/p/60/ch/WRL_FR_2013/stg/all/tour/all')
            Game_club(self, var=global1)

        if football_year == '2012':
            global1 = open_game_club('http://wildstat.ru/p/60/ch/WRL_FR_2012/stg/all/tour/all')
            Game_club(self, var=global1)

        if football_year == '2011':
            global1 = open_game_club('http://wildstat.ru/p/60/ch/WRL_FR_2011/stg/all/tour/all')
            Game_club(self, var=global1)

        if football_year == '2010':
            global1 = open_game_club('http://wildstat.ru/p/60/ch/WRL_FR_2010/stg/all/tour/all')
            Game_club(self, var=global1)

        if football_year == '2009':
            global1 = open_game_club('http://wildstat.ru/p/60/ch/WRL_FR_2009/stg/all/tour/all')
            Game_club(self, var=global1)

        if football_year == '2008':
            global1 = open_game_club('http://wildstat.ru/p/60/ch/WRL_FR_2008/stg/all/tour/all')
            Game_club(self, var=global1)

    def print_year_club(self):
        football_year = self.text
        if football_year == '2019/2018':
            global1 = open_game_now('http://wildstat.ru/p/50/ch/EUR_CL_2018_2019/stg/all/tour/all')
            Game_now(self, var=global1)

        if football_year == '2018/2017':
            global1 = open_game_now('http://wildstat.ru/p/50/ch/EUR_CL_2017_2018/stg/all/tour/all')
            Game_now(self, var=global1)

        if football_year == '2017/2016':
            global1 = open_game_now('http://wildstat.ru/p/50/ch/EUR_CL_2016_2017/stg/all/tour/all')
            Game_now(self, var=global1)

        if football_year == '2016/2015':
            global1 = open_game_now('http://wildstat.ru/p/50/ch/EUR_CL_2015_2016/stg/all/tour/all')
            Game_now(self, var=global1)

        if football_year == '2015/2014':
            global1 = open_game_now('http://wildstat.ru/p/50/ch/EUR_CL_2014_2015/stg/all/tour/all')
            Game_now(self, var=global1)

        if football_year == '2014/2013':
            global1 = open_game_now('http://wildstat.ru/p/50/ch/EUR_CL_2013_2014/stg/all/tour/all')
            Game_now(self, var=global1)

        if football_year == '2013/2012':
            global1 = open_game_now('http://wildstat.ru/p/50/ch/EUR_CL_2012_2013/stg/all/tour/all')
            Game_now(self, var=global1)

        if football_year == '2012/2011':
            global1 = open_game_now('http://wildstat.ru/p/50/ch/EUR_CL_2011_2012/stg/all/tour/all')
            Game_now(self, var=global1)

        if football_year == '2011/2010':
            global1 = open_game_now('http://wildstat.ru/p/50/ch/EUR_CL_2010_2011/stg/all/tour/all')
            Game_now(self, var=global1)

        if football_year == '2010/2009':
            global1 = open_game_now('http://wildstat.ru/p/50/ch/EUR_CL_2009_2010/stg/all/tour/all')
            Game_now(self, var=global1)

        if football_year == '2009/2008':
            global1 = open_game_now('http://wildstat.ru/p/50/ch/EUR_CL_2008_2009/stg/all/tour/all')
            Game_now(self, var=global1)

        if football_year == '2008/2007':
            global1 = open_game_now('http://wildstat.ru/p/50/ch/EUR_CL_2007_2008/stg/all/tour/all')
            Game_now(self, var=global1)

    def open_music(self):
        t.start()

class Child(tk.Toplevel):
    def __init__(self, root):
        super().__init__(root)
        self.init_child()
        self.root = root

    def init_child(self):
        self.title('Футбольные Команды')
        self.geometry('400x220+400+300')
        self.resizable(False, False)

        label_description = tk.Label(self, text='Название 2-х команд:')
        label_description.place(x=50, y=50)

        self.entry_description = ttk.Entry(self)
        self.entry_description.place(x=200, y=50)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=170)

        btn_ok = ttk.Button(self, text='Сравнить', command = self.add_something)
        btn_ok.place(x=220, y=170)

        self.grab_set()
        self.focus_set()

    def add_something(self):
        self.root.text = self.entry_description.get()
        self.root.print_text()
        self.destroy()

class Game(tk.Toplevel):
    def __init__(self, root):
        super().__init__(root)
        self.init_game()
        self.root = root

    def init_game(self):
        self.title('Футбольные Команды и их иглы')
        self.geometry('400x220+400+300')
        self.resizable(False, False)

        label_description = tk.Label(self, text='Название 2-х команд:')
        label_description.place(x=50, y=50)

        self.entry_description = ttk.Entry(self)
        self.entry_description.place(x=200, y=50)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=170)

        btn_ok = ttk.Button(self, text='Посмотреть игры', command = self.add_game)
        btn_ok.place(x=190, y=170)

        self.grab_set()
        self.focus_set()

    def add_game(self):
        self.root.text = self.entry_description.get()
        self.root.print_game()
        self.destroy()


class show_Game(tk.Toplevel):
    def __init__(self, root, var):
        super().__init__(root)
        self.root = root
        self.var = var
        self.init_show_game()

    def init_show_game(self):
        self.title('Футбольные Команды и их иглы')
        self.geometry('800x420+400+300')
        self.resizable(False, False)

        mylist = tk.Listbox(self, width=118, height=20)
        for line in range(len(self.var[2])):
            mylist.insert(tk.END, self.var[2][line])
        mylist.pack(side=tk.LEFT, fill=tk.BOTH)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=715, y=20)


class Game_now(tk.Toplevel):
    def __init__(self, root, var):
        super().__init__(root)
        self.root = root
        self.var = var
        self.init_game_now()


    def init_game_now(self):
        self.title('Футбольные Команды и их иглы')
        self.geometry('800x420+400+300')
        self.resizable(False, False)

        mylist = tk.Listbox(self, width=118, height=20)
        for line in range(len(self.var)):
            mylist.insert(tk.END, self.var[line].getText())
        mylist.pack(side=tk.LEFT, fill=tk.BOTH)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=715, y=20)

        self.grab_set()
        self.focus_set()

class Game_club(tk.Toplevel):
    def __init__(self, root, var):
        super().__init__(root)
        self.root = root
        self.var = var
        self.init_game_now()


    def init_game_now(self):
        self.title('Футбольные Команды и их иглы')
        self.geometry('800x420+400+300')
        self.resizable(False, False)

        mylist = tk.Listbox(self, width=118, height=20)
        for line in range(1, len(self.var), 2):
            mylist.insert(tk.END, self.var[line].getText())
        mylist.pack(side=tk.LEFT, fill=tk.BOTH)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=715, y=20)

        self.grab_set()
        self.focus_set()

class Year(tk.Toplevel):
    def __init__(self, root):
        super().__init__(root)
        self.init_year()
        self.root = root

    def init_year(self):
        self.title('Футбольные Команды и их иглы')
        self.geometry('400x220+400+300')
        self.resizable(False, False)

        label_select = tk.Label(self, text='Годы:')
        label_select.place(x=155, y=80)

        self.combobox = ttk.Combobox(self, values=[u"2019", u"2018", "2017", u"2016", u"2015", u"2014", "2013",
                                                   u"2012", u"2011", u"2010", "2009", u"2008"])
        self.combobox.current(0)
        self.combobox.place(x=200, y=80)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=170)

        btn_ok = ttk.Button(self, text='Посмотреть игры', command = self.add_year)
        btn_ok.place(x=190, y=170)

        self.grab_set()
        self.focus_set()

    def add_year(self):
        self.root.text = self.combobox.get()
        self.root.print_year()
        self.destroy()

class Year_club(tk.Toplevel):
    def __init__(self, root):
        super().__init__(root)
        self.init_year()
        self.root = root

    def init_year(self):
        self.title('Футбольные Команды и их иглы')
        self.geometry('400x220+400+300')
        self.resizable(False, False)

        label_select = tk.Label(self, text='Годы:')
        label_select.place(x=155, y=80)

        self.combobox = ttk.Combobox(self, values=[u"2019/2018", u"2018/2017", "2017/2016", u"2016/2015", u"2015/2014",
                                                   u"2014/2013", "2013/2012",
                                                   u"2012/2011", u"2011/2010", u"2010/2009", "2009/2008",
                                                   u"2008/2007"])
        self.combobox.current(0)
        self.combobox.place(x=200, y=80)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=170)

        btn_ok = ttk.Button(self, text='Посмотреть игры', command = self.add_year)
        btn_ok.place(x=190, y=170)

        self.grab_set()
        self.focus_set()

    def add_year(self):
        self.root.text = self.combobox.get()
        self.root.print_year_club()
        self.destroy()

class Game(tk.Toplevel):
    def __init__(self, root):
        super().__init__(root)
        self.init_game()
        self.root = root

    def init_game(self):
        self.title('Футбольные Команды и их иглы')
        self.geometry('400x220+400+300')
        self.resizable(False, False)

        label_description = tk.Label(self, text='Название 2-х команд:')
        label_description.place(x=50, y=50)

        self.entry_description = ttk.Entry(self)
        self.entry_description.place(x=200, y=50)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=170)

        btn_ok = ttk.Button(self, text='Посмотреть игры', command = self.add_game)
        btn_ok.place(x=190, y=170)

        self.grab_set()
        self.focus_set()

    def add_game(self):
        self.root.text = self.entry_description.get()
        self.root.print_game()
        self.destroy()



if __name__ == "__main__":
    #root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title("football_manager")
    root.geometry("1280x950+300+200")
    root.resizable(False, False)
    root.mainloop()

