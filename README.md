# NFT Shuffler

The NFT Shuffler app simplifies the process of preparing NFTs by organizing metadata and images to meet the ERC-721 standard. It seamlessly combines batches, shuffles content, correctly renames files, and updates IPFS links for finalized NFTs, providing outputs that are ready for IPFS upload.

## Prerequisites

- Python 3.6 or later

## Installation

Clone this repository to your local machine:

```
git clone https://github.com/username/nft-shuffler.git
cd nft-shuffler
```

## Usage

Before running the NFT Shuffler, ensure that you place the initial files into the designated "input" folder. While the subfolders within the "input/" folder are not required to follow a specific naming convention, it is crucial that the folder or folders include both an "images" and a "metadata" folder, named exactly as specified. Also, ensure that both the images and metadata folders contain an equal number of files.

```shell
input/
├── batch1
│   ├── images
│   └── metadata
├── batch2
│   ├── images
│   └── metadata
└── batch3
    ├── images
    └── metadata
```

or

```shell
input/
└── folder
    ├── images
    └── metadata
```

The main script for the whole process is `main.py`, which executes the entire workflow by performing all the necessary steps in the correct order.

To start it, run the following command:

```shell
python main.py
```

During the process, you will be asked for the NFT name, that will be used to name every nft with it's corresponding number and an option to input your description, if it's not already there. Once you reach the stage where you are prompted to upload image files to IPFS, you will be given the choice to continue now or continue later.

If you choose to continue now, you will be asked to input the IPFS CID, and the process will finish.

If you choose to continue later, the script will simply exit.

The `finalize_metadata.py` script is specifically designed to handle the finalization process in case you chose to continue later during the upload of image files in `main.py`. So once you have successfully uploaded the image files to IPFS, the next step is to finalize the metadata. To do so, run the following command:

```shell
python finalize_metadata.py
```

You will be prompted to input your IPFS CID, and the process will finish.

Please note that the remaining scripts in the functions directory are auxiliary scripts called by `main.py` and `finalize_metadata.py`. You don't need to execute these scripts independently unless you want to modify or extend the functionality of the NFT Shuffler app.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
