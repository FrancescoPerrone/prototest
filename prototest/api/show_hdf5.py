import pandas as pd
import h5py
import numpy as np

def hdf5_to_csv(hdf5_file, dataset_name, csv_file, axis_names=None):
    """
    Reads a dataset from an HDF5 file, flattens the data to 2D if necessary,
    and writes it to a CSV file.

    Args:
    hdf5_file (str): Path to the HDF5 file.
    dataset_name (str): Name of the dataset in the HDF5 file.
    csv_file (str): Path to the output CSV file.
    axis_names (list of str): List of names for the axes of the data.
    """
    with h5py.File(hdf5_file, 'r') as f:
        data = f[dataset_name][...]

        if axis_names is None:
            axis_names = [f'axis{i}' for i in range(data.ndim)]

        # Flatten the data if it's more than 2D
        if data.ndim > 2:
            data = data.reshape(data.shape[0], -1)

            # Generate column names
            axis1_name = axis_names[1] if len(axis_names) > 1 else 'axis1'
            axis2_name = axis_names[2] if len(axis_names) > 2 else 'axis2'
            columns = [f'{axis1_name}{i}_{axis2_name}{j}'
                       for i in range(data.shape[1])
                       for j in range(data.shape[2])]
        else:
            # For 2D data, use the second axis name for column names
            columns = [f'{axis_names[1]}{i}' for i in range(data.shape[1])]

        df = pd.DataFrame(data, columns=columns)
        df.to_csv(csv_file, index=False)



import pandas as pd
def display_data_in_csv(csv_file):
    """
    Reads a CSV file and displays it as a table.
    
    Args:
    csv_file (str): Path to the CSV file.
    """
    df = pd.read_csv(csv_file)
    print(df)