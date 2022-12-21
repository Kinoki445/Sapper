import tkinter
from random import shuffle #перемешивает любой список

class MyButton(tkinter.Button):
    
    def __init__(self, master, x, y, number, *args, **kwargs):
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
        count = 1
        for i in range(BaronBunny.ROW): #Создаём цикл который делает кнопки
            temp = []
            for j in range(BaronBunny.COLUMNS):
                btn = MyButton(BaronBunny.window, x = i, y = j, number=count)
                temp.append(btn)
                count += 1 
            self.buttons.append(temp)

    def create_widgets(self):
        for i in range(BaronBunny.ROW):
            for j in range(BaronBunny.COLUMNS):
                btn = self.buttons[i][j] # Указывает место кнопки [0][0] начало
                btn.grid(row =i, column = j) # Выводит в tinker сами кнопки 

    def print_Button(self):
        for row_btn in self.buttons:
            print(row_btn) 

    def insert_bunny(self):
        index_bunny = (self.get_bunny_places())
        print (index_bunny)
        for row_btn in self.buttons:
            for btn in row_btn:
                if btn.number in index_bunny:
                    btn.bunny = True

    @staticmethod #не поучает данные из __init__
    def get_bunny_places():
        index = list(range(1, BaronBunny.COLUMNS * BaronBunny.ROW + 1))
        shuffle(index)
        return(index [:BaronBunny.MINES])


    def start(self):
        self.create_widgets()
        self.insert_bunny()
        self.print_Button()
        BaronBunny.window.mainloop()


game = BaronBunny()
game.start()








