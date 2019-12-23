"""
You are given a "folder" with sub-folders and files.
User enters a file path. If it's executable (and you can find the file at the end), return True.
"""
import re


folder = ['D:', ['recycle bin'], ['tmp', ['old'], ['new folder1', 'asd.txt', 'asd.bak', 'find.me.bak']], 'hey.py']
#file_path = 'D:/tmp/new folder1'
file_path = 'D:/tmp/new folder1'


def path_decoder():
    global file_path, filepathnew
    filepathnew = file_path.split('/')
    return filepathnew


def file_search(folder):
   path_level = 0
   while path_level <= len(filepathnew):
        regexpr = bool(re.findall(filepathnew[path_level], folder))
        if regexpr:
            path+=1
            continue
            current_folder = filepathnew[1]

#find length of filepathnew, use for cyclical search


#print(path_decoder())
