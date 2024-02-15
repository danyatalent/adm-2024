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
            tmp = (Digits[num % notation] if num % notation >= 10 else str(num % notation)) + tmp
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
            self.number = '-' + tmp
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
            self.number = '-' + str(tmp + tmp_num)
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
    print(notation)
    lhs.convert_to_10(lhs.notation)
    rhs.convert_to_10(rhs.notation)
    tmp = str(float(lhs.number) + float(rhs.number))
    if notation == 16:
        tmp = hex(int(float(tmp)))
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
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F',
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15}


def button_click(char, text_input):
    global calc_operator
    calc_operator += str(char)
    text_input.set(calc_operator)


def clear_display(text_input):
    global calc_operator
    calc_operator = ''
    text_input.set("")


def calculate(text_input):
    try:
        result = eval(calc_operator)
        text_input.set(str(result))
        print(text_input.get())
    except Exception as e:
        text_input.set("Error")


def change_base(base, text_input):
    global current_base, calc_operator, lhs_display
    current_base = base
    calc_operator = ''  # Reset the calculation operator when changing base
    update_buttons()
    text_input.set(calc_operator)  # Update the input window with an empty string
    lhs_display.destroy()  # Destroy the existing input field
    lhs_display = Entry(tk_calc, font=('sans-serif', 20, 'bold'), textvariable=text_input,
                        bd=2, insertwidth=3, bg='#BBB', justify='right', width=10)
    lhs_display.grid(row=0, column=0, columnspan=5, padx=0, pady=5)


def update_buttons():
    global current_base
    for button in numeric_buttons:
        button.config(state=NORMAL)
    for letter_button in letter_buttons:
        letter_button.config(state=DISABLED)
    if current_base == 2:
        for i in range(2, 10):
            numeric_buttons[i - 1].config(state=DISABLED)
    elif current_base == 8:
        for i in range(8, 10):
            numeric_buttons[i - 1].config(state=DISABLED)
    elif current_base == 16:
        for letter_button in letter_buttons:
            letter_button.config(state=NORMAL)


def main():
    global current_base, calc_operator, numeric_buttons, lhs_display, letter_buttons
    current_base = 10
    calc_operator = ''
    global tk_calc
    tk_calc = Tk()
    tk_calc.configure(bg="#293C4A", bd=50)
    text_input = StringVar()

    tk_calc.title("Calculator")

    lhs_display = Entry(tk_calc, font=('sans-serif', 20, 'bold'), textvariable=text_input,
                        bd=2, insertwidth=3, bg='#BBB', justify='right', width=10)
    lhs_display.grid(row=0, column=0, columnspan=5, padx=0, pady=5)
    button_params = {'bd': 5, 'fg': '#BBB', 'bg': '#3C3636', 'font': ('sans-serif', 20, 'bold')}

    # Numeric Buttons
    numeric_buttons = []
    for i in range(1, 10):
        button = Button(tk_calc, button_params, text=str(i), command=lambda i=i: button_click(i, text_input))
        button.grid(row=(i - 1) // 3 + 1, column=(i - 1) % 3, sticky="nesw")
        numeric_buttons.append(button)
    Button(tk_calc, button_params, text='0', command=lambda: button_click('0', text_input)).grid(row=4, column=1,
                                                                                                 sticky="nesw")

    # Adding letter buttons for hexadecimal system
    letter_buttons_title = ['A', 'B', 'C', 'D', 'E', 'F']
    letter_buttons = []
    for i, letter in enumerate(letter_buttons_title):
        button = Button(tk_calc, button_params, text=letter, command=lambda letter=letter: button_click(letter, text_input))
        button.grid(row=5, column=i, sticky="nesw")
        letter_buttons.append(button)

    # Arithmetic operation buttons
    Button(tk_calc, button_params, text='+', command=lambda: button_click('+', text_input)).grid(row=1, column=3,
                                                                                                 sticky="nesw")
    Button(tk_calc, button_params, text='-', command=lambda: button_click('-', text_input)).grid(row=2, column=3,
                                                                                                 sticky="nesw")
    Button(tk_calc, button_params, text='*', command=lambda: button_click('*', text_input)).grid(row=3, column=3,
                                                                                                 sticky="nesw")
    Button(tk_calc, button_params, text='/', command=lambda: button_click('/', text_input)).grid(row=4, column=3,
                                                                                                 sticky="nesw")

    # Other buttons
    Button(tk_calc, button_params, text='C', command=lambda: clear_display(text_input)).grid(row=1, column=4,
                                                                                             sticky="nesw")
    Button(tk_calc, button_params, text='=', command=lambda: calculate(text_input)).grid(row=2, column=4, rowspan=3,
                                                                                         sticky="nesw")

    # Base change buttons
    base_buttons = [("Dec", 10), ("Hex", 16), ("Oct", 8), ("Bin", 2)]
    for base_name, base_value in base_buttons:
        Button(tk_calc, button_params, text=base_name,
               command=lambda base_value=base_value: change_base(base_value, text_input)).grid(
            row=0, column=base_buttons.index((base_name, base_value)), sticky="nesw")

    tk_calc.mainloop()


if __name__ == "__main__":
    main()
