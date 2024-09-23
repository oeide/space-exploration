import csv
import numpy
import os
#import generateMap
from generateMap import generate_map_from_file
import sys
import re
import os

user_abort = False

def map_generator(filename: str):
    color= "ff0000"
    print("Calling map generation for " + filename + " with color "+color+"\n")
    map_path= generate_map_from_file(filename, color)
    print("Map path in map_generator: " + map_path)
    filenameExt = re.split("/", filename)
    filenameClean= re.split("\.", filenameExt[len(filenameExt)-1])[0]
    print("Filename: " + filenameClean)
    i=0
    pathOutput=""
    while i < len(filenameExt)-2:
        pathOutput= pathOutput+filenameExt[i]+"/"
        i= i+1
    pathOutput= pathOutput+"outputMaps/"+filenameClean+".html"
    cmd = "cp /private/tmp/map.html "+pathOutput
    returned_value = os.system(cmd)
    print("Copy: "+cmd+" Return value:"+str(returned_value))
    
file= sys.argv[1]
map_generator(file)
