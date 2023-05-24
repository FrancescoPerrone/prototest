import argparse
from prototest import file_utils as papi_file_utils
from prototest import main as papi_main

def main():
    parser = argparse.ArgumentParser(description='Process and visualize 4DSTEM data.')
    parser.add_argument('--filepath', type=str, help='Path to the directory containing the data files.')
    parser.add_argument('--file_extensions', type=str, nargs='+', help='List of file extensions to include.')
    args = parser.parse_args()
    filepath = args.filepath
    file_extensions = args.file_extensions

    try:
        file_list = papi_file_utils.get_file_list(filepath, file_extensions)
        print('File list:')
        print(file_list)
    except (FileNotFoundError, OSError, KeyError) as e:
        print(f"An error occurred while trying to get the file list: {e}")
        return

    papi_main.visualize_4DSTEM_from_files(filepath, file_list)


if __name__ == "__main__":
    main()
