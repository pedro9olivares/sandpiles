from sandpiles import add_grains, draw
import numpy as np

n = 10
B = np.zeros((n,n))

# Step 1: add 2 grains on corners and 1 grain on borders

for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == n-1 or j == n-1:
            add_grains(1, i, j, B, False) # Borders

add_grains(2, 0, 0, B, False)         # Top-left corner
add_grains(2, n-1, 0, B, False)       # Bottom-left corner
add_grains(2, 0, n-1, B, False)       # Top-right corner
add_grains(2, n-1, n-1, B, False)     # Bottom-right corner

#print(B)

# Step 2: add B + B
def BplusB(B, n):
    for i in range(n):
        for j in range(n):
            add_grains(int(B[i, j]), i, j, B)
    return B

check = BplusB(B, n)

#print(check)

# Step 3: repeat until B does not change
while not (check == B).all():
    B = check
    check = BplusB(B, n)

id = check

#print(id)
draw(id, title='Identity', close=False)
