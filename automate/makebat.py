import os
from pathlib import Path
import sys

p = Path.home()
os.chdir(p)
if len(sys.argv) > 2:
    # Get txt file name from command line.
    folder = sys.argv[2]
    txtName = sys.argv[1]
elif len(sys.argv) > 1:
    # Get txt file name from command line.
    folder = 'Ch12-Web_Scrapping'
    txtName = sys.argv[1]
else:
    # example txt.
    txtName = 'example'
fileLocation = "@py.exe C:/Users/steve/Documents/GitHub/python-training/automate/{}/{}.py %*".format(
    folder, txtName)
autoFile = open('{}.bat'.format(sys.argv[1]), 'w')
autoFile.write('{}\n@pause'.format(fileLocation))
autoFile.close()
