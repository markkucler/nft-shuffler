import os
import json

# Function to find image extension
def find_image_extension(directory):
    for filename in os.listdir(directory):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            return os.path.splitext(filename)[1]
    return None

# Function to update image links in metadata
def update_image_links(cid):
    # Set the directory paths
    json_directory = "output/metadata"
    images_directory = "output/images"

    # Find the image file extension
    file_extension = find_image_extension(images_directory)
    if file_extension is None:
        print('No image files found in the images directory.')
        return

    # Construct the base IPFS URL
    ipfs_base_url = f"ipfs://{cid}/"

    # Iterate through each file in the directory
    for filename in os.listdir(json_directory):
        # Check if the file has a .json extension
        if filename.endswith(".json"):
            # Read the .json file
            with open(os.path.join(json_directory, filename), "r") as file:
                metadata = json.load(file)

            # Get the image filename from the .json filename
            image_filename = os.path.splitext(filename)[0] + file_extension

            # Update the image key value with the IPFS URL
            metadata["image"] = ipfs_base_url + image_filename

            # Write the updated metadata back to the .json file
            with open(os.path.join(json_directory, filename), "w") as file:
                json.dump(metadata, file, indent=2)
