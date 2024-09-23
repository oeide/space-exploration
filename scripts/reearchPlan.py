import csv
import numpy
import os
#import generateMap
from generateMap import generate_map_from_file

user_abort = False

def csv_reader(filepath: str):
    """
    Extracts Between-info
    :param filepath: filepath to csv-file
    # row_list: Place, Xord, Yord, Zone, Distance, Direction, Koord
    """
    with open(filepath) as file:
        csvreader = csv.DictReader(file)
        read_list = list()
        i= 0
        place= []
        array= numpy.zeros((6))
        row_list =[]
        for row in csvreader:
            row_list.append(row)
            place.append(row["Place"])
#            array.append(place=row["Place"], xord=row["Xord"], yord=row["Yord"], zone=row["Zone"], distance=row["Distance"], direction=row["Direction"], koord=row["Koord"]), 
            #print(place[i])
            i= i+1
        #print(place[3])
        #print(row_list[3]["Xord"])
        i= 1
        while i < len(row_list)-1:
            if i<10:
                color="#"+str(i)+str(i)+"0000"
            else:
                color="#"+str(i)+"0000"
            filename= root+"output/coord"+str(i)+".csv"
            filenamePoint= root+"output/coord"+str(i)+".txt"
            if os.path.exists(filename):
                os.remove(filename)
            if os.path.exists(filenamePoint):
                os.remove(filenamePoint)
            fileOut = open(filename, "x")
            fileOutPoint = open(filenamePoint, "x")
            iBefore= i-1
            iAfter= i+1
            print(row_list[i]["Place"] + " is being handled...")
            #print("utm," + row_list[i]["Xord"] + " " + row_list[i]["Yord"] + " " + row_list[i]["Zone"] + " S,direction," + str(int(row_list[i]["Distance"]) * distMiil) + " " + west1 + west2)
            fileOut.write("cs,coordinates,type,verweis\n")
            fileOut.write("utm," + row_list[iBefore]["Xord"] + " " + row_list[iBefore]["Yord"] + " " +
                  row_list[iBefore]["Zone"] + " S,direction," + str(int(row_list[i]["Distance"]) * distMiil) + 
                  " " + str(int(westMiddle-(span/2))) + " " + str(int(westMiddle+(span/2)))+"\n")
            fileOut.write("utm," + row_list[iAfter]["Xord"] + " " + row_list[iAfter]["Yord"] + " " +
                  row_list[iAfter]["Zone"] + " S,direction," + str(int(row_list[iAfter]["Distance"]) * distMiil) +
                  " " + str(int(eastMiddle-(span/2))) + " " + str(int(eastMiddle+(span/2)))+"\n")
            fileOutPoint.write(row_list[i]["Xord"] + " " + row_list[i]["Yord"])
            i= i+1
            fileOut.write("\n")
            fileOut.close()
            fileOutPoint.write("\n")
            fileOutPoint.close()
            #print("Calling map generation for " + filename + " with color "+color+"\n")
            #generate_map_from_file(filename, color)
            
# Parameters, later to be modified in experiments
west1= "130"
west2= "230"
westMiddle= 180
east1= "310"
east2= "410"
eastMiddle= 360

span= 225
distMiil= 6

root= "/Users/oeide/Documents/GitHub/space-exploration/"

#while not user_abort:
csv_reader(root+"SchnitlerBasis.csv")
    
