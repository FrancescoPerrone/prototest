import h5py

def print_attrs(name, obj, datasets):
    if isinstance(obj, h5py.Dataset):
        print(f'Dataset path:  {name}')
        datasets[name] = obj

def load_4DSTEM_data(file_path, dataset_path):
    """
    Load a 4DSTEM dataset from a specified path within an HDF5 file.

    Parameters:
    file_path: str
        The path to the HDF5 file.
    dataset_path: str
        The path to the dataset within the HDF5 file.

    Returns:
    np.ndarray
        The loaded dataset.
    """

    with h5py.File(file_path, 'r') as f:
        if isinstance(dataset_path, (str, bytes)):
            if dataset_path in f:
                data = f[dataset_path][()]
                return data
            else:
                raise KeyError(f"The dataset path was not found in the file: {dataset_path}")
        else:
            raise TypeError(f"The dataset path must be a str or bytes, not {type(dataset_path)}")

def explore_and_load_4DSTEM_data(file_paths: list):
    """
    Explore the available datasets in a list of HDF5 files and prompt the user to select a dataset to load.
    The user is shown the path structure of the HDF5 file and asked to enter the path to the dataset they wish to load.
    If a valid dataset is selected, it is loaded and returned. If the user decides to change the file, a special keyword is returned.
    
    Parameters:
    file_paths: list
        The list of file paths to the HDF5 files.

    Returns:
    np.ndarray or str
        The loaded dataset, or a special keyword indicating the user's wish to change the file.
    """
    for file_path in file_paths:
        print(f'Exploring file: {file_path}')

        try:
            with h5py.File(file_path, 'r') as f:
                datasets = {}
                f.visititems(lambda name, obj: print_attrs(name, obj, datasets))
                while True:
                    print("Available datasets:")
                    for i, dataset_name in enumerate(datasets.keys(), start=1):
                        print(f"{i}: {dataset_name}")
                    dataset_index = input("Enter the number of the dataset you wish to load, or 'change file' to explore another file: ")
                    if dataset_index.lower() == 'change file':
                        return 'change file'
                    try:
                        dataset_index = int(dataset_index) - 1
                        dataset_path = list(datasets.keys())[dataset_index]
                        print(f'Trying to load: {file_path}/{dataset_path}')
                        data = datasets[dataset_path][()]
                        return data
                    except (ValueError, IndexError, KeyError, OSError) as e:
                        print(f'An error occurred while trying to load the dataset: {e}')
                        print('Please select a different dataset.')

        except OSError as e:
            print(f'An error occurred while trying to explore the file: {e}')