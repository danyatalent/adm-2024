from maze_class import *
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

solver = MazeSolver(maze)
path = solver.find_path()

if path:
    print("Путь найден:")
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if (row, col) in path:
                print("*", end=" ")
            else:
                print(maze[row][col], end=" ")
        print()
else:
    print("Путь не найден.")