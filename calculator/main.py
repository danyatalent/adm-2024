# Выполнили: Каневский Даниил, Труфманов Михаил, Махров Матвей

from tkinter import *
from tkinter import ttk
from calculator import Calculator
from number import Number


def calculate(answer_output: StringVar, cal: Calculator):
    try:
        answer_output.set("")
        result = cal.calculate()
        answer_output.set(result.number)
    except Exception as e:
        answer_output.set("Error")


def main():
    global current_base, calc_operator, numeric_buttons, lhs_display, letter_buttons
    current_base = 10
    calc_operator = ''
    #print(Number(10,10).number)
    global tk_calc
    tk_calc = Tk()
    tk_calc.configure(bg="#293C4A", bd=50)
    lhs_input = StringVar()
    rhs_input = StringVar()
    ans_output = StringVar()

    lhs_notation = StringVar(value='10')
    rhs_notation = StringVar(value='10')
    ans_notation = StringVar(value='10')


    tk_calc.title("Calculator")

    lhs_display = Entry(tk_calc, font=('sans-serif', 20, 'bold'), textvariable=lhs_input,
                        bd=2, insertwidth=3, bg='#BBB', justify='right', width=10)
    lhs_display.grid(row=1, column=0, columnspan=4, padx=0, pady=0, sticky="w")

    rhs_display = Entry(tk_calc, font=('sans-serif', 20, 'bold'), textvariable=rhs_input,
                        bd=2, insertwidth=3, bg='#BBB', justify='right', width=10)
    rhs_display.grid(row=1, column=3, columnspan=3, padx=0, pady=0, sticky="e")
    
    ans_display = Entry(tk_calc, font=('sans-serif', 20, 'bold'), textvariable=ans_output,
                        bd=2, insertwidth=3, bg='#BBB', justify='left', width=10).grid(row=3, column=0, sticky="s")
    button_params = {'bd': 5, 'fg': '#BBB', 'bg': '#3C3636', 'font': ('sans-serif', 20, 'bold')}
    lhs_label = Label(tk_calc,font=('sans-serif', 10, 'bold'),text="1st number", bg="#293C4A", fg="#BBB").grid(row=0, column=0, sticky="w")
    rhs_label = Label(tk_calc,font=('sans-serif', 10, 'bold'),text="2nd number", bg="#293C4A", fg="#BBB").grid(row=0, column=3)
    ans_label = Label(tk_calc,font=('sans-serif', 10, 'bold'),text="Answer", bg="#293C4A", fg="#BBB").grid(row=4, column=0, sticky="w")


    # Comboboxes for notation
    lhs_combo = ttk.Combobox(tk_calc, state="readonly", height=5, values=list(x for x in range(2, 17)), font=('sans-serif', 10, 'bold'), width=2, 
                             textvariable=lhs_notation).grid(row=1, column=1,sticky="ws")
    rhs_combo = ttk.Combobox(tk_calc, state="readonly", height=5, values=list(x for x in range(2, 17)), font=('sans-serif', 10, 'bold'), width=2, 
                             textvariable=rhs_notation).grid(row=1, column=6,sticky="ws")
    ans_combo = ttk.Combobox(tk_calc, state="readonly", height=5, values=list(x for x in range(2, 17)), font=('sans-serif', 10, 'bold'), width=2, 
                             textvariable=ans_notation).grid(row=3, column=1,sticky="ws")


    # Arithmetic operation buttons
    Button(tk_calc, button_params, text='+', command=lambda: calculate(ans_output, Calculator(Number(lhs_input.get(), int(lhs_notation.get())), 
                                                                                              Number(rhs_input.get(), int(rhs_notation.get())),
                                                                                              '+', int(ans_notation.get())))).grid(row=2, column=0,
                                                                                                 sticky="w", pady=10)
    Button(tk_calc, button_params, text='-', command=lambda: calculate(ans_output, Calculator(Number(lhs_input.get(), int(lhs_notation.get())), 
                                                                                              Number(rhs_input.get(), int(rhs_notation.get())),
                                                                                              '-', int(ans_notation.get())))).grid(row=2, column=1,
                                                                                                 sticky="nesw", pady=10)
    Button(tk_calc, button_params, text='*', command=lambda: calculate(ans_output, Calculator(Number(lhs_input.get(), int(lhs_notation.get())), 
                                                                                              Number(rhs_input.get(), int(rhs_notation.get())),
                                                                                              '*', int(ans_notation.get())))).grid(row=2, column=2,
                                                                                                 sticky="nesw", pady=10)
    Button(tk_calc, button_params, text='/', command=lambda: calculate(ans_output, Calculator(Number(lhs_input.get(), int(lhs_notation.get())), 
                                                                                              Number(rhs_input.get(), int(rhs_notation.get())),
                                                                                              '/', int(ans_notation.get())))).grid(row=2, column=3,
                                                                                                 sticky="nesw", pady=10)

    tk_calc.mainloop()


if __name__ == "__main__":
    main()
