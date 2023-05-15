import os
import re

def rename_files():
    base_path = "data/separated"

    # Get list of subdirectories
    subdirectories = [d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))]

    # Regular expression to match the last occurring number in the filename
    regex = re.compile(r'(\d+)(?!.*\d)')

    # Iterate over subdirectories
    for subdirectory in subdirectories:
        print(f"Renaming files in: {subdirectory}")

        # Define paths for metadata and images in current subdirectory
        metadata_folder = os.path.join(base_path, subdirectory, 'metadata')
        images_folder = os.path.join(base_path, subdirectory, 'images')

        # loop through each file in the metadata folder
        for filename in os.listdir(metadata_folder):
            if filename.endswith(".json"):
                # extract the last occurring number from the file name
                match = regex.search(filename)
                if match:
                    number = match.group(0)
                    new_filename = number + ".json"
                    old_file_path = os.path.join(metadata_folder, filename)
                    new_file_path = os.path.join(metadata_folder, new_filename)
                    os.rename(old_file_path, new_file_path)

        # loop through each file in the images folder
        for filename in os.listdir(images_folder):
            if filename.endswith((".png", ".jpg", ".jpeg")):
                # extract the last occurring number from the file name
                match = regex.search(filename)
                if match:
                    number = match.group(0)
                    new_filename = number + filename[filename.rfind('.'):]
                    old_file_path = os.path.join(images_folder, filename)
                    new_file_path = os.path.join(images_folder, new_filename)
                    os.rename(old_file_path, new_file_path)
