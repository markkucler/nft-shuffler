import os
import shutil

def prepare_folders():
    # Define paths
    input_path = 'input'
    output_path = 'data/separated'

    # Create necessary folders if they don't exist
    os.makedirs(output_path, exist_ok=True)

    # Get list of subdirectories in the input folder
    subdirectories = [d for d in os.listdir(input_path) if os.path.isdir(os.path.join(input_path, d))]

    # Iterate over subdirectories
    for subdirectory in subdirectories:
        print(f"Making a copy of: {subdirectory}")

        # Define paths for current subdirectory
        input_subdirectory_path = os.path.join(input_path, subdirectory)
        output_subdirectory_path = os.path.join(output_path, subdirectory)

        # Copy the subdirectory to the output folder
        shutil.copytree(input_subdirectory_path, output_subdirectory_path)
