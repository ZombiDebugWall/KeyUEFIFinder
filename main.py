import codecs


#Author: ZombiDebugWall
#Date: 17.06.2023
#KeyUEFIFinder script for finding keys in UEFI binary images

def keyUEFIFinderMain():

    rom_file = open("binfile.bin", "rb")

    string_cache = ""

    file_bytes_encode = rom_file.read().decode("ANSI")
    
    search_pattern_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-"]

    byte_counter_cache = 0
    byte_counter = 0
    byte_counter_set = False
    for byte in file_bytes_encode:

        if byte in search_pattern_list:
            string_cache += byte
            if not byte_counter_set:
                byte_counter_cache = byte_counter
                byte_counter_set = True
        else:
            if len(string_cache) > 24:
                print("At byte", str(byte_counter_cache) + ":", string_cache)
                string_cache = ""
                byte_counter_set = False
                
            else:
                string_cache = ""
                byte_counter_set = False

        byte_counter += 1

keyUEFIFinderMain()
