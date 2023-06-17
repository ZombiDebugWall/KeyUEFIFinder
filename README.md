# KeyUEFIFinder
Script for finding Windows keys in UEFI binary images. Works with binary images pulled from EEPROM Chips with e.g. CH341A USB Programmer.

## Usage
1. Place your binary image into the root folder that conatains main.py and rename it to "binfile.bin"
2. Run the script by running  ```python main.py``` in a terminal
3. Check the output after the script finished running for keys (watch out for lines that contain hyphens)

## How does it work?
The script extracts strings from the provided binary file and outputs them to the terminal if a string is longer than 24 characters.
