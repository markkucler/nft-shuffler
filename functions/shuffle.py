import os
import shutil
import random

def shuffle():
    # Define paths
    combined_path = 'data/combined'
    shuffled_path = 'data/shuffled'

    # Create necessary folders if they don't exist
    os.makedirs(os.path.join(shuffled_path, 'metadata'), exist_ok=True)
    os.makedirs(os.path.join(shuffled_path, 'images'), exist_ok=True)

    print("Shuffling files...")

    # Get list of file numbers
    metadata_files = [f for f in os.listdir(os.path.join(combined_path, 'metadata')) if f.endswith('.json')]
    file_numbers = list(range(1, len(metadata_files) + 1))

    # Shuffle file numbers
    random.shuffle(file_numbers)

    # Iterate over shuffled file numbers
    for i, file_number in enumerate(file_numbers, start=1):
        # Define old (current) paths
        old_metadata_path = os.path.join(combined_path, 'metadata', f"{file_number}.json")
        
        # Define new paths
        new_metadata_path = os.path.join(shuffled_path, 'metadata', f"{i}.json")
        
        # Copy metadata file
        shutil.copy2(old_metadata_path, new_metadata_path)
        
        # Find and copy the corresponding image file
        for extension in ['.png', '.jpg', '.jpeg']:
            old_image_path = os.path.join(combined_path, 'images', f"{file_number}{extension}")
            if os.path.isfile(old_image_path):
                new_image_path = os.path.join(shuffled_path, 'images', f"{i}{extension}")
                shutil.copy2(old_image_path, new_image_path)
                break
