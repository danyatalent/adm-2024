# БПМ-22-1
# Выполнили: Каневский Даниил, Махров Матвей, Труфманов Михаил

# Смежное представление
class ContiguousArray:
    def __init__(self):
        self.array = []

    # Добавление элемента
    def add_element(self, value):
        self.array.append(value)
        print("Элемент", value, "успешно добавлен.")

    # Удаление элемента
    def delete_element(self, value):
        if value in self.array:
            self.array.remove(value)
            print("Элемент", value, "был удалён.")
        else:
            print("Элемент не найден.")

    # Вывод размерности массива
    def length(self):
        return len(self.array)

    # Вывод массива
    def show(self):
        print(self.array)
        for value in self.array:
            print("Смежный массив:")
            print(value)

# Элемент связного массива
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Связное представление
class LinkedArray:
    def __init__(self):
        self.head = None

    # Добавление элемента
    def add_element(self, value):
        # Обновляется ссылка на следующий элемент
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        print("Элемент", value, "успешно добавлен.")

    # Удаление элемента
    def delete_element(self, value):
        # Поиск элемента и обновление ссылок
        temp = self.head
        prev = None
        if temp is not None and temp.data == value:
            self.head = temp.next
            temp = None
            print("Элемент", value, "был удалён.")
            return
        while temp is not None:
            if temp.data == value:
                break
            prev = temp
            temp = temp.next
        if temp == None:
            print("Элемент не найден.")
            return
        prev.next = temp.next
        temp = None
        print("Элемент", value, "был удалён.")

    # Вывод размерности массива
    def length(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    # Вывод массива
    def show(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

# Консоль
def main():
    contig_array = ContiguousArray()
    linked_array = LinkedArray()

    array_type = input("Выберите тип массива (смежный - 1, связный - 2): ")
    while True:
        if array_type == "1":
            array = contig_array
            break
        elif array_type == "2":
            array = linked_array
            break
        else:
            print("Неверный тип массива.")
            continue
    
    while True:
        print("\nОперации:")
        print("1. Добавить элемент")
        print("2. Удалить элемент")
        print("3. Вывести размерность")
        print("4. Вывести весь массив")
        print("5. Выход")
        choice = int(input("Введите номер операции: "))

        if choice == 5:
            break

        if choice == 1:
            element = input("Введите элемент для добавления: ")
            array.add_element(element)
        elif choice == 2:
            element = input("Введите элемент для удаления: ")
            array.delete_element(element)
        elif choice == 3:
            print("Размерность:", array.length())
        elif choice == 4:
            print("Массив: ")
            array.show()
        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    main()