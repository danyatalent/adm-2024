# БПМ-22-1
# Выполнили: Каневский Даниил, Махров Матвей, Труфманов Михаил

# Смежная последовательность
class AdjacencySequence:
    def __init__(self, sequence):
        self.sequence = sequence

    def __str__(self):
        return str(self.sequence)

    # Вывод элемента на позиции
    def access(self, index):
        if 0 <= index < len(self.sequence):
            return self.sequence[index]
        else:
            raise IndexError("Индекс вне последовательности")

    # Добавление элемента
    def append(self, data):
        self.sequence.append(data)
        print("Элемент", data, "успешно добавлен.")
    
    # Добавление элемента на позицию
    def insert(self, data, index):
        self.sequence.insert(index, data)
        print("Элемент", data, "успешно добавлен.")

    # Удаление элемента с позиции
    def delete(self, index):
        del self.sequence[index]
        print("Элемент с позиции", index, "был удалён.")

    # Вывод длины последовательности
    def length(self):
        return len(self.sequence)
    
    # Вывод последовательности
    def show(self):
        print("Смежная последовательность:", end=" ")
        print(self)

# Элемент последовательности
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Связная последовательность
class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.head is None:
            return "Последовательность пуста"
        result = ""
        current = self.head
        while current is not None:
            result += str(current.data) + " "
            current = current.next
        return result

    # Добавление элемента
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            print("Элемент", data, "успешно добавлен.")
            return
        
        last = self.head

        # обновление указателей
        while last.next:
            last = last.next
        last.next = new_node
        
        print("Элемент", data, "успешно добавлен.")

    # Вывод элемента на позиции
    def access(self, index):
        current = self.head
        count = 0
        while current:
            if count == index:
                return current.data
            count += 1
            current = current.next
        raise IndexError("Индекс вне последовательности")

    # Добавление элемента на позицию
    def insert(self, data, index):
        new_node = Node(data)
        # добавление в начало
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for i in range(index - 1):
                current = current.next
            # обновление указателей
            new_node.next = current.next
            current.next = new_node

        print("Элемент", data, "успешно добавлен.")

    # Удаление элемента с позиции
    def delete(self, index):
        # удаление из начала
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for i in range(index - 1):
                current = current.next
            current.next = current.next.next
        
        print("Элемент с позиции", index, "был удалён.")

    # Вывод длины последовательности
    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    
    # Вывод последовательности
    def show(self):
        temp = self.head
        print("Связная последовательность:", end=" ")
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

# Консоль
def main():
    while True:
        seq_type = input("Выберите тип последовательности (смежная - 1, связная - 2): ")
        
        if seq_type == "1":
            adj_seq = input("Введите последовательность через пробел: ").split(' ')
            seq = AdjacencySequence(adj_seq)
            break
        elif seq_type == "2":
            seq = LinkedList()
            break
        else:
            print("Неверный тип последовательности.")
            continue
    
    while True:
        print("\nОперации:")
        print("1. Добавить элемент")
        print("2. Удалить элемент")
        print("3. Вывести длину последовательности")
        print("4. Вывести всю последовательность")
        print("5. Выход")
        choice = int(input("Введите номер операции: "))

        if choice == 5:
            break

        if choice == 1:
            element = input("Введите элемент для добавления: ")
            ind = input("Введите позицию (можно оставить пустым (Enter) - добавление в конец): ")
            if ind != '':
                seq.insert(element, int(ind))
            else: 
                seq.append(element)

        elif choice == 2:
            indx = int(input("Введите индекс для удаления: "))
            seq.delete(indx)
            
        elif choice == 3:
            print("Размерность:", seq.length())

        elif choice == 4:
            seq.show()
            print()

        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    main()