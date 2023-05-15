import os
import shutil

def combine_files():
    # Define paths
    base_path = 'data/separated'
    combined_path = 'data/combined'

    # Create necessary folders if they don't exist
    os.makedirs(os.path.join(combined_path, 'metadata'), exist_ok=True)
    os.makedirs(os.path.join(combined_path, 'images'), exist_ok=True)

    # Get list of subdirectories
    subdirectories = [d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))]

    # Initialize file counter
    file_counter = 1

    # Iterate over subdirectories
    for subdirectory in sorted(subdirectories):
        print(f"Combining: {subdirectory}")

        # Define paths for metadata and images in current subdirectory
        metadata_path = os.path.join(base_path, subdirectory, 'metadata')
        images_path = os.path.join(base_path, subdirectory, 'images')

        # Get list of files in current subdirectory
        files = [f for f in os.listdir(metadata_path) if f.endswith('.json')]

        # Iterate over files in current subdirectory
        for filename in files:
            # Define old (current) paths
            old_metadata_path = os.path.join(metadata_path, filename)
            file_id = int(filename.split('.')[0])  # Extract the file ID from the filename

            # Define new paths
            new_metadata_path = os.path.join(combined_path, 'metadata', f"{file_counter}.json")

            # Define old image path based on the file ID
            for extension in ['.png', '.jpg', '.jpeg']:
                old_image_path = os.path.join(images_path, f"{file_id}{extension}")
                if os.path.isfile(old_image_path):
                    new_image_path = os.path.join(combined_path, 'images', f"{file_counter}{extension}")
                    # Copy files
                    shutil.copy2(old_metadata_path, new_metadata_path)
                    shutil.copy2(old_image_path, new_image_path)
                    break
            else:
                print(f"Could not find image file for metadata file: {filename}")

            # Increment file counter
            file_counter += 1
