from maze_gen import Maze

# size of maze
nx, ny = 40, 40

# start position
ix, iy = 0, 0

maze = Maze(nx, ny, ix, iy)
maze.generate_maze_df()

print(maze)
maze.write_svg('maze.svg')