import os
from pathlib import Path
Path('spam', 'bacon', 'eggs')
str(Path('spam', 'bacon', 'eggs'))
Path.cwd()
str(Path(Path.cwd()) / 'steven')
Path.home()

Path(Path.cwd()/'spam').mkdir()
Path(Path.cwd()/'spam').rmdir()
# 引數的絕對路徑的字串
os.path.abspath('.')
# 擷取檔案路徑的各個部分
p = Path(Path.cwd())
p.anchor
p.parent
os.path.dirname(p)
p.name
os.path.basename(p)
p.stem
p.suffix
p.drive
# 取得工作資料夾以上路徑的分別名稱字串
str(p).split(os.sep)
os.path.getsize('./Ch4-Lists/conway.py')
os.listdir('.')
# glob
p
p.glob('*')
list(p.glob('*'))
p.is_file()
p.is_dir()
# open and edit files
p = Path('spam.txt')
p.write_text('Hello, world!')
p.read_text()
# writing files
baconFile = open('bacon.txt', 'w')
baconFile.write('Hello world!\n')
baconFile.close()
baconFile = open('bacon.txt', 'a')
baconFile.write('Bacon is not a vegetable.')
baconFile.close()
