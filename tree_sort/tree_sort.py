# БПМ-22-1
# Выполнили: Каневский Даниил, Махров Матвей, Труфманов Михаил

# Вершина дерева
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Вставка вершины
def insert(root, key):
    # Корень дерева отсутствует
    if root is None:
        return Node(key)
    else:
        # Добаляемая вершина меньше корня
        if key < root.key:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

# Проход по всем потомкам
def in_order_traversal(root, result):
    # Если корень дерева есть
    if root is not None:
        # проходим по левому поддереву
        in_order_traversal(root.left, result)
        # добавление корня в результирующее дерево
        result.append(root.key)
        # проходим по правому поддереву
        in_order_traversal(root.right, result)

# Сортировка двоичного дерева
def tree_sort(arr):
    root = None
    for key in arr:
        root = insert(root, key)
    
    result = []
    in_order_traversal(root, result)
    return result

# Блочная (карманная) сортировка
def bucket_sort(arr):
    # Максимальный элемент в массиве
    max_value = max(arr)
    # Оптимальный размер блока
    size = max_value/len(arr)

    # Создаем список корзин
    buckets = [[] for _ in range(len(arr))]
    
    # Распределяем элементы по блокам
    for i in range(len(arr)):
        j = int(arr[i] / size)

        # добавляем элемент в блок j
        if j != len(arr):
            buckets[j].append(arr[i])
            
        # добавляем элемент в последний блок
        else:
            buckets[len(arr) - 1].append(arr[i])
    
    # Сортировка каждой корзины с помощью сортировки вставкой
    for bucket in buckets:
        insertion_sort(bucket)
    
    # Объединение корзин
    sorted_arr = []
    for bucket in buckets:
        sorted_arr += bucket
    
    return sorted_arr

# Сортировка вставкой
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # сдвигаем текущий элемент направо
        # если он больше key
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def main():
    arr = [int(x) for x in input("Введите последовательность через пробел: ").split(' ')]

    while True:
        choice = input("Выберите алгоритм сортировки (на дереве - 1, блочная - 2): ")
        if choice == '1':
            sorted_arr = tree_sort(arr)
            break
        elif choice == '2':
            sorted_arr = bucket_sort(arr)
            break
        else:
            print("Неверный выбор.")
    
    print("Отсортированная последовательность:", sorted_arr)

if __name__ == "__main__":
    main()