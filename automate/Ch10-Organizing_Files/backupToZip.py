import zipfile
import os
from pathlib import Path

p = Path.home()
Path(p/'spam').mkdir()
Path.cwd()
os.chdir(p/'spam')
Path.cwd()
baconFile = open('bacon.txt', 'w')
baconFile.write('To be backed up\n')
baconFile.close()

# 正文


def backupToZip(folder):
    # Backup the entire contents of "folder" into a ZIP file.
    folder = os.path.abspath(folder)  # make sure folder is absolute
    # Figure out the filename this code should use based on
    # what files already exist.
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):  # 如果此路徑不存在名字相同的檔案則break
            break
        number = number + 1
    # Create the ZIP file.
    print(f'Creating {zipFilename}...')
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # Walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print(f'Adding files in {foldername}...')
        # Add the current folder to the ZIP file.
        backupZip.write(foldername)
        # Add all the files in this folder to the ZIP file.
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done.')


folder = Path.cwd()
folder
backupToZip(Path.cwd())  # WindowsPath('C:/Users/user/spam')
abspath = os.path.abspath(Path.cwd())
os.path.basename(abspath)
