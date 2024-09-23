import csv
import numpy
import os
#import generateMap
from generateMap import generate_map_from_file
import sys

user_abort = False

def map_generator(filename: str):
    color= "ff0000"
    print("Calling map generation for " + filename + " with color "+color+"\n")
    generate_map_from_file(filename, color)
            
# Parameters, later to be modified in experiments
distMiil= 11.3
west1= "130"
west2= "230"
westMiddle= 180
east1= "310"
east2= "410"
eastMiddle= 360
span= 90

file= sys.argv[1]

map_generator(file)

