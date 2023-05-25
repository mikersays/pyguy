#!/bin/bash

# Make sure python3 and pip3 are installed
if ! command -v python3 &> /dev/null; then
    echo "Python3 not found, please install it first."
    exit 1
fi

if ! command -v pip3 &> /dev/null; then
    echo "pip3 not found, please install it first."
    exit 1
fi

# Create a virtual environment (optional)
python3 -m venv venv
source venv/bin/activate

# Update pip
pip3 install --upgrade pip

# List of popular Python3 packages
packages=(
  numpy
  pandas
  matplotlib
  seaborn
  scikit-learn
  scipy
  requests
  beautifulsoup4
  Flask
  Django
  sqlalchemy
  pytest
  jupyter
  pylint
  tensorflow
  keras
  torch
)

echo "Installing popular Python3 packages..."
for package in "${packages[@]}"; do
    echo "Installing $package..."
    pip3 install "$package"
done

# To deactivate the virtual environment when done (not necessary if you didn't create one)
# deactivate

echo "All packages have been installed. Enjoy coding!"
