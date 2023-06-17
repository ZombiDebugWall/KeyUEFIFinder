# KeyUEFIFinder
Script for finding Windows keys in UEFI binary images. Works with binary images pulled from EEPROM Chips with e.g. CH341A USB Programmer.

## Usage
1. Place your binary image into the root folder that contains main.py and rename it to "binfile.bin"
2. Run the script by running  ```python main.py``` in a terminal
3. Check the output for keys, after the script finished running (watch out for lines that are hyphenated)

## How does it work?
The script extracts strings from the provided binary file and outputs strings longer than 24 characters to the terminal.
