from tkinter import *
from tkinter import ttk
import math
import numpy as np


class Number:
    def __init__(self, number: str, notation: int = 10) -> None:
        self.number = number
        self.notation = notation
    
    def convert_from_10(self, notation: int) -> None:
        tmp = ''
        number = self.number
        self.notation = notation
        is_negative = True if number[0] == '-' else False
        if is_negative: number = number[1:]
        number = number.split('.')
        num = int(number[0])
        while num != 0:
            tmp = (Digits[num%notation] if num % notation >= 10 else str(num % notation)) + tmp
            num //= notation
        if len(number) > 1:
            tmp_num = ''
            fl = float('0.' + number[1])
            while len(tmp_num) != 6 and fl != 0:
                fl *= notation
                if fl < 1.0:
                    tmp_num += '0'
                else:
                    tmp_num += str(int(fl)) if int(fl) not in Digits.keys() else Digits[int(fl)]
                    fl -= int(fl)
            tmp += '.' + tmp_num
        if is_negative:
            self.number = '-'+tmp
        else:
            self.number = tmp
    
    def convert_to_10(self, notation: int) -> None:
        tmp = 0
        number = self.number
        self.notation = 10
        is_negative = True if number[0] == '-' else False
        if is_negative: number = number[1:]
        number = number.split('.')
        num = number[0]
        num = num[::-1]
        tmp_num = 0
        for i in range(len(num)):
            if num[i] in Digits.keys():
                tmp += Digits[num[i]] * (notation ** i)
            else:
                tmp += int(num[i]) * (notation ** i)
        if len(number) > 1:
            fl = number[1]
            for i in range(len(fl)):
                if fl[i] in Digits.keys():
                    tmp_num += Digits[fl[i]] * (notation ** (-(i + 1)))
                else:
                    tmp_num += int(fl[i]) * (notation ** (-(i + 1)))
        if is_negative:
            self.number = '-'+str(tmp + tmp_num)
        else:
            self.number = str(tmp + tmp_num)

    def __add__(self, other):
        return add(self, other)
    def __sub__(self, other):
        return sub(self, other)
    def __mul__(self, other):
        return multiply(self, other)
    def __div__(self, other):
        return division(self, other)


def add(lhs: Number, rhs: Number, notation: int = 10) -> Number: 
    lhs.convert_to_10(lhs.notation)
    rhs.convert_to_10(rhs.notation)
    tmp = str(float(lhs.number) + float(rhs.number))
    return Number(tmp, notation)


def sub(lhs: Number, rhs: Number, notation: int = 10) -> Number:
    lhs.convert_to_10(lhs.notation)
    rhs.convert_to_10(rhs.notation)
    tmp = str(float(lhs.number) - float(rhs.number))
    return Number(tmp, notation)


def multiply(lhs: Number, rhs: Number, notation: int = 10) -> Number:
    lhs.convert_to_10(lhs.notation)
    rhs.convert_to_10(rhs.notation)
    tmp = str(float(lhs.number) * float(rhs.number))
    return Number(tmp, notation)


def division(lhs: Number, rhs: Number, notation: int = 10) -> Number:
    lhs.convert_to_10(lhs.notation)
    rhs.convert_to_10(rhs.notation)
    try:
        tmp = str(float(lhs.number) / float(rhs.number))
    except ZeroDivisionError:
        print('Деление на ноль!')
        return lhs
    else:
        return Number(tmp, notation)


Digits = {
    10:'A',
    11:'B',
    12:'C',
    13:'D',
    14:'E',
    15:'F',
    'A':10,
    'B':11,
    'C':12,
    'D':13,
    'E':14,
    'F':15}



# def convert_from_10(number: str, notation: int) -> str:
#     tmp = ''
#     is_negative = True if number[0] == '-' else False
#     if is_negative: number = number[1:]

