import zipfile
import shutil
import os
import send2trash
from pathlib import Path
p = Path.home()
# 更換現在工作位置到home
os.chdir(p)
Path.cwd()
# 檔案寫入
spamFile = open('spam.txt', 'w')
spamFile.write('Hello, there!\n')
spamFile.close()
# 檔案複製
shutil.copy(p / 'spam.txt', p / 'documents')
shutil.copy(p / 'spam.txt', p / 'documents/spam2.txt')
# 創造home之下的spam資料夾
Path(p/'spam').mkdir()
shutil.copytree(p / 'spam', p/'spam_backup')
# 創造home之下的move.txt
moveFile = open('move.txt', 'w')
moveFile.write("I'm moving right now ~ ")
moveFile.close()
# 移動moveFile 到 documents
shutil.move(p / 'move.txt', p / 'documents')
shutil.move(p / 'documents/move.txt', p)
shutil.move(p / 'move.txt', p / 'documents/new_move.txt')
shutil.move(p / p / 'documents/new_move.txt', p / 'move.txt')
# 如果沒有移動目標的資料夾，則會創造該名稱的資料夾，預期結果不同，為該名稱資料夾而非該名稱資料夾下的txt檔
shutil.move(p / 'move.txt', p / 'idiot')
# permanently deleting files and folders
print(p / 'idiot')
os.unlink(p / 'idiot')
for filename in Path(p / 'documents').glob('*.txt'):
    print(filename)
    os.unlink(filename)  # delete spam & spam2 txt files.
# send2trash module send to recycle bin
baconFile = open('bacon.doc', 'a')  # creates the file
baconFile.write('Bacon is not a vegetable.')
baconFile.close()
send2trash.send2trash('bacon.txt')
# os.walk walk through directory tree
p = Path.home()
for folderName, subfolders, filenames in os.walk(Path(p / 'Pictures')):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': ' + filename)

    print('')
# zipfile module
p = Path.home()
exampleZip = zipfile.ZipFile(p / 'example.zip')
exampleZip.namelist()
spamInfo = exampleZip.getinfo('spam.txt')
spamInfo.file_size
spamInfo.compress_size
f'Compressed file is {round(spamInfo.file_size / spamInfo.compress_size, 2)}x smaller!'
exampleZip.close()
# 解壓縮檔案到cwd
exampleZip = zipfile.ZipFile(p / 'example.zip')
exampleZip.extractall()
exampleZip.close()
# 建立與新增到ZIP檔中
newZip = zipfile.ZipFile('new.zip', 'w')
newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()
