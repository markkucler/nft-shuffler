import shutil
import os

def clean_up():
    # Define path
    data_path = 'data'

    # Check if data directory exists
    if os.path.exists(data_path):
        # Remove data folder
        shutil.rmtree(data_path)
        print(f"Cleaned up {data_path}.")
