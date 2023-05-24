import argparse
import os
from .file_utils import get_file_list, select_file
from .hdf5_utils import explore_and_load_4DSTEM_data
from .stem4D_utils import visualize_4DSTEM_data


def  visualize_4DSTEM_from_files():
    while True:
        try:
            __IPYTHON__
            filepath = input("Please enter the path to the directory containing the data files (or 'exit' to quit): ")
            if filepath.lower() == 'exit':
                print("Exiting...")
                return
            file_extensions = input("Please enter the list of file extensions to include (separated by spaces): ").split()
            if not os.path.isdir(filepath):
                raise FileNotFoundError
        except NameError:
            parser = argparse.ArgumentParser(description='Process 4DSTEM data.')
            parser.add_argument('--filepath', type=str, help='Path to the directory containing the data files.')
            parser.add_argument('--file_extensions', type=str, nargs='+', help='List of file extensions to include.')
            args = parser.parse_args()
            filepath = args.filepath
            file_extensions = args.file_extensions

        # Get list of files
        try:
            file_list = get_file_list(filepath, file_extensions)
            print('File list:')
            print(file_list)
        except FileNotFoundError as e:
            print("Invalid directory. Please try again.")
            continue

        # User selects file
        while True:
            selected_file = select_file(file_list)
            if selected_file is None:
                print("Exiting...")
                break

            # Load and visualize data for the selected file
            full_file_path = os.path.join(filepath, selected_file)
            loaded_data = explore_and_load_4DSTEM_data([full_file_path])  # Pass a list with a single file path
            if loaded_data == 'change file':
                continue
            try:
                visualize_4DSTEM_data(loaded_data)
            except Exception as e:
                print(f'An error occurred while trying to visualize the dataset: {e}')
