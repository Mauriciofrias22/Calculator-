from tkinter import *

window = Tk()
window.title("Calculator")

i = 0

    #Entrada
e_texto = Entry(window, font = ("Calibri 20"))
e_texto.grid(row = 0, column = 0, columnspan = 4, padx = 5, pady = 5) 

    #funciones
def click_button(valor):
    global i
    e_texto.insert(i, valor)
    i += 1

def delete_text():
    e_texto.delete(0, END)
    i = 0

def operations():
    ecuacion = e_texto.get()
    resultado = eval(ecuacion)
    e_texto.delete(0, END)
    e_texto.insert(0, resultado)
    i = 0
    
    #Buttons
number1 = Button(window, text = "1", width = 5, height = 2, command = lambda: click_button(1))
number2 = Button(window, text = "2", width = 5, height = 2, command = lambda: click_button(2))
number3 = Button(window, text = "3", width = 5, height = 2, command = lambda: click_button(3))
number4 = Button(window, text = "4", width = 5, height = 2, command = lambda: click_button(4))
number5 = Button(window, text = "5", width = 5, height = 2, command = lambda: click_button(5))
number6 = Button(window, text = "6", width = 5, height = 2, command = lambda: click_button(6))
number7 = Button(window, text = "7", width = 5, height = 2, command = lambda: click_button(7))
number8 = Button(window, text = "8", width = 5, height = 2, command = lambda: click_button(8))
number9 = Button(window, text = "9", width = 5, height = 2, command = lambda: click_button(9))
number0 = Button(window, text = "0", width = 15, height = 2, command = lambda: click_button(0))

delete_button = Button(window, text = "AC", width = 5, height = 2, command = lambda: delete_text())
parentheses1_button  = Button(window, text = "(", width = 5, height = 2, command = lambda: click_button("("))
parentheses2_button = Button(window, text = ")", width = 5, height = 2, command = lambda: click_button(")"))
point_button = Button(window, text = ".", width = 5, height = 2, command = lambda: click_button("."))

division_button = Button(window, text = "/", width = 5, height = 2, command = lambda: click_button("/"))
multiplication_button = Button(window, text = "x", width = 5, height = 2, command = lambda: click_button("*"))
add_button = Button(window, text = "+", width = 5, height = 2, command = lambda: click_button("+"))
substraction_button = Button(window, text = "-", width = 5, height = 2, command = lambda: click_button("-"))
equal_button = Button(window, text = "=", width = 5, height = 2, command = lambda: operations())

    #Agregar botones en pantalla
delete_button.grid(row = 1, column = 0, padx = 5, pady = 5)       
parentheses1_button.grid(row = 1, column = 1, padx = 5, pady = 5)
parentheses2_button.grid(row = 1, column = 2, padx = 5, pady = 5)
division_button.grid(row = 1, column = 3, padx = 5, pady = 5)

number7.grid(row = 2, column = 0, padx = 5, pady = 5)
number8.grid(row = 2, column = 1, padx = 5, pady = 5)
number9.grid(row = 2, column = 2, padx = 5, pady = 5)
multiplication_button.grid(row = 2, column = 3, padx = 5, pady = 5)

number4.grid(row = 3, column = 0, padx = 5, pady = 5)
number5.grid(row = 3, column = 1, padx = 5, pady = 5)
number6.grid(row = 3, column = 2, padx = 5, pady = 5)
add_button.grid(row = 3, column = 3, padx = 5, pady = 5)

number1.grid(row = 4, column = 0, padx = 5, pady = 5)
number2.grid(row = 4, column = 1, padx = 5, pady = 5)
number3.grid(row = 4, column = 2, padx = 5, pady = 5)
substraction_button.grid(row = 4, column = 3, padx = 5, pady = 5)

number0.grid(row = 5, column = 0, columnspan = 2, padx = 5, pady = 5)
point_button.grid(row = 5, column = 2, padx = 5, pady = 5)
equal_button.grid(row = 5, column = 3, padx = 5, pady = 5)

window.mainloop()
