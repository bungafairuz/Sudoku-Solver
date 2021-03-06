
from BFS_Sudoku import BFS_solve

# grid = [[0,3,0,0,0,1,5,0,0],
#       [0,0,0,5,0,0,0,8,4],
#       [0,0,5,0,0,7,0,6,0],
#       [0,0,0,0,0,0,0,0,0],
#       [0,8,0,2,0,0,0,7,0],
#       [0,0,0,8,5,0,0,0,9],
#       [0,0,3,0,9,4,0,0,7],
#       [0,0,4,0,0,0,0,0,8],
#       [5,0,6,0,1,0,0,0,0]]

grid = [[0,3,0,0,0,1,5,0,0], 
      [0,0,0,5,0,0,0,8,4],
      [0,0,5,0,0,7,0,6,0],
      [0,0,0,0,0,0,0,0,0],
      [0,8,0,2,0,0,0,7,0],
      [0,0,0,8,5,0,0,0,9],
      [0,0,3,0,9,4,0,0,7],
      [0,0,4,0,0,0,0,0,8],
      [5,0,6,0,1,0,0,0,0]]
 
print ("Problem:")
for row in grid:
      print (row)

BFS_solve(grid)