import numpy as np
import matplotlib.pyplot as plt
import time
from matplotlib.colors import Normalize
import matplotlib.cm

# GLOBAL VARIABLE
t = 0

# ===========================================================================
# 1: Drawing
# ===========================================================================

def draw(matrix, title=None, cmap_name="viridis", close=True):   # close controls if its going to be a video
    global t
    t += 1
    # Validate the matrix contains only natural numbers
    if not np.all(np.array(matrix) >= 0):
        raise ValueError("The matrix should only contain natural numbers (≥0).")
    
    # Create a colormap and normalization based on the matrix's values
    #cmap = get_cmap(cmap_name)
    cmap = matplotlib.cm.Blues(np.linspace(0,1,20))
    cmap = matplotlib.colors.ListedColormap(cmap[10:,:-1])
    norm = Normalize(vmin=np.min(matrix), vmax=np.max(matrix))
    
    # Plot the matrix with colors based on the values
    fig = plt.figure(figsize=(8, 6))
    plt.imshow(matrix, cmap=cmap, norm=norm, aspect='auto')
    plt.colorbar(label="Grains of sand")

    if title:
      plt.title(title)
    else:
      plt.title(f'Sand pile at time {t}')

    # ----- Annotate cell value -----
    #for i in range(matrix.shape[0]):
    #    for j in range(matrix.shape[1]):
    #        plt.text(j, i, str(matrix[i, j]), ha='center', va='center', color='white', fontsize=8)
    # ----- Annotate cell value -----
    
    if close:
        plt.show(block=False)
        plt.pause(.1)
        plt.close()

        #fig.canvas.draw_idle()  # Update the figure without clearing it
        #plt.pause(0.3)  # Short pause to allow the figure to be displayed
        #plt.clf()
    else: 
        plt.show()

# ===========================================================================
# 2: Game rules
# ===========================================================================

def is_unstable(grid):
  for i in range(len(grid)):
    for j in range(len(grid)):
      if grid[i, j] >= 4:
        return True
  return False

def topple(x, y, grid):
  # Get grid dimensions
  n = len(grid)

  grid[x, y] -= 4

  if 0 < (x + 1) < n:
    grid[x + 1, y] += 1
  if 0 <= (x - 1) < n:
    grid[x - 1, y] += 1
  if 0 < (y + 1) < n:
    grid[x, y + 1] += 1
  if 0 <= (y - 1) < n:
    grid[x, y - 1] += 1

def add_grain(x, y, grid, draw_it=True):
  grid[x, y] += 1
  if draw_it: draw(grid)

  # If the point has become unstable, topple it
  if grid[x, y] >= 4:
    topple(x, y, grid)
    if draw_it: draw(grid)

    # Now, traverse the grid in search of new unstable point
    while is_unstable(grid):
      for i in range(len(grid)):
        for j in range(len(grid)):
          if grid[i, j] >= 4:
            topple(i, j, grid)
            if draw_it: draw(grid)

def add_grains(m, x, y, grid, draw_it=True):
  for _ in range(m):
    add_grain(x, y, grid, draw_it)

# ===========================================================================
# 3: Test
# ===========================================================================
#n = 100
#grid = np.zeros((n,n))
#add_grains(1000, 0, 0, grid)

#draw(grid, close = False)

