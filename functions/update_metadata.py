import os
import json

def update_metadata():
    # Prompt the user for project name and description
    nft_name = input("Enter your NFT name: ")
    description = input("Enter the description or press Enter to leave it as is: ")

    # Define paths
    shuffled_path = 'data/shuffled'

    # Get list of JSON files
    json_files = [f for f in os.listdir(os.path.join(shuffled_path, 'metadata')) if f.endswith('.json')]

    # Iterate over JSON files
    for json_file in json_files:
        # Define the JSON file path
        json_path = os.path.join(shuffled_path, 'metadata', json_file)

        # Read the JSON file
        with open(json_path, 'r') as f:
            metadata = json.load(f)

        # Update the "name" key
        metadata['name'] = f"{nft_name} {json_file[:-5]}"  # Remove '.json' from the file name

        # Update the "description" key if a new description was provided
        if description:
            metadata['description'] = description

        # Write the updated JSON data back to the file
        with open(json_path, 'w') as f:
            json.dump(metadata, f, indent=2)
