The 'backup.py' script backs up all the subdirectories of 'main' into the 'backup' directory.  The process is facilitaed by using the subprocess 
module to run bash tools from within a script. Specifically, rsync is used to perform the backup with directories as the units and using the recursive feature to include 
all files within the corresponding subdirectory. To speed up the back up process, the script uses the multiprocess module that allows the backing up of each individual
subdirectory to be its own process. In this scenario, it is not effective as the contents of the subdirectories are minimal, but this may be crucial if the subdirecotires
contained large fles. Subdirectories of the 'backup' directory contain additional empty files as it is not possible to have empty directories in GitHub. 

Potential improvements:  
Include command to create directory to avoid having directories with unnecessary empty files
Allow users to compress directories instead using the multiprocessing method
