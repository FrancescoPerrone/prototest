from setuptools import setup, find_packages

setup(
    name='prototest',
    version='0.1.0',
    author='Francesco Perrone',
    author_email='francescoperr@gmail.com',
    description='a Python package to handle data in condensed matter physics.',
    packages=find_packages(),
    install_requires=[
        'numpy>=1.18.1',
        'pandas>=1.0.1',
        'h5py>=2.10.0',
        'matplotlib>=3.1.3',
    ],
)
