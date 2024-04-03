#Выполнил Труфманов Михаил
from maze_class import *
from maze_generator import *
rows, cols = 0, 0
rows = int(input("Введите значение rows лабиринта: "))
cols = int(input("Введите значение cols лабиринта: "))
maze_generator = MazeGenerator(rows, cols)
maze = maze_generator.generate_maze()
for row in maze:
    print(' '.join(row))

solver = MazeSolver(maze)
solution = solver.solve_maze()

if solution:
    print("Path found:")
    for step in reversed(solution):
        print(step)
else:
    print("No path found")