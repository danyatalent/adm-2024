class CombinatorialScheme:
    """Базовый класс для комбинаторных схем."""

    def __init__(self, name):
        """
        Инициализация комбинаторной схемы с заданным именем.

        Args:
            name (str): Название комбинаторной схемы.
        """
        self.name = name
    def factorial(self, n):
        """
        Вычисление факториала заданного числа.

        Args:
            n (int): Число, для которого нужно вычислить факториал.

        Returns:
            int: Факториал заданного числа.
        """
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

    def combinations(self, n, k):
        """
        Вычисление числа комбинаций.

        Args:
            n (int): Общее количество элементов.
            k (int): Количество элементов для выбора.

        Returns:
            int: Число комбинаций.
        """
        return self.factorial(n) // (self.factorial(k) * self.factorial(n - k))

    def execute(self, n, k, test_mode):
        """
        Выполнение комбинаторной схемы. Должен быть реализован в подклассах.
        """
        pass


class SumRule(CombinatorialScheme):
    """Реализация правила суммы."""
    def execute(self, n = 0, k = 0, test_mode = False):
        """Выполнение правила суммы."""
        print("Вы выбрали правило суммы.")
        if not test_mode:
            n = int(input("Мощность множества (n): "))
            k = int(input("Количество (k): "))
        result = n * k
        print("Результат:", n * k)
        return result


class ProductRule(CombinatorialScheme):
    """Реализация правила произведения."""
    def execute(self, n = 0, k = 0, test_mode = False):
        """Выполнение правила произведения."""
        print("Вы выбрали правило произведения.")
        if not test_mode:
            n = int(input("Мощность множества (n): "))
            k = int(input("Количетсво (k): "))
        result = n ** k
        print("Результат:", result)
        return result


class PermWithRep(CombinatorialScheme):
    """Реализация перестановок с повторениями."""
    def execute(self, n = 0, k = 0, test_mode = False):
        """Выполнение перестановок с повторениями."""
        print("Вы выбрали перестановки с повторениями.")
        if not test_mode:

            n = int(input("Введите количество элементов (n): "))
            k = int(input("Введите длину перестановки (k): "))
        result = n ** k
        print("Результат:", result)
        return result


class PermWithoutRep(CombinatorialScheme):
    """Реализация перестановок без повторений."""
    def execute(self, n = 0, k = 0, test_mode = False):
        """Выполнение перестановок без повторений."""
        print("Вы выбрали перестановки без повторений.")
        if not test_mode:
            n = int(input("Введите количество элементов (n): "))
            k = int(input("Введите длину перестановки (k): "))
        result = self.factorial(n) // self.factorial(n - k)
        print("Результат:", self.factorial(n) // self.factorial(n - k))
        return result

class CombWithRep(CombinatorialScheme):
    """Реализация сочетаний с повторениями."""
    def execute(self, n = 0, k = 0, test_mode = False):
        """Выполнение сочетаний с повторениями."""
        print("Вы выбрали сочетания с повторениями.")
        if not test_mode:
            n = int(input("Введите количество элементов (n): "))
            k = int(input("Введите длину сочетания (k): "))
        result = self.combinations(n + k - 1, k)
        print("Результат:", result)
        return result

class CombWithoutRep(CombinatorialScheme):
    """Реализация сочетаний без повторений."""

    def execute(self, n = 0, k = 0, test_mode = False):
        """Выполнение сочетаний без повторений."""
        print("Вы выбрали сочетания без повторений.")
        if not test_mode:
            n = int(input("Введите количество элементов (n): "))
            k = int(input("Введите длину сочетания (k): "))
        result = self.combinations(n,k)
        print("Результат:", result)
        return result



class ArrangeWithRep(CombinatorialScheme):
    """Реализация размещений с повторениями."""

    def execute(self, n = 0, k = 0, test_mode = False):
        """Выполнение размещений с повторениями."""
        print("Вы выбрали размещения с повторениями.")
        if not test_mode:
            n = int(input("Введите количество элементов (n): "))
            k = int(input("Введите длину размещения (k): "))
        print("Результат:", n ** k)
        return n ** k


class ArrangeWithoutRep(CombinatorialScheme):
    """Реализация размещений без повторений."""

    def execute(self, n = 0, k = 0, test_mode = False):
        """Выполнение размещений без повторений."""
        print("Вы выбрали размещения без повторений.")
        if not test_mode:
            n = int(input("Введите количество элементов (n): "))
            k = int(input("Введите длину расстоновки (k): "))
        result = self.factorial(n) // self.factorial(n - k)
        print("Результат:", result)
        return result





