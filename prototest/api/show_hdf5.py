import pandas as pd
import h5py
import numpy as np

def hdf5_to_csv(hdf5_file, dataset_name, csv_file, axis_names=None, flatten=False):
    """
    Reads a dataset from an HDF5 file and writes it to a CSV file.

    Args:
    hdf5_file (str): Path to the HDF5 file.
    dataset_name (str): Name of the dataset in the HDF5 file.
    csv_file (str): Path to the output CSV file.
    axis_names (list of str): List of names for the axes of the data.
    flatten (bool): If True, flatten the data to 2D. Default is False.
    """
    with h5py.File(hdf5_file, 'r') as f:
        data = f[dataset_name][...]

        # Generate default axis names if not provided
        if axis_names is None:
            axis_names = [f'axis{i}' for i in range(data.ndim)]
        
        if flatten:
            # Flatten the data to 2D
            data = data.reshape(data.shape[0], -1)
            columns = [f'{axis_names[0]}_{i}_{axis_names[1]}_{j}'
                        for i in range(data.shape[0])
                        for j in range(data.shape[1])]
        else:
            # Keep the original shape, generate a multi-index for columns
            index = pd.MultiIndex.from_product([range(i) for i in data.shape[1:]], names=axis_names[1:])
            columns = pd.Index(range(data.shape[0]), name=axis_names[0])
            data = data.reshape(data.shape[0], -1)
            df = pd.DataFrame(data, index=columns, columns=index)
            df.to_csv(csv_file)
            return

        df = pd.DataFrame(data, columns=columns)
        df.to_csv(csv_file, index=False)

# To flatten the data and create custom names for each dimension
# hdf5_to_csv('path_to_your_file.hdf5', 'dataset_name', 'output.csv', ['time', 'x', 'y'], flatten=True)
# To keep the original shape and create custom names for each dimension
# hdf5_to_csv('path_to_your_file.hdf5', 'dataset_name', 'output.csv', ['time', 'x', 'y'])



import pandas as pd
def display_data_in_csv(csv_file):
    """
    Reads a CSV file and displays it as a table.
    
    Args:
    csv_file (str): Path to the CSV file.
    """
    df = pd.read_csv(csv_file)
    print(df)