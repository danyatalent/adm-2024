# БПМ-22-1
# Выполнили: Каневский Даниил, Махров Матвей, Труфманов Михаил

# Узел дерева с указателями на левого и правого потомков
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Двоичное дерево
class BinaryTree:
    def __init__(self):
        self.root = None

    # Добавление узла
    def add_element(self, value):
        # Если нет корня дерева
        if not self.root:
            self.root = TreeNode(value)
        else:
            # Вызов рекурсивной функции от корня
            self._add_element_recursive(self.root, value)
        
        print("Элемент", value, "успешно добавлен.")

    # Добавление вершинв с сортировкой по возрастанию
    def _add_element_recursive(self, current_node, value):
        # Если добавляемый узел меньше текущей вершины
        if value < current_node.value:
            # У текущей вершины нет потомков
            if current_node.left is None:
                current_node.left = TreeNode(value)
            # Вызов функции от левого потомка
            else:
                self._add_element_recursive(current_node.left, value)
        else:
            # У текущей вершины нет потомков
            if current_node.right is None:
                current_node.right = TreeNode(value)
            # Вызов фунции от правого потомка
            else:
                self._add_element_recursive(current_node.right, value)

    # Удаление вершины
    def delete_element(self, value):
        self.root = self._delete_element_recursive(self.root, value)
        print("Элемент", value, "был удалён.")

    # Удаление вершины с сортировкой по возрастанию
    def _delete_element_recursive(self, current_node, value):
        # Текущей вершины не существует
        if current_node is None:
            return None

        # Удаляемый узел меньше текущей вершины
        if value < current_node.value:
            # Левый потомок текущей вершины - результат функции
            current_node.left = self._delete_element_recursive(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self._delete_element_recursive(current_node.right, value)
        else:
            # У текущей вершины нет левого потомка
            if current_node.left is None:
                return current_node.right
            # У текущей вершины нет правого потомка
            elif current_node.right is None:
                return current_node.left
            else:
                min_value = self._find_min_value(current_node.right)
                # Текущая вершина минимизируется
                current_node.value = min_value
                # Правый потомок текущей вершины - результат функции
                current_node.right = self._delete_element_recursive(current_node.right, min_value)

        return current_node

    # Поиск минимального значения для функции удаления
    def _find_min_value(self, node):
        # Пока есть левый потомок
        while node.left is not None:
            node = node.left
        return node.value

    # Вывод дерева
    def show(self):
        print("Связное дерево:")
        self._inorder_traversal(self.root)

    # Проход по всем потомкам
    def _inorder_traversal(self, node):
        if node is not None:
            self._inorder_traversal(node.left)
            print(node.value)
            self._inorder_traversal(node.right)

def main():
    tree = BinaryTree()

    while True:
        print("\n1. Добавить элемент")
        print("2. Удалить элемент")
        print("3. Вывести дерево")
        print("4. Выход")

        choice = int(input("Введите номер операции: "))

        if choice == 4:
            break

        if choice == 1:
            element = input("Введите элемент для добавления: ")
            tree.add_element(element)
        elif choice == 2:
            element = input("Введите элемент для удаления: ")
            tree.delete_element(element)
        elif choice == 3:
            tree.show()
        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    main()