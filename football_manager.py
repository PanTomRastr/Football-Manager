import tkinter as tk
from tkinter import ttk
from function import football_box, proverka, chek, sait

class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.text = ''

    def init_main(self):

        #self.scrollbar = tk.Scrollbar(root, orient="vertical")
        #self.scrollbar.pack(side=tk.LEFT, fill=tk.Y)

        toolbar = tk.Frame(bg='#d7d8e0', bd=2)
        toolbar.pack(side=tk.TOP,fill=tk.X)


        self.add_img = tk.PhotoImage(file="add.gif")
        btn_open_dialog = tk.Button(toolbar, text='Сравните команды', command=self.open_dialog, bg='#d7d8e0', bd=0,
                                    compound=tk.TOP, image=self.add_img)
        btn_open_dialog.pack(side=tk.LEFT)

        self.tree1 = ttk.Treeview(self, columns=('ID'))
        self.tree1.column("ID", width=440, anchor=tk.CENTER)
        #self.tree1.column("description", width=365, anchor=tk.CENTER)
        #self.tree1.column("costs", width=150, anchor=tk.CENTER)
        #self.tree1.column("total", width=100, anchor=tk.CENTER)

        #self.tree1.heading("ID", text='ID')
        #self.tree1.heading("description", text='Наименование')
        #self.tree1.heading("costs", text='Статья дохода/расхода')
        #self.tree1.heading("total", text='Сумма')

        self.tree1.insert('', '0', 'item1', text = 'Игры')
        self.tree1.insert('', '1', 'item2', text='Победы')
        self.tree1.insert('', '2', 'item3', text='Ничьи')
        self.tree1.insert('', '3', 'item4', text='Проигрыши')

        self.tree1.pack(side=tk.LEFT)

        self.tree2 = ttk.Treeview(self, columns=('ID'))
        self.tree2.column("ID", width=440, anchor=tk.CENTER)
        #self.tree2.column("description", width=365, anchor=tk.CENTER)
        #self.tree2.column("costs", width=150, anchor=tk.CENTER)
        #self.tree2.column("total", width=100, anchor=tk.CENTER)

        #self.tree2.heading("ID", text='ID')
        #self.tree2.heading("description", text='Наименование')
        #self.tree2.heading("costs", text='Статья дохода/расхода')
        #self.tree2.heading("total", text='Сумма')

        self.tree2.insert('', '0', 'item1', text='Игры')
        self.tree2.insert('', '1', 'item2', text='Победы')
        self.tree2.insert('', '2', 'item3', text='Ничьи')
        self.tree2.insert('', '3', 'item4', text='Проигрыши')

        self.tree2.pack(side=tk.LEFT)

        self.label_teams = tk.Label(bg='black', fg='white', width=182, height=15)
        self.label_teams.pack()

    def open_dialog(self):
        Child(self)

    def print_text(self):
        football_teams = self.text.split()
        football_teams = chek(football_teams)

        global1 = sait(football_teams[0], football_teams[1])

        print(football_teams, global1)

        if len(football_teams) == 2 and global1 != 'Нету комманд':

            self.label_teams['text'] = '\n'.join(football_teams)

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

        if global1 == 'Нету комманд':
            self.label_teams['text'] = global1

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
        #label_select = tk.Label(self, text='Статья дохода/расхода:')
        #label_select.place(x=50, y=80)
        #label_sum = tk.Label(self, text='Сумма:')
        #label_sum.place(x=50, y=110)

        self.entry_description = ttk.Entry(self)
        self.entry_description.place(x=200, y=50)
        #print(s)
        #self.entry_money = ttk.Entry(self)
        #self.entry_money.place(x=200, y=110)

        #self.combobox = ttk.Combobox(self, values=[u"Доход", u"Расход"])
        #self.combobox.current(0)
        #self.combobox.place(x=200, y=80)

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



if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title("football_manager")
    root.geometry("1280x720+300+200")
    root.resizable(False, False)
    root.mainloop()