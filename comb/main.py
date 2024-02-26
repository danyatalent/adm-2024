from combination import *

def main():
    """Главная функция для выполнения программы."""
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
        schemes[choice - 1].execute(test_mode=0)
    else:
        raise Exception("Вы вышли за границы, попробуйте еще раз")


if __name__ == "__main__":
    main()
