import tkinter
from tkinter import Tk, Button
from PIL import ImageTk
from random import shuffle #перемешивает любой список

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
        super(MyButton, self).__init__(master, width = 5, font='Comics_sans 15 bold', *args, **kwargs)
        self.x = x
        self.y = y
        self.number = number
        self.bunny = False
        self.count_bomb = 0

    def __repr__(self): # меняет вывод в консоль 
        return (f'Btn #:{self.number} x:{self.x} y:{self.y} {self.bunny}')

class BaronBunny:
    window = tkinter.Tk()
    window.title("BaronBunny | Alpha")
    ROW = 10 #Столбцов 
    COLUMNS = 10 #Строк
    MINES = 10


    def __init__(self):
        self.buttons = []
        for i in range(BaronBunny.ROW+2): #Создаём цикл который делает кнопки
            temp = []
            for j in range(BaronBunny.COLUMNS+2):
                btn = MyButton(BaronBunny.window, x = i, y = j)
                btn.config(command =lambda button = btn: self.click(button))
                temp.append(btn)
            self.buttons.append(temp)

    def create_widgets(self):
        for i in range(1, BaronBunny.ROW + 1):
            for j in range(1, BaronBunny.COLUMNS+1):
                btn = self.buttons[i][j] # Указывает место кнопки [0][0] начало
                btn.grid(row =i, column = j) # Выводит в tinker сами кнопки 

    def open_btn(self):
        for i in range(BaronBunny.ROW+2):
            for j in range(BaronBunny.COLUMNS+2):
                btn = self.buttons[i][j] # Указывает место кнопки [0][0] начало
                if btn.bunny:
                    # icon = ImageTk.PhotoImage(file="D:\Desktop\my works\Game\Sapper\icon.png")
                    btn.config(text = '*', background='red') #Если мина, то *
                elif btn.count_bomb in colors:
                    color = colors.get(btn.count_bomb, 'black')
                    btn.config(text = btn.count_bomb, fg = color)

                # btn.config(state='disabled', disabledforeground='black')  
                # btn.grid(row =i, column = j) # Выводит в tinker сами кнопки

    def click(self, click_btn: MyButton):
        if click_btn.bunny: 
            click_btn.config(text = '*', background='red', disabledforeground='black') #Если мина, то *
        else:
            color = colors.get(click_btn.count_bomb, 'black')
            if click_btn.count_bomb:
                click_btn.config(text = click_btn.count_bomb, disabledforeground=color)
            else:
                click_btn.config(text = '', disabledforeground=color)
        click_btn.config(state='disabled', relief=tkinter.SUNKEN) # Добавляет рельеф
        


    def print_Button(self):
        for i in range(1, BaronBunny.ROW + 1):
            for j in range(1, BaronBunny.COLUMNS+1):
                btn = self.buttons[i][j] # Указывает место кнопки [0][0] начало
                if btn.bunny:
                    print('B ', end='')
                else:
                    print(f'{btn.count_bomb} ', end='')
            print()

    def insert_bunny(self):
        index_bunny = (self.get_bunny_places())
        print (index_bunny)
        count = 1 
        for i in range(1, BaronBunny.ROW + 1):
            for j in range(1, BaronBunny.COLUMNS+1):
                btn = self.buttons[i][j]
                btn.number = count
                if btn.number in index_bunny:
                    btn.bunny = True
                count += 1
                
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
    def get_bunny_places():
        index = list(range(1, BaronBunny.COLUMNS * BaronBunny.ROW + 1))
        shuffle(index)
        return(index [:BaronBunny.MINES])


    def start(self):
        self.create_widgets()
        self.insert_bunny()
        self.count_mines_in_ceils()
        self.open_btn()
        self.print_Button()
        BaronBunny.window.mainloop()


game = BaronBunny()
game.start()








