import numpy as np
from sandpiles import draw

def topple(config, n, m):
    """
    Config is the unstable sandpile,
    n and m are the height and width of the grid.
    """
    B = config.copy()  # Copy the input configuration
    check = 0  # Used to check if configuration is stable

    while check < n * m:
        check = 0  # Reset the stability counter
        
        for i in range(n):
            for j in range(m):
                if B[i, j] < 4:  # Vertex is stable
                    check += 1  # Count stable vertices

                if B[i, j] >= 4:  # Unstable vertex
                    B[i, j] -= 4  # Subtract 4 grains from unstable vertex

                    # Add grains to neighboring vertices
                    if i + 1 < n:
                        B[i + 1, j] += 1  # Add a grain to the below neighbor
                    if i - 1 >= 0:
                        B[i - 1, j] += 1  # Add a grain to the above neighbor
                    if j + 1 < m:
                        B[i, j + 1] += 1  # Add a grain to the right neighbor
                    if j - 1 >= 0:
                        B[i, j - 1] += 1  # Add a grain to the left neighbor

    return B

"""
n = 500
m = 500

B = np.zeros((n, m))
draw(B)

for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == n-1 or j == n-1:
            B[i, j] = 1

B[0, 0] = 2
B[n-1, 0] = 2
B[0, m-1] = 2
B[n-1, m-1] = 2
draw(B)

check = topple(B+B, n, m)
draw(check)

while not (check == B).all():
    B = check
    check = topple(B+B, n, m)
    draw(check)

id = check

draw(id, title='Identity', close=False)

np.save(f'id{n}x{n}.npy', id)
"""
