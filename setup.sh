#!/bin/bash

# Update and install necessary packages
echo "Updating system..."
sudo apt-get update -y

# Install Python and pip
echo "Installing Python and pip..."
sudo apt-get install python3 python3-pip -y

# Install dependencies for generating the index
echo "Installing Python dependencies..."
pip3 install pillow requests

# Clone the repository
echo "Cloning repository..."
git clone https://github.com/Rekt-Developer/TemplatesX.git

# Change to the directory and generate index
cd TemplatesX
python3 generate_index.py

echo "Setup complete. Index file generated."
