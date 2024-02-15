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

    def __truediv__(self, other):
        return division(self, other)
    
def add(lhs: Number, rhs: Number, notation: int = 10) -> Number:
    #print(notation)
    lhs.convert_to_10(lhs.notation)
    rhs.convert_to_10(rhs.notation)
    tmp = str(float(lhs.number) + float(rhs.number))
    if notation == 16:
        tmp = hex(int(float(tmp)))
    return Number(tmp)


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
        return Number(tmp, notation)
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
