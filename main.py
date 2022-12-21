import tkinter
from random import shuffle #перемешивает любой список

class MyButton(tkinter.Button): #Вся информация о кнопках
    
    def __init__(self, master, x, y, number = 0, *args, **kwargs):
        super(MyButton, self).__init__(master, width = 3, font='Comics_sans 15 bold', *args, **kwargs)
        self.x = x
        self.y = y
        self.number = number
        self.bunny = False

    def __repr__(self): # меняет вывод в консоль 
        return (f'Btn #:{self.number} x:{self.x} y:{self.y} {self.bunny}')

class BaronBunny:

    window = tkinter.Tk()
    window.title("BaronBunny | Alpha") 
    ROW = 10 #Столбцов 
    COLUMNS = 7 #Строк
    MINES = 15


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
        for i in range(BaronBunny.ROW+2):
            for j in range(BaronBunny.COLUMNS+2):
                btn = self.buttons[i][j] # Указывает место кнопки [0][0] начало
                btn.grid(row =i, column = j) # Выводит в tinker сами кнопки 

    def open_btn(self):
        for i in range(BaronBunny.ROW+2):
            for j in range(BaronBunny.COLUMNS+2):
                btn = self.buttons[i][j] # Указывает место кнопки [0][0] начало
                if btn.bunny: 
                    btn.config(text = '*', background='red') #Если мина, то *
                else:
                    btn.config(text = btn.number)
                btn.config(state='disabled', disabledforeground='black')  
                btn.grid(row =i, column = j) # Выводит в tinker сами кнопки

    def click(self, click_btn: MyButton):
        if click_btn.bunny: 
            click_btn.config(text = '*', background='red') #Если мина, то *
        else:
            click_btn.config(text = click_btn.number)
        click_btn.config(state='disabled', disabledforeground='black')


    def print_Button(self):
        for row_btn in self.buttons:
            print(row_btn) 

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

    @staticmethod #не поучает данные из __init__
    def get_bunny_places():
        index = list(range(1, BaronBunny.COLUMNS * BaronBunny.ROW + 1))
        shuffle(index)
        return(index [:BaronBunny.MINES])


    def start(self):
        self.create_widgets()
        self.insert_bunny()
        self.open_btn()
        self.print_Button()
        BaronBunny.window.mainloop()


game = BaronBunny()
game.start()








