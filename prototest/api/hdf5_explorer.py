import os
import h5py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def explore_directory():
    """
    Prompts the user for a directory path and explores the hdf5 files in that directory,
    performing correlation analysis on each file.

    Returns:
    None
    """
    while True:
        directory = input("Enter the directory path (or 'exit' to quit): ")

        if directory.lower() == 'exit':
            print("Exiting the program.")
            return

        if not os.path.isdir(directory):
            print(f"{directory} is not a valid directory. Please enter a valid directory path.")
            continue

        correlation_data = {}  # Dictionary to hold data for correlation analysis

        try:
            for root, dirs, files in os.walk(directory):
                for file in files:
                    if file.endswith(".hdf5"):
                        filepath = os.path.join(root, file)
                        with h5py.File(filepath, 'r') as hdf:
                            print(f"\nInspecting file: {filepath}")
                            correlation_data = explore_group(hdf, correlation_data)
        except Exception as e:
            print(f"An error occurred while reading the HDF5 file(s): {e}")
            continue

        # Perform correlation analysis on each pair of datasets
        if correlation_data:
            for key1 in correlation_data:
                for key2 in correlation_data:
                    if key1 != key2:
                        df1 = pd.Series(correlation_data[key1])
                        df2 = pd.Series(correlation_data[key2])
                        if len(df1) == len(df2):
                            try:
                                correlation = df1.corr(df2)
                                print(f"\nCorrelation between {key1} and {key2}: {correlation}")
                            except Exception as e:
                                print(f"An error occurred while calculating correlation: {e}")
        else:
            print("\nNo suitable datasets found for correlation analysis.")

        return


def explore_group(group, correlation_data):
    for key in group.keys():
        item = group[key]
        if isinstance(item, h5py.Dataset):
            print(f"\nDataset: {item.name}")
            print(f"Shape: {item.shape}")
            print(f"Dtype: {item.dtype}")
            explore_dataset(item)
            if item.dtype.kind in 'iuf' and item.ndim == 1:  # If dataset is 1D and numeric
                correlation_data[item.name] = np.array(item)
        elif isinstance(item, h5py.Group):
            print(f"\nGroup: {item.name}")
            correlation_data = explore_group(item, correlation_data)
    return correlation_data

def explore_dataset(dataset):
    data = np.array(dataset)

    # Only compute statistics for datasets with less than 2 dimensions and less than 1000 unique values
    if data.ndim < 2 and len(np.unique(data)) < 1000:
        print(f"Min: {np.min(data)}")
        print(f"Max: {np.max(data)}")
        print(f"Mean: {np.mean(data)}")
        print(f"Median: {np.median(data)}")
        print(f"Std dev: {np.std(data)}")

        # Plot histogram
        plt.figure()
        plt.hist(data, bins='auto', alpha=0.5, rwidth=0.85, density=True)  # rwidth < 1 creates space between bars, density=True normalizes data

        # Plot KDE
        try:
            pd.Series(data).plot(kind='kde')
        except:
            print("Could not plot KDE. Check if data is suitable for KDE plot.")

        plt.title(f"Histogram of {dataset.name}")
        plt.show()

# if __name__ == "__main__":
#     directory = input("Enter the directory path: ")
#     explore_directory(directory)
