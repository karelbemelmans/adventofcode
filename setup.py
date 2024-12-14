from setuptools import setup, find_packages
setup(
    name='adventofcode',
    version='0.1',
    packages=find_packages(include=['tests', 'tests.*']),
    include_package_data=True,
    install_requires=[
        'pytest',
        'bresenham',
        'networkx',
        'autopep8',
        'utils',
        'numpy',
        'matplotlib',
        'sympy'
    ],
)
