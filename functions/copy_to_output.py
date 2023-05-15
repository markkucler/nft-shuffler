import os
import shutil

def copy_to_output():
    # Define paths
    source_path = 'data/shuffled'
    output_path = 'output'

    # Check if source directory exists
    if not os.path.exists(source_path):
        print(f"Source directory {source_path} does not exist.")
        return

    # Check if output directory exists, create if it doesn't
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # Copy data
    shutil.copytree(source_path, output_path, dirs_exist_ok=True)
    print(f"Data successfully copied from {source_path} to {output_path}.")
