from tkinter import *
from calculadora import Calculadora


def calculadora_basica(largura_calculadora, altura_calculadora):
    largura = largura_calculadora
    altura = altura_calculadora
    canvas = Canvas(janela_principal, width=largura, height=altura)
    canvas.pack()
    calculadora_basica = Calculadora(canvas)


janela_principal = Tk()
janela_principal.title("Calc")
icon = PhotoImage(file="imagem/calculadora_icone.png")
janela_principal.iconphoto(True, icon)
calculadora_basica(500, 500)
janela_principal.mainloop()
