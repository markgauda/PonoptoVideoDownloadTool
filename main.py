"""
This program takes in the a url to an index.m3u8 file
    and it will return a modified version of that file
    hat vlc media player can use
"""


import sys
import urllib.request


if __name__ == "__main__":
    if len(sys.argv) == 2:
        url = sys.argv[1]
        fileToModify = "tempFile.txt"
        urllib.request.Request(url, fileToModify)
        urlSliceEnd = url.find("index.m3u8")
        url = url[0:(urlSliceEnd -1)]
        outputFileLocation = "./Output.m3u8"

        with(fileToModify, 'r') as inputFile:
            buffer = ""
            for line in inputFile:
                if line[0] == '#':
                    buffer = buffer + line
                else:
                    buffer = buffer + url + '/' + line

        with open(outputFileLocation, "w") as outputFile:
            outputFile.write(buffer)
             
        
    else:
        print("invalid amount of arguments (Should be 1) (0 through 1)")
        argumentNumber = 0
        for argument in sys.argv:
            print(f"{argumentNumber}, {argument}")
            argumentNumber += 1




    