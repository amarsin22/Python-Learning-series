import os

# Specify the directory path
directory = '/'  # '.' refers to the current directory

# List all entries in the directory
entries = os.listdir(directory)

# Print the entries
for entry in entries:
    print(entry)
