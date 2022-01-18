from tkinter import *
from math import *
import re


class Calculadora:
    def __init__(self, canvas):
        self._numeros = ''# Numbers label
        altura = 2# Buttons heigth
        largura = 5# Buttons width
        self._canvas = canvas
        # display
        self._display = Label(self._canvas, text="Num", height=3, width=25, bg="white")
        # Frame
        self._frame = Frame(self._canvas)
        self._create_button(altura, largura)
        # build interface
        self._place_buttons()

    def _create_button(self, altura, largura):
        # 0 - 9
        self._button_0 = Button(self._frame, text="0", height=altura, width=largura,
                                command=lambda: self.button_num('0'))
        self._button_1 = Button(self._frame, text="1", height=altura, width=largura,
                                command=lambda: self.button_num('1'))
        self._button_2 = Button(self._frame, text="2", height=altura, width=largura,
                                command=lambda: self.button_num('2'))
        self._button_3 = Button(self._frame, text="3", height=altura, width=largura,
                                command=lambda: self.button_num('3'))
        self._button_4 = Button(self._frame, text="4", height=altura, width=largura,
                                command=lambda: self.button_num('4'))
        self._button_5 = Button(self._frame, text="5", height=altura, width=largura,
                                command=lambda: self.button_num('5'))
        self._button_6 = Button(self._frame, text="6", height=altura, width=largura,
                                command=lambda: self.button_num('6'))
        self._button_7 = Button(self._frame, text="7", height=altura, width=largura,
                                command=lambda: self.button_num('7'))
        self._button_8 = Button(self._frame, text="8", height=altura, width=largura,
                                command=lambda: self.button_num('8'))
        self._button_9 = Button(self._frame, text="9", height=altura, width=largura,
                                command=lambda: self.button_num('9'))

        # special buttons
        self._button_negate = Button(self._frame, text="+/-", height=altura, width=largura, command=self.button_negate)
        self._button_dot = Button(self._frame, text=",", height=altura, width=largura,
                                  command=lambda: self.button_special('.'))
        self._button_plus = Button(self._frame, text="+", height=altura, width=largura,
                                   command=lambda: self.button_special('+'))
        self._button_minus = Button(self._frame, text="-", height=altura, width=largura,
                                    command=lambda: self.button_special('-'))
        self._button_multiplication = Button(self._frame, text="*", height=altura, width=largura,
                                             command=lambda: self.button_special('*'))
        self._button_division = Button(self._frame, text="÷", height=altura, width=largura,
                                       command=lambda: self.button_special('/'))
        self._button_confirm = Button(self._frame, text="=", height=altura, width=largura, command=self.button_confirm)
        self._button_square_root = Button(self._frame, text="√", height=altura, width=largura,
                                          command=self.button_square_root)
        self._button_square = Button(self._frame, text="x²", height=altura, width=largura, command=self.button_square)
        self._button_percent = Button(self._frame, text="%", height=altura, width=largura,
                                      command=self.button_pecent)
        self._button_clear = Button(self._frame, text="C", height=altura, width=largura, command=self.button_clear)
        self._button_invert = Button(self._frame, text="1/x", height=altura, width=largura, command=self.button_invert)
        self._button_remove = Button(self._frame, text="X", height=altura, width=largura, command=self.button_remove)

    def _place_buttons(self):
        # Display
        self._display.pack()
        # Frame
        self._frame.pack()
        # Row 1
        self._button_percent.grid(row=1, column=0)
        self._button_clear.grid(row=1, column=1)
        self._button_remove.grid(row=1, column=2)
        # Row 2
        self._button_invert.grid(row=2, column=0)
        self._button_square.grid(row=2, column=1)
        self._button_square_root.grid(row=2, column=2)
        self._button_division.grid(row=2, column=3)
        # Row 3
        self._button_7.grid(row=3, column=0)
        self._button_8.grid(row=3, column=1)
        self._button_9.grid(row=3, column=2)
        self._button_multiplication.grid(row=3, column=3)
        # row 4
        self._button_4.grid(row=4, column=0)
        self._button_5.grid(row=4, column=1)
        self._button_6.grid(row=4, column=2)
        self._button_minus.grid(row=4, column=3)
        # row 5
        self._button_1.grid(row=5, column=0)
        self._button_2.grid(row=5, column=1)
        self._button_3.grid(row=5, column=2)
        self._button_plus.grid(row=5, column=3)
        # row 6
        self._button_negate.grid(row=6, column=0)
        self._button_0.grid(row=6, column=1)
        self._button_dot.grid(row=6, column=2)
        self._button_confirm.grid(row=6, column=3)

    def button_num(self, num):
        if not self._comeca_com_zero(num):
            self._numeros = self._numeros + str(num)
            self._display.config(text=self._numeros)

    def button_special(self, buttons):
        if self._tem_numero_antes():
            self._numeros = self._numeros + str(buttons)
            self._display.config(text=self._numeros)

    def button_clear(self):
        self._numeros = ""
        self._display.config(text=self._numeros)

    def button_remove(self):
        ultimo_caracter = len(self._numeros) - 1
        self._numeros = self._numeros[:ultimo_caracter]
        self._display.config(text=self._numeros)

    def button_confirm(self):
        if self._display_com_numero():
            try:
                total = eval(self._numeros)
                self._display.config(text=total)
                self._numeros = str(total)
            except ZeroDivisionError:
                self._display.config(text="Não é possível dividir por 0")
            except:
                self._display.config(text="Não foi possível efetuar o cálculo")

    def button_negate(self):
        self.button_confirm()
        if self._display_com_numero():
            try:
                numero = float(self._numeros)
                numero = numero * -1
                self._numeros = str(numero)
                self._display.config(text=self._numeros)
            except:
                self._display.config(text="Não foi possível efetuar o cálculo")

    def button_square_root(self):
        if self._display_com_numero():
            try:
                numero = int(self._numeros)
                numero_square_root = sqrt(numero)
                self._numeros = numero_square_root
                self._display.config(text=self._numeros)
            except:
                self._display.config(text="Não foi possível efetuar o cálculo")

    def button_square(self):
        if self._display_com_numero():
            try:
                numero = int(self._numeros)
                numero_square = pow(numero, 2)
                self._numeros = numero_square
                self._display.config(text=self._numeros)
            except:
                self._display.config(text="Não foi possível efetuar o cálculo")

    def button_invert(self):
        self.button_confirm()
        if self._display_com_numero():
            try:
                numero = int(self._numeros)
                numero_invert = 1 / numero
                self._numeros = numero_invert
                self._display.config(text=self._numeros)
            except:
                self._display.config(text="Não foi possível efetuar o cálculo")

    def _tem_numero_antes(self):
        tem_numero_antes = False
        if self._display_com_numero():
            for i in range(10):
                numero_string = str(i)
                if self._numeros[-1] == numero_string:
                    tem_numero_antes = True
                    break
        return tem_numero_antes

    def button_pecent(self):
        if self._display_com_numero():
            self._numeros = str(self._numeros) + '%'
            padrao = "[0-9]{1,}%"
            # search any number that end with %
            try:
                busca = re.search(padrao, str(self._numeros))
                percent_numero_com_porcentagem = busca.group(0)
                # remove the '%' to convernt in fraction number
                tamanho_sem_porcentagem = len(percent_numero_com_porcentagem) - 1
                numero_sem_porcentagem = percent_numero_com_porcentagem[0: tamanho_sem_porcentagem]
                numero_fracionario = float(numero_sem_porcentagem) / 100
                numeros = str(self._numeros)
                self._numeros = numeros.replace(percent_numero_com_porcentagem, str(numero_fracionario))
                self.button_confirm()
            except:
                self._display.config(text="Não foi possível efetuar o cálculo")

    def _display_com_numero(self):
        return len(self._numeros)

    def _comeca_com_zero(self, num):
        comeca_com_zero = False
        if not self._display_com_numero() and num == '0':
            comeca_com_zero = True
        return comeca_com_zero
