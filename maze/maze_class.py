class MazeSolver:
    def __init__(self, maze):
        self.maze = maze
        self.rows = len(maze)
        self.cols = len(maze[0])
        self.visited = [[False] * self.cols for _ in range(self.rows)]

    def solve_maze(self):
        start_pos = self.find_start()
        if start_pos:
            path = []
            if self.solve_recursive(start_pos[0], start_pos[1], path):
                return path
        return None

    def solve_recursive(self, row, col, path):
        if not self.is_valid_position(row, col):
            return False

        if self.maze[row][col] == 'F':
            path.append((row, col))
            return True

        if self.visited[row][col]:
            return False

        self.visited[row][col] = True

        if self.solve_recursive(row + 1, col, path) or \
           self.solve_recursive(row - 1, col, path) or \
           self.solve_recursive(row, col + 1, path) or \
           self.solve_recursive(row, col - 1, path):
            path.append((row, col))
            return True

        return False

    def is_valid_position(self, row, col):
        return 0 <= row < self.rows and 0 <= col < self.cols and self.maze[row][col] != 'W' and not self.visited[row][col]

    def find_start(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.maze[i][j] == 'S':
                    return i, j
        return None


maze = [
    ['S', ' ', ' ', 'W'],
    ['W', 'W', ' ', 'W'],
    [' ', ' ', ' ', ' '],
    ['W', ' ', 'W', 'F']
]

solver = MazeSolver(maze)
solution = solver.solve_maze()

if solution:
    print("Path found:")
    for step in reversed(solution):
        print(step)
else:
    print("No path found")
