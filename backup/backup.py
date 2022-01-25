#!/usr/bin/env python3

import subprocess
import os
from multiprocessing import Pool


src = "./main/"
dest = "./backup/"
directories = []

for root, dirs, files in os.walk(src, topdown=False):  #list the names of the direcories found in the directory named 'main'
   for name in dirs:
        directories.append(name)                       #add directories to a list

def sync_dir(directory):
   ''' uses the Linux tool rsync to backup files from a specified source to a specified destination'''
        subprocess.call(["rsync", "-zrvh", os.path.join(src, directory),  dest] )
        source = os.path.join(src, directory)
        destination = os.path.join(dest, directory)
        print("Backing up folder {} and its contents into {}".format(directory, destination)) #print output to let users know what directories are being backed up


p = Pool(len(directories))     #create a pool of tasks to be completed
p.map(sync_dir, directories)   #backup each subdirectory of the 'main' directory and process each as a separate thread  
  
