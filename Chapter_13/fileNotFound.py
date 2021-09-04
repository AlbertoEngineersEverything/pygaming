import os

def fileExists(file_name):
    try:
        with open(file_name, 'r') as f:
            f.close()
            return True

    except IOError:
        return False


print(fileExists('fileNotFound.py'))

print(fileExists('this-does-not-exist.txt'))
