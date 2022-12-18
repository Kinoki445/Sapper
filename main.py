import tkinter

class MyButton(tkinter.Button):
    
    def __init__(self, master, x, y, *args, **kwargs):
        super(MyButton, self).__init__(master, width = 4, font='Comics_sans 15 bold', *args, **kwargs)
        self.x = x
        self.y = y
        self.bunny = False


    def __repr__(self):
        return (f'MyButton x:{self.x} y:{self.y} {self.bunny}')

class BaronBunny:
    window = tkinter.Tk()
    ROW = 6 #Столбцов 
    COLUMNS = 4 #Строк


    def __init__(self):
        self.buttons = []
        for i in range(BaronBunny.ROW): #Создаём цикл который делает кнопки
            temp = []
            for j in range(BaronBunny.COLUMNS):
                btn = MyButton(BaronBunny.window, x = i, y = j)
                temp.append(btn)
            self.buttons.append(temp)

    def create_widgets(self):
        for i in range(BaronBunny.ROW):
            for j in range(BaronBunny.COLUMNS):
                btn = self.buttons[i][j] # Указывает место кнопки [0][0] начало
                btn.grid(row =i, column = j) # Выводит в tinker сами кнопки 

    def print_Button(self):
        for row_btn in self.buttons:
            print(row_btn) 

    def start(self):
        self.create_widgets()
        self.print_Button()
        BaronBunny.window.mainloop()


game = BaronBunny()
game.start()








