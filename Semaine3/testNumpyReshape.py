# Import NumPy
import numpy as np

if __name__ == "__main__":
    # Create a NumPy array of range values
    np_array = np.arange(16)
    #  Print the NumPy array values
    print("The values of NumPy array : \n", np_array)
    # Reshape the array based on C-style orderin
    new_array1 = np.reshape(np_array, (4, 4), order='C')
    # Print the reshaped values
    print("\nThe reshaped 2D array values based with C-style ordering are : \n", new_array1)
    # Reshape the array based on Fortran-style ordering
    new_array2 = np.reshape(np_array, (4, 4), order='F')
    # Print the reshaped values
    print("\nThe reshaped 2D array values-based with Fortran-style ordering are : \n", new_array2)
    new_array2.reshape(-1)
    print(new_array2)
