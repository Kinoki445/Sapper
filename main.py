import tkinter


class BaronBunny:
    window = tkinter.Tk()
    ROW = 4
    COLUMNS = 8


    def __init__(self):
        self.buttons = []
        for i in range(BaronBunny.ROW): #Создаём цикл который делает кнопки
            temp = []
            for j in range(BaronBunny.COLUMNS):
                btn = tkinter.Button(BaronBunny.window, width = 4, font='Comics_sans 15 bold')
                temp.append(btn)
            self.buttons.append(temp)

    def create_widgets(self):
        for i in range(BaronBunny.ROW):
            for j in range(BaronBunny.COLUMNS):
                btn = self.buttons[i][j] # Указывает место кнопки [0][0] начало
                btn.grid(row =i, column = j) # Выводит в tinker сами кнопки 

    def start(self):
        self.create_widgets()
        BaronBunny.window.mainloop()


game = BaronBunny()
game.start()

# for row_btn in game.buttons:
#     print(row_btn)