#     number = number.split('.')
#     num = int(number[0])
#     while num != 0:
#         tmp = (Digits[num%notation] if num % notation >= 10 else str(num % notation)) + tmp
#         num //= notation
#     if len(number) > 1:
#         tmp_num = ''
#         fl = float('0.' + number[1])
#         while len(tmp_num) != 6 and fl != 0:
#             fl *= notation
#             if fl < 1.0:
#                 tmp_num += '0'
#             else:
#                 tmp_num += str(int(fl)) if int(fl) not in Digits.keys() else Digits[int(fl)]
#                 fl -= int(fl)
#         tmp += '.' + tmp_num
#     if is_negative:
#         return '-'+tmp
#     return tmp


# def convert_to_10(number: str, notation: int) -> str:
#     tmp = 0
#     is_negative = True if number[0] == '-' else False
#     if is_negative: number = number[1:]
#     number = number.split('.')
#     num = number[0]
#     num = num[::-1]
#     tmp_num = 0
#     for i in range(len(num)):
#         if num[i] in Digits.keys():
#             tmp += Digits[num[i]] * (notation ** i)
#         else:
#             tmp += int(num[i]) * (notation ** i)
#     if len(number) > 1:
#         fl = number[1]
#         for i in range(len(fl)):
#             if fl[i] in Digits.keys():
#                 tmp_num += Digits[fl[i]] * (notation ** (-(i + 1)))
#             else:
#                 tmp_num += int(fl[i]) * (notation ** (-(i + 1)))
#     if is_negative:
#         return '-'+str(tmp + tmp_num)
#     return str(tmp + tmp_num)


# def convert(num: str, from_notation: int = 10, to_notation: int = 10) -> str:
#     tmp = convert_to_10(num, from_notation)
#     return convert_from_10(tmp, to_notation)


def button_click(char, text_input):
    global calc_operator
    calc_operator += str(char)
    text_input.set(calc_operator)

calc_operator = ''

def main():
    tk_calc = Tk()
    tk_calc.configure(bg="#293C4A", bd=10)
    text_input = StringVar()
    rhs_input = StringVar()
    # operator_input = StringVar()
    # notation_input = StringVar()
    tk_calc.title("Calculator")
    lhs_display = Entry(tk_calc, font=('sans-serif', 20, 'bold'), textvariable=text_input,
                     bd=2, insertwidth = 3, bg='#BBB', justify='right',width=10).grid(columnspan=5, padx = 0, pady = 5)
    # notation_display = Entry(tk_calc, font=('sans-serif', 20, 'bold'), textvariable=notation_input,
    #                  bd=5, insertwidth = 5, bg='#BBB', justify='right',width=2).grid(row=0, column=5)
    button_params = {'bd':5, 'fg':'#BBB', 'bg':'#3C3636', 'font':('sans-serif', 20, 'bold')}
    button_params_main = {'bd':5, 'fg':'#000', 'bg':'#BBB', 'font':('sans-serif', 20, 'bold')}
    button_1 = Button(tk_calc, button_params, text='1',
                   command=lambda:button_click('1',text_input)).grid(row=1, column=0, sticky="nesw")
    
    combobox = ttk.Combobox(tk_calc,font=('sans-serif', 10, 'bold'), foreground='#000', state='readonly', width=2,values=list(x for x in range(2,17))).grid(column=5, row=0, sticky='se')
    operator = ttk.Combobox(tk_calc, font=('sans-serif', 20, 'bold'), background="#BBB", foreground="#000", state="readonly", width=1, values=['-','+','*','/']).grid(column=6, row=0, padx=20, pady=5)
    rhs_display = Entry(tk_calc, font=('sans-serif', 20, 'bold'), textvariable=rhs_input,
                     bd=2, insertwidth = 5, bg='#BBB', justify='right',width=10).grid(row=0,column=7,columnspan=2, padx = 10, pady = 5)

    tk_calc.mainloop()

if __name__ == "__main__":
    main()