#!/usr/bin/env python

import os
import sys
import collections
import string
import itertools
import time

def main():

    # creats timer to time the execution time of the program
    start_time = time.time()

    # set the directory to look find the matching files
    x = sys.argv[1]

    # set variables for storage and comparison
    files = []
    words = []
    database = []
    test = 0

    # get the file patch for each text file in directory
    for dirpath, dirnames, filenames in os.walk(x):
        for filename in [f for f in filenames if f.endswith(".txt")]:
            files.append(os.path.join(dirpath, filename))

    # open each file then store their words counts as an entry in a list
    for line in files:
        fopen = open(line)
        for line in fopen:
            line = line.lower()
            line = line.translate(None, string.punctuation)
            for w in line.split():
                words.append(w)
        result = collections.Counter(words)
        database.append(result)
        result = []
        words = []

    # compare each entry's word count to find the two files that match the closest then store their index values
    for ((i,x),(j,y)) in itertools.combinations(enumerate(database), 2):
        if (x != y):
            new =  x & y
            if (len(new)>test):
                trackx = i
                tracky = j
                test = len(new)

    # output the two closest matching files
    print ("The two files with the closest match are: ")
    print (files[trackx])
    print (files[tracky])

    # print out execution time
    print ("")
    print ("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__": 
    main()