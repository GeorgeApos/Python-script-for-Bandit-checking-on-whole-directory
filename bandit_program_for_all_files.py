from os import listdir
import os
import sys
from os.path import isfile, join
import subprocess

bashCommand = 'bandit '
mypath= {YOUR_PATH}

for f in listdir(mypath):
    if isfile(join(mypath, f)):
        print("\nI found a file")
        if os.path.splitext(f)[-1].lower() == ".py":
            print("Checking file ... " + f + "\n")
            os.system(bashCommand + f)
        else:
            print(f + " doesn't end with .py")

            


