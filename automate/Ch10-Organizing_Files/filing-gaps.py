
"""Fix gaps in files with a chosen prefix in a specified folder."""

import os
import re
import shutil
from pathlib import Path
import random

p = Path.home()
os.chdir(p/'spam')
numlist = [1]
spamFile = open('spam00{}.txt'.format(numlist[0]), 'w')
spamFile.write('Hello, there!\n')
spamFile.close()

for i in range(5):
    randomNumber = random.randint(2, 9)
    if randomNumber not in numlist:
        numlist.append(randomNumber)
        spamFile = open('spam00{}.txt'.format(numlist[len(numlist)-1]), 'w')
        spamFile.write('Hello, there!\n')
        spamFile.close()
p = Path.home()/'spam'
os.chdir(p)

folder = os.path.abspath(Path.cwd())
folder = input("Enter the absolute path of the folder you'd like to search: ")
prefix = 'spam'
prefix = input("Enter the prefix (up to the numbering) of the files whose"
               "numbering you'd like to check: ")

# Regex to find the chosen sequentially named files
ordered_regex = re.compile(r'({0})(\d*)(.*)(\..*)'.format(prefix))

found = []       # Keep track of numbering of files with chosen prefix

# Filewalk to find files with chosen prefix
for folders, subfolders, filenames in os.walk(folder):
    for filename in filenames:

        if ordered_regex.search(filename) is not None:

            # Determine length of numbering digits (for later naming)
            num_length = int(len(ordered_regex.search(filename).group(2)))

            # Find extension of files (for later naming)
            extension = ordered_regex.search(filename).group(4)

            # Number of files with chosen prefix
            found.append(ordered_regex.search(filename).group(2))

    ordered = sorted([int(x) for x in found])

# Loop to check for corret numbering based on amount of files found
for number in range(1, len(found) + 1):

    # Calculate amount of 0's to prepend to reconstruct original format
    zeroes = '0' * (num_length - len(str(number)))

    # Recreate path of what should be the next file
    current_file = '{}/{}{}{}{}'.format(folder, prefix, zeroes,
                                        number, extension)

    # Check if the file exists
    if os.path.exists(current_file) is False:
        # Find numbering of actual next file and format path
        next_num = ordered[number - 1]
        next_zeroes = '0' * (num_length - len(str(next_num)))
        next_file = (folder + '/' + prefix + str(next_zeroes)
                     + str(next_num) + extension)

        # Rename actual to desired through shutil move
        shutil.move(next_file, current_file)

print('File numbering has been fixed.')


# try later

# import os
# import re
# from pathlib import Path
# import shutil

# folder = input('Enter the folder which you want to organize files')
# reExtension = re.compile(r"""
#     ^(.*?)
#     ([0-9]+)
#     (\.[a-z]{3,4})
#     """, re.VERBOSE)
# folder = 'C:/Users/steve/Documents/StevenDD/20210723'
# files = os.listdir(os.path.abspath(folder))

# for i in range(len(files)):
#     if reExtension.search(files[i]):
#         gap = int(reExtension.search(files[i]).group(2)) - int(reExtension.search(files[i-1]).group(2))
#         if gap > 1 :
#             shutil.move(folder / reExtension.search(files[i+1]).group(), folder / reExtension.search(files[i+1]).group(1)+\
#                 str(int(reExtension.search(files[i]).group(2))-gap+1))
#         reExtension.search(files[i]).group(2)
# reExtension.findall(files).group()
