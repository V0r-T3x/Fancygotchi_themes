#!/bin/bash

# Simple Bash Script to write "Hello, World!" to a file

# Define the output file with the absolute path for clarity
output_file="/home/pi/HACK_THE_PLANET.txt"

# Use sudo to write to the file
echo "Hello, World!" | sudo tee "$output_file" > /dev/null

# Inform the user
sudo echo "Written 'Hello, World!' to $output_file"

# Exit with success
exit 0
