import random

class MazeGenerator:
    """
    Класс MazeGenerator предназначен для генерации лабиринта методом "Recursive Backtracking".

    Атрибуты:
        rows (int): Количество строк в лабиринте.
        cols (int): Количество столбцов в лабиринте.
        maze (list): Двумерный массив, представляющий лабиринт.
    """

    def __init__(self, rows, cols):
        """
        Инициализирует объект MazeGenerator.

        Параметры:
            rows (int): Количество строк в лабиринте.
            cols (int): Количество столбцов в лабиринте.
        """
        self.rows = rows
        self.cols = cols
        self.maze = [['W' for _ in range(cols)] for _ in range(rows)]

    def generate_maze(self):
        """
        Генерирует лабиринт методом "Recursive Backtracking".

        Возвращает:
            list: Двумерный массив, представляющий сгенерированный лабиринт.
        """
        self.carve_passage(0, 0)
        self.maze[0][0] = 'S'
        self.maze[self.rows - 1][self.cols - 1] = 'F'
        return self.maze

    def carve_passage(self, row, col):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        random.shuffle(directions)

        for dr, dc in directions:
            next_row, next_col = row + 2 * dr, col + 2 * dc
            if 0 <= next_row < self.rows and 0 <= next_col < self.cols and self.maze[next_row][next_col] == 'W':
                self.maze[row + dr][col + dc] = ' '
                self.maze[next_row][next_col] = ' '
                self.carve_passage(next_row, next_col)

        self.maze[self.rows - 2][self.cols - 1] = ' '




# Вывод сгенерированного лабиринта
