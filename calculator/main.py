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


def clear_display(text_input):
    global calc_operator
    calc_operator = ''
    text_input.set("")

def calculate(text_input):
    try:
        result = eval(calc_operator)
        text_input.set(str(result))
    except Exception as e:
        text_input.set("Error")

def main():
    tk_calc = Tk()
    tk_calc.configure(bg="#293C4A", bd=10)
    text_input = StringVar()
    tk_calc.title("Calculator")

    lhs_display = Entry(tk_calc, font=('sans-serif', 20, 'bold'), textvariable=text_input,
                     bd=2, insertwidth=3, bg='#BBB', justify='right', width=10)
    lhs_display.grid(columnspan=5, padx=0, pady=5)

    button_params = {'bd':5, 'fg':'#BBB', 'bg':'#3C3636', 'font':('sans-serif', 20, 'bold')}

    # Numeric Buttons
    for i in range(1, 10):
        Button(tk_calc, button_params, text=str(i), command=lambda i=i: button_click(i, text_input)).grid(row=(i-1)//3+1, column=(i-1)%3, sticky="nesw")
    Button(tk_calc, button_params, text='0', command=lambda: button_click('0', text_input)).grid(row=4, column=1, sticky="nesw")

    # Arithmetic operation buttons
    Button(tk_calc, button_params, text='+', command=lambda: button_click('+', text_input)).grid(row=1, column=3, sticky="nesw")
    Button(tk_calc, button_params, text='-', command=lambda: button_click('-', text_input)).grid(row=2, column=3, sticky="nesw")
    Button(tk_calc, button_params, text='*', command=lambda: button_click('*', text_input)).grid(row=3, column=3, sticky="nesw")
    Button(tk_calc, button_params, text='/', command=lambda: button_click('/', text_input)).grid(row=4, column=3, sticky="nesw")

    # Other buttons
    Button(tk_calc, button_params, text='C', command=lambda: clear_display(text_input)).grid(row=1, column=4, sticky="nesw")
    Button(tk_calc, button_params, text='=', command=lambda: calculate(text_input)).grid(row=2, column=4, rowspan=3, sticky="nesw")

    tk_calc.mainloop()

if __name__ == "__main__":
    main()