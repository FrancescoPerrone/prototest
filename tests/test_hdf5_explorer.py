from unittest.mock import patch
import prototest.api.hdf5_explorer as papi

@patch('prototest.api.hdf5_explorer.os')
@patch('builtins.input', return_value='/path/to/directory')
def test_explore_directory(mock_input, mock_os):
    mock_os.path.isdir.return_value = True

    papi.explore_directory()
    
    mock_input.assert_called_once()
    mock_os.path.isdir.assert_called_with('/path/to/directory')
