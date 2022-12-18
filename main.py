import tkinter

window = tkinter.Tk()

ROW = 4
COLUMNS = 8

buttons = []
for i in range(ROW): #Создаём цикл который делает кнопки
    temp = []
    for j in range(COLUMNS):
        btn = tkinter.Button(window, width = 4, font='Comics_sans 15 bold')
        temp.append(btn)
    buttons.append(temp)

for row_btn in buttons:
    print(row_btn)

for i in range(ROW):
    for j in range(COLUMNS):
        btn = buttons[i][j] # Указывает место кнопки [0][0] начало
        btn.grid(row =i, column = j) # Выводит в tinker сами кнопки 


window.mainloop()