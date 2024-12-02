import numpy as np
import matplotlib.pyplot as plt
import os
import matplotlib.cm

# Function to load and visualize .npy file
def load_and_visualize_npy(file_path, title):
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' does not exist.")
        return

    try:
        data = np.load(file_path)
        print(f"Loaded data shape: {data.shape}")

        # Check if data is 2D or 3D for plotting
        if data.ndim == 2:
            cmap = matplotlib.cm.Blues(np.linspace(0,1,20))
            plt.imshow(data, cmap=matplotlib.colors.ListedColormap(cmap[10:,:-1]))
            plt.colorbar()
            plt.title(title)
        else:
            print("Data is not 2D. Cannot visualize directly.")
        plt.show()
    except Exception as e:
        print(f"Error loading or visualizing the file: {e}")

# Example usage
if __name__ == "__main__":
    # Replace 'your_file.npy' with the path to your .npy file
    file_path = "id256x256.npy"
    load_and_visualize_npy(file_path, 'Identity of 256x256 Abelian Sandpile')
