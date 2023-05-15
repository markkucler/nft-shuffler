from functions.prepare_folders import prepare_folders
from functions.process_data import process_data
from functions.shuffle import shuffle
from functions.update_metadata import update_metadata
from functions.copy_to_output import copy_to_output
from functions.clean_up import clean_up
from functions.update_image_links import update_image_links
from functions.rm_json_extension import rm_json_extension

def main():
    # Prepare folders
    prepare_folders()

    # Process data
    process_data()

    # Shuffle
    shuffle()

    # Update metadata
    update_metadata()

    # Copy shuffled data to output folder
    copy_to_output()

    # Clean up
    clean_up()

    # Print message
    print("Done! Upload your image files from output/images to IPFS and enter the CID below.")

    # Ask user if they want to continue now or later
    choice = input("Do you have your CID and want to continue now (Y/N)? ")

    if choice.lower() == "n":
        print("You can continue later by running the following command: python finalize_metadata.py")
        exit()

    # Update image links
    cid = input("Enter the CID of the collection: ")
    update_image_links(cid)

    # Finalize metadata
    rm_json_extension()

    # Print message
    print("Done! Your metadata files from output/metadata are now ready to be uploaded to IPFS.")

if __name__ == "__main__":
    main()
