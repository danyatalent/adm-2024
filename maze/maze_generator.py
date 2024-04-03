import random

def generate_maze(size):
    maze = [[0 for _ in range(size)] for _ in range(size)]

    # Установка начальной и конечной точек
    maze[0][0] = 0  # Начало
    maze[size - 1][size - 1] = 2  # Конец

    # Создание случайных стен в лабиринте
    for i in range(size):
        for j in range(size):
            if random.random() < 0.3:  # Шанс создания стены
                maze[i][j] = 1  # Стена

    return maze

# Генерация лабиринта 5x5
maze_example = generate_maze(5)

# Вывод лабиринта
print("Пример лабиринта:")
for row in maze_example:
    print(row)
