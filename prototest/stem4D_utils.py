import py4DSTEM
import numpy as np

def visualize_4DSTEM_data(data):
    """
    Visualize a 4DSTEM dataset.

    Parameters:
    data: np.ndarray
        The 4DSTEM dataset.

    """

    # Create a DataCube object
    dataset = py4DSTEM.io.datastructure.DataCube(data = data)

    # Calculate max and mean diffraction patterns
    dataset.get_dp_max()
    dataset.get_dp_mean()

    # Visualize the computed diffraction patterns
    py4DSTEM.visualize.show_image_grid(
        lambda i:[
            dataset.tree['dp_mean'],
            dataset.tree['dp_max']
        ][i],
        H=1,
        W=2,
        cmap='turbo',
        scaling='power',
        power=0.25
    )