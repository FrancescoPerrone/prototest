import os
import h5py
import numpy as np

def print_structure(name, obj):
    """
    Function to be used as a callback for h5py's visititems function.
    Prints the structure of an HDF5 file.
    
    Args:
    name (str): Path to the object in the HDF5 file.
    obj (h5py.Dataset or h5py.Group): HDF5 object.
    """
    print(name)
    if isinstance(obj, h5py.Dataset):
        print(f" - Dataset, datatype: {obj.dtype}, shape: {obj.shape}")
        if obj.size <= 100 and np.issubdtype(obj.dtype, np.number):
            try:
                data_sample = obj[...]
                print(f" - Data sample: {data_sample}")
            except Exception as e:
                print(f" - Error reading data: {e}")
    elif isinstance(obj, h5py.Group):
        print(" - Group")

def explore_hdf5_files(directory):
    """
    Traverses a directory and for each HDF5 file found, prints its structure 
    and a small data sample for each dataset (if it's not too large and is of a basic numeric datatype).
    
    Args:
    directory (str): Path to the directory that contains the HDF5 files.
    """
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith((".hdf5", ".h5")):
                filepath = os.path.join(root, file)
                print(f"\nExploring file: {filepath}")
                
                with h5py.File(filepath, 'r') as f:
                    f.visititems(print_structure)

# Use the function to explore a specific directory
# explore_hdf5_files("/path/to/your/directory")