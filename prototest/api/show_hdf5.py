import pandas as pd
import h5py

def hdf5_to_csv(hdf5_file, dataset_name, csv_file):
    """
    Reads a dataset from an HDF5 file and writes it to a CSV file.
    
    Args:
    hdf5_file (str): Path to the HDF5 file.
    dataset_name (str): Name of the dataset in the HDF5 file.
    csv_file (str): Path to the output CSV file.
    """
    with h5py.File(hdf5_file, 'r') as f:
        data = f[dataset_name][...]
        df = pd.DataFrame(data)
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