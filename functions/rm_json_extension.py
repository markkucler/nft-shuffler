import os

def rm_json_extension():
    json_directory = "output/metadata"
    
    # Iterate through each file in the directory
    for filename in os.listdir(json_directory):
        # Check if the file has a .json extension
        if filename.endswith(".json"):
            # Get the file path without the .json extension
            new_filename = os.path.splitext(filename)[0]
            
            # Create the file paths for the original and new filenames
            original_file_path = os.path.join(json_directory, filename)
            new_file_path = os.path.join(json_directory, new_filename)

            # Rename the file
            os.rename(original_file_path, new_file_path)
