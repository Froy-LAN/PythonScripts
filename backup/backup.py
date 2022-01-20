#!/usr/bin/env python3

import subprocess
import os
import tarfile
from multiprocessing import Pool
from os.path import join

src = "./main/"
dest = "./backup/"
directories = []

for root, dirs, files in os.walk(src, topdown=False):
   for name in dirs:
        directories.append(name)

def sync_dir(directory):
        subprocess.call(["rsync", "-zrvh", os.path.join(src, directory),  dest] )
        source = os.path.join(src, directory)
        destination = os.path.join(dest, directory)
        print("Backing up folder {} and its contents into {}".format(directory, destination))


p = Pool(len(directories))
p.map(sync_dir, directories)
