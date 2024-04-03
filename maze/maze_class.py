from maze_generator import *
class MazeSolver:
    """
    Класс MazeSolver предназначен для решения лабиринта, представленного в виде двумерного массива.

    Attributes:
        maze (list): Двумерный массив, представляющий лабиринт.
        rows (int): Количество строк в лабиринте.
        cols (int): Количество столбцов в лабиринте.
        visited (list): Двумерный массив, отслеживающий посещенные ячейки лабиринта.

    Methods:
        solve_maze(): Пытается найти путь от стартовой позиции 'S' до целевой позиции 'F' в лабиринте.
                     Возвращает путь в виде списка координат, если путь найден, иначе возвращает None.
        solve_recursive(row, col, path): Вспомогательная рекурсивная функция для поиска пути в лабиринте.
        is_valid_position(row, col): Проверяет, является ли указанная позиция в лабиринте допустимой.
        find_start(): Находит начальную позицию 'S' в лабиринте.
    """

    def __init__(self, maze):
        """
        Инициализирует объект MazeSolver с заданным лабиринтом.

        Args:
            maze (list): Двумерный массив, представляющий лабиринт.
        """
        self.maze = maze
        self.rows = len(maze)
        self.cols = len(maze[0])
        self.visited = [[False] * self.cols for _ in range(self.rows)]

    def solve_maze(self):
        """
        Пытается найти путь от стартовой позиции 'S' до целевой позиции 'F' в лабиринте.

        Returns:
            list or None: Путь в виде списка координат, если путь найден, иначе None.
        """
        start_pos = self.find_start()
        if start_pos:
            path = []
            if self.solve_recursive(start_pos[0], start_pos[1], path):
                return path
        return None

    def solve_recursive(self, row, col, path):
        """
        Вспомогательная рекурсивная функция для поиска пути в лабиринте.

        Args:
            row (int): Текущая строка в лабиринте.
            col (int): Текущий столбец в лабиринте.
            path (list): Список координат, представляющих текущий путь.

        Returns:
            bool: True, если путь найден, иначе False.
        """
        if not self.is_valid_position(row, col):
            return False

        if self.maze[row][col] == 'F':
            path.append((row, col))
            return True

        if self.visited[row][col]:
            return False

        self.visited[row][col] = True

        if (self.solve_recursive(row + 1, col, path) or
           self.solve_recursive(row - 1, col, path) or
           self.solve_recursive(row, col + 1, path) or
           self.solve_recursive(row, col - 1, path)):
            path.append((row, col))
            return True

        return False

    def is_valid_position(self, row, col):
        """
        Проверяет, является ли указанная позиция в лабиринте допустимой.

        Args:
            row (int): Проверяемая строка в лабиринте.
            col (int): Проверяемый столбец в лабиринте.

        Returns:
            bool: True, если позиция допустима, иначе False.
        """
        return 0 <= row < self.rows and \
               0 <= col < self.cols and \
               self.maze[row][col] != 'W' and \
               not self.visited[row][col]

    def find_start(self):
        """
        Находит начальную позицию 'S' в лабиринте.

        Returns:
            tuple or None: Координаты начальной позиции 'S', если найдена, иначе None.
        """
        for i in range(self.rows):
            for j in range(self.cols):
                if self.maze[i][j] == 'S':
                    return i, j
        return None



