from functions.update_image_links import update_image_links
from functions.rm_json_extension import rm_json_extension

def finalize_metadata():
    # Update image links
    cid = input("Enter the CID of the collection: ")
    update_image_links(cid)

    # Finalize metadata
    rm_json_extension()

    # Print message
    print("Done! Your metadata files from output/metadata are now ready to be uploaded to IPFS.")

if __name__ == "__main__":
    finalize_metadata()