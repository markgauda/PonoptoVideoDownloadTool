"""
This program takes in the path to an index.m3u8 file and a url
This program then modifies the index.m3u8 file such that it
    will prepend every line that dosent start with a '#' with the
    url
"""


import sys


if __name__ == "__main__":
    if len(sys.argv) == 3:
        pathToFileToChange = sys.argv[1]
        url = sys.argv[2]
        outputFileLocation = "./Output.m3u8"
        with open(pathToFileToChange, "r") as inputFile:
            buffer = ""
            for line in inputFile:
                if line[0] == '#':
                    buffer = buffer + line
                else:
                    buffer = buffer + url + '/' + line

        with open(outputFileLocation, "w") as outputFile:
            outputFile.write(buffer)
            
        
    else:
        print("invalid amount of arguments (Should be 2) (0 through 2)")
        argumentNumber = 0
        for argument in sys.argv:
            print(f"{argumentNumber}, {argument}")
            argumentNumber += 1



