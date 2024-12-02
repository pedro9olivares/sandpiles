import numpy as np
import matplotlib.pyplot as plt
from groningen_sand import topple
import os

# Example usage
if __name__ == "__main__":
    file_path = "id256x256.npy"

    data = np.load(file_path)

    plt.imshow(data, cmap='viridis')
    plt.colorbar()
    plt.title(f"Visualization of {file_path}")
    plt.show()

    state_1 = data + np.ones((256,256))
    state_1 = topple(state_1, 256, 256)

    plt.imshow(state_1, cmap='viridis')
    plt.colorbar()
    plt.title(f"Visualization of state_1")
    plt.show()

    n = 256
    np.save(f'state1_{n}x{n}.npy', state_1)
