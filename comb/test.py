class CombinatorialScheme:
    def __init__(self, name):
        self.name = name
    def factorial(self, n):
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

    def combinations(self, n, k):
        return self.factorial(n) // (self.factorial(k) * self.factorial(n - k))

    def execute(self):
        pass


class SumRule(CombinatorialScheme):
    def execute(self):
        print("Вы выбрали правило суммы.")
        n = int(input("Мощность множества (n)"))
        k = int(input("Количество (k)"))
        print("Результат:", n * k)


class ProductRule(CombinatorialScheme):
    def execute(self):
        print("Вы выбрали правило произведения.")
        n = int(input("Мощность множества (n)"))
        k = int(input("Количетсво (k)"))
        result = n ** k
        print("Результат:", result)


class PermWithRep(CombinatorialScheme):
    def execute(self):
        print("Вы выбрали перестановки с повторениями.")
        n = int(input("Введите количество элементов (n): "))
        k = int(input("Введите длину перестановки (k): "))
        result = n ** k
        print("Результат:", result)


class PermWithoutRep(CombinatorialScheme):
    def execute(self):
        print("Вы выбрали перестановки без повторений.")
        n = int(input("Введите количество элементов (n): "))
        k = int(input("Введите длину перестановки (k): "))
        result = self.factorial(n) // self.factorial(n - k)
        print("Результат:", self.factorial(n) // self.factorial(n - k))

class CombWithRep(CombinatorialScheme):
    def execute(self):
        print("Вы выбрали сочетания с повторениями.")
        n = int(input("Введите количество элементов (n): "))
        k = int(input("Введите длину сочетания (k): "))
        result = self.combinations(n + k - 1, k)
        print("Результат:", result)

class CombWithoutRep(CombinatorialScheme):
    def execute(self):
        print("Вы выбрали сочетания без повторений.")
        n = int(input("Введите количество элементов (n): "))
        k = int(input("Введите длину сочетания (k): "))
        result = self.combinations(n,k)
        print("Результат:", result)



class ArrangeWithRep(CombinatorialScheme):
    def execute(self):
        print("Вы выбрали размещения с повторениями.")
        n = int(input("Введите количество элементов (n): "))
        k = int(input("Введите длину размещения (k): "))
        print("Результат:", n ** k)


class ArrangeWithoutRep(CombinatorialScheme):
    def execute(self):
        print("Вы выбрали размещения без повторений.")
        n = int(input("Введите количество элементов (n): "))
        k = int(input("Введите длину расстоновки (k): "))
        result = self.factorial(n) // self.factorial(n - k)
        print("Результат:", result)




def main():
    schemes = [
        SumRule("Правило суммы"),
        ProductRule("Правило произведения"),
        PermWithRep("Перестановки с повторениями"),
        PermWithoutRep("Перестановки без повторений"),
        CombWithRep("Сочетания с повторениями"),
        CombWithoutRep("Сочетания без повторений"),
        ArrangeWithRep("Размещения с повторениями"),
        ArrangeWithoutRep("Размещения без повторений")
    ]

    print("Выберите комбинаторную схему:")
    for i, scheme in enumerate(schemes, start=1):
        print(f"{i}. {scheme.name}")

    choice = int(input("Введите номер схемы: "))

    if choice >= 1 and choice <= len(schemes):
        schemes[choice - 1].execute()
    else:
        raise Exception("Вы вышли за границы, попробуйте еще раз")


if __name__ == "__main__":
    main()
