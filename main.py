import tkinter

from random import shuffle #перемешивает любой список
from tkinter.messagebox import showinfo, showerror


colors = {
    0: 'white',
    1: 'blue',
    2: 'green',
    3: '#8037ed',
    4: '#377ded',
    5: '#d64b85',
    6: '#d6724b',
    7: '#d64bca',
    8: '#8c2222'
}

class MyButton(tkinter.Button): #Вся информация о кнопках
    def __init__(self, master, x, y, number = 0, *args, **kwargs):
        super(MyButton, self).__init__(master, width = 3, font='Comics_sans 15 bold', *args, **kwargs)
        self.x = x
        self.y = y
        self.number = number
        self.bunny = False
        self.count_bomb = 0
        self.is_open = False

    def __repr__(self): # меняет вывод в консоль 
        return (f'Btn #:{self.number} x:{self.x} y:{self.y} {self.bunny}')

class BaronBunny:
    window = tkinter.Tk()
    window.title("BaronBunny | Alpha")
    window.iconbitmap(r'icon.ico')

    ROW = 10 #Столбцов 
    COLUMNS = 7 #Строк
    MINES = 10
    GAME_OVER = False
    FIRST_CLICK = True
    
    def __init__(self):
        self.buttons = []
        for i in range(BaronBunny.ROW + 2): #Создаём цикл который делает кнопки
            temp = []
            for j in range(BaronBunny.COLUMNS + 2):
                btn = MyButton(BaronBunny.window, x = i, y = j)
                btn.config(command = lambda button = btn: self.click(button))
                btn.bind("<Button-3>", self.right_click)
                temp.append(btn)
            self.buttons.append(temp)

    def right_click(self, event):
        if BaronBunny.GAME_OVER:
            return
        cur_btn = event.widget
        if cur_btn['state'] == 'normal':
            cur_btn['state'] = 'disabled'
            cur_btn['text'] = '🐰'
        elif cur_btn['text'] == '🐰':
            cur_btn['text'] = ''
            cur_btn['state'] = 'normal'

    def game(self):
        [child.destroy() for child in self.window.winfo_children()]
        self.__init__()
        self.create_widgets()
        BaronBunny.FIRST_CLICK = True
        BaronBunny.GAME_OVER = False

    def settings(self):
        win_set = tkinter.Toplevel(self.window)
        win_set.wm_title('Настройки')

        tkinter.Label(win_set, text='Количество строк:').grid(row=0,column=0)
        row_entry = tkinter.Entry(win_set)
        row_entry.insert(0, BaronBunny.ROW)
        row_entry.grid(row=0,column=1, padx=20, pady=20)

        tkinter.Label(win_set, text='Количество колонок:').grid(row=1,column=0)
        column_entry = tkinter.Entry(win_set)
        column_entry.insert(0, BaronBunny.COLUMNS)
        column_entry.grid(row=1, column=1, padx=20, pady=20)

        tkinter.Label(win_set, text='Количество зайцев:').grid(row=2,column=0)
        bunny_entry = tkinter.Entry(win_set)
        bunny_entry.insert(0, BaronBunny.MINES)
        bunny_entry.grid(row=2, column=1, padx=20, pady=20)

        save_btn = tkinter.Button(win_set, text='Применить', command=lambda :self.change_settings(row_entry, column_entry, bunny_entry))
        save_btn.grid(row=3,column=0, columnspan=2)

    def change_settings(self, row: tkinter.Entry, column: tkinter.Entry, bunny: tkinter.Entry):
        try:
            int(row.get()), int(column.get()), int(bunny.get())
        except ValueError:
            showerror('ERROR', 'Вы ввели неверное число!')
        BaronBunny.ROW = int(row.get())
        BaronBunny.COLUMNS = int(column.get())
        BaronBunny.MINES = int(bunny.get())

        self.game()

    def create_widgets(self):
        
        menubar = tkinter.Menu(self.window)
        self.window.config(menu=menubar)

        menubar.add_command(label='Играть', command=self.game)
        menubar.add_command(label='Настройки', command=self.settings)
        menubar.add_command(label='Выйти', command=self.window.destroy)

        count = 1
        for i in range(1, BaronBunny.ROW + 1):
            for j in range(1, BaronBunny.COLUMNS+1):
                btn = self.buttons[i][j] # Указывает место кнопки [0][0] начало
                btn.number = count
                btn.grid(row =i, column = j, stick = 'nwes') # Выводит в tinker сами кнопки 
                count += 1
        
        for i in range(1, BaronBunny.ROW + 1):
            tkinter.Grid.rowconfigure(self.window, i, weight = 1)

        for i in range(1, BaronBunny.COLUMNS + 1):
            tkinter.Grid.columnconfigure(self.window, i, weight = 1)

    def open_btn(self):
        for i in range(BaronBunny.ROW+2):
            for j in range(BaronBunny.COLUMNS+2):
                btn = self.buttons[i][j] # Указывает место кнопки [0][0] начало
                if btn.bunny:
                    btn.config(text = '💣') #Если мина, то *
                elif btn.count_bomb in colors:
                    color = colors.get(btn.count_bomb, 'black')
                    btn.config(text = btn.count_bomb, fg = color)

                # btn.config(state='disabled', disabledforeground='black')  
                # btn.grid(row =i, column = j) # Выводит в tinker сами кнопки

    def click(self, click_btn: MyButton):

        if BaronBunny.GAME_OVER:
            return None
            
        if BaronBunny.FIRST_CLICK:
            self.insert_bunny(click_btn.number)
            self.count_mines_in_ceils()
            self.print_Button()
            BaronBunny.FIRST_CLICK = False


        if click_btn.bunny: 
            click_btn.config(text = '💣') #Если мина, то *
            click_btn.is_open = True
            BaronBunny.GAME_OVER = True
            showinfo('Game over', 'Вы проиграли')

            for i in range(1, BaronBunny.ROW + 1):
                for j in range(1, BaronBunny.COLUMNS + 1):
                    btn = self.buttons[i][j] # Указывает место кнопки [0][0] начало
                    if btn.bunny:
                        btn['text'] = ('💣')
        else:
            color = colors.get(click_btn.count_bomb, 'black')
            click_btn.is_open = True
            if click_btn.count_bomb:
                click_btn.config(text = click_btn.count_bomb, disabledforeground=color)
            else:
                self.search(click_btn)
        click_btn.config(state='disabled', relief=tkinter.SUNKEN) # Добавляет рельеф
        
    def search(self, btn: MyButton): #реализация алгоритм обход в ширину
        queue = [btn]
        while queue:
            cur_btn = queue.pop()
            color = colors.get(cur_btn.count_bomb, 'black')
            if cur_btn.count_bomb:
                cur_btn.config(text = cur_btn.count_bomb, disabledforeground=color)
            else:
                cur_btn.config(text = '', disabledforeground=color)

            cur_btn.is_open = True
            cur_btn.config(state='disabled', relief=tkinter.SUNKEN) # Добавляет рельеф

            if  cur_btn.count_bomb == 0:
                x, y = (cur_btn.x, cur_btn.y)
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        # if not abs(dx - dy) == 1:
                        #     continue
                        
                        next_btn = self.buttons[x+dx][y+dy]
                        if not next_btn.is_open and 1<=next_btn.x <= BaronBunny.ROW and 1<=next_btn.y <= BaronBunny.COLUMNS and next_btn not in queue:
                            queue.append(next_btn)

    def print_Button(self):
        for i in range(1, BaronBunny.ROW + 1):
            for j in range(1, BaronBunny.COLUMNS + 1):
                btn = self.buttons[i][j] # Указывает место кнопки [0][0] начало
                if btn.bunny:
                    print('B ', end='')
                else:
                    print(f'{btn.count_bomb} ', end='')
            print()

    def insert_bunny(self, number: int):
        index_bunny = (self.get_bunny_places(number))
        print (index_bunny)
        for i in range(1, BaronBunny.ROW + 1):
            for j in range(1, BaronBunny.COLUMNS+1):
                btn = self.buttons[i][j]
                if btn.number in index_bunny:
                    btn.bunny = True

    def count_mines_in_ceils(self):
        for i in range(BaronBunny.ROW + 1):
            for j in range(BaronBunny.COLUMNS + 1):
                btn = self.buttons[i][j]
                count_bomb = 0
                if not btn.bunny:
                    for row_dx in [-1, 0, 1]:
                        for col_dx in [-1, 0, 1]:
                            neignbour = self.buttons[i+row_dx][j+col_dx]
                            if neignbour.bunny:
                                count_bomb += 1
                btn.count_bomb = count_bomb

    @staticmethod #не поучает данные из __init__
    def get_bunny_places(exclude_number: int):
        index = list(range(1, BaronBunny.COLUMNS * BaronBunny.ROW + 1))
        index.remove(exclude_number)
        shuffle(index)
        return(index [:BaronBunny.MINES])


    def start(self):
        self.create_widgets()
        # self.open_btn()
        BaronBunny.window.resizable(False,False)
        BaronBunny.window.mainloop()

game = BaronBunny()
game.start()








