import os
import fnmatch

def get_file_list(filepath: str, file_extensions: list = ['*.h5', '*.hdf5']) -> list:
    """
    This function returns a sorted list of files in the specified directory that matches any of the specified file extensions.
    """
    if not os.path.isdir(filepath):
        raise FileNotFoundError(f"The specified directory does not exist: {filepath}")
    
    files = [file for file in os.listdir(filepath) for file_extension in file_extensions if fnmatch.fnmatch(file, file_extension)]
    files.sort()
    return files

def select_file(file_list):
    """
    This function presents a list of files to the user and allows them to select one.
    """
    print("Available files:")
    for i, file in enumerate(file_list):
        print(f"{i+1}: {file}")
    file_index = int(input("Enter the number of the file you want to explore, or 0 to quit: ")) - 1
    if file_index == -1:
        return None
    return file_list[file_index]
