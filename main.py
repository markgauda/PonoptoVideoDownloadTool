"""
This program takes in the a url to an index.m3u8 file
    and it will return a modified version of that file
    that vlc media player can use
"""


import sys
import requests


def outputBuffer(buffer, outputFile):
    buffer = buffer + '\n'
    outputFile.write(buffer)
    buffer = ""
    return buffer

if __name__ == "__main__":
    if len(sys.argv) == 2:
        url = sys.argv[1]
        fileToModify = requests.get(url).text #Save the Index.m3u8 into memory
        urlSliceEnd = url.find("index.m3u8")
        modifiedURL = url[0:(urlSliceEnd -1)]
        outputFileLocation = "./Output.m3u8"

        with open(outputFileLocation, "w") as outputFile:
            buffer = ""
            for character in fileToModify:
                if character != '\n':
                    buffer = buffer + character
                else:
                    if buffer[0] != '#': #This means that we are looking at a link and we need to add the url
                        buffer = modifiedURL + '/' + buffer
                        buffer = outputBuffer(buffer, outputFile)

                    else: #This means the buffer has a comment and we can just add it
                        buffer = outputBuffer(buffer, outputFile)
             
        
    else:
        print("invalid amount of arguments (Should be 1) (0 through 1)")
        argumentNumber = 0
        for argument in sys.argv:
            print(f"{argumentNumber}, {argument}")
            argumentNumber += 1




