import os
import shutil

from_dir = '/Users/simonebeshtoev/Desktop/python/project102/downloads'
to_dir = '/Users/simonebeshtoev/Desktop/python/project102'

list_of_files = os.listdir(from_dir)

for item in list_of_files:
    name, ext = os.path.splitext(item)
    if ext == "":
        continue
    elif ext in ['.txt', '.doc', '.docx', '.pdf', '.JPG', '.jpeg']:
        path1 = from_dir + '/' + name
        path2 = to_dir + '/' + 'document_files'
        path3 = to_dir + '/' + 'document_files' + '/' + name
        if os.path.exists(path2):
            print('moving ', name, '.....')
            shutil.move(path1, path3)
        else: 
            os.makedirs(path2)
            print('moving ' + name + '...')
            shutil.move(path1, path3)
