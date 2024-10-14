from setuptools import setup, find_packages

# Define the requirements
requirements = [
    'alpaca-trade-api',  # Alpaca API package
    'pandas',            # Pandas for data manipulation
    'numpy',             # Numpy for numerical operations
]

# Setup function
setup(
    name='your_project_name',  # Replace with your project name
    version='0.1',
    description='Your project description',
    packages=find_packages(),  # Automatically find and include project packages
    install_requires=requirements,  # Dependencies to install
    python_requires='>=3.7',  # Specify the Python version your project supports
)
