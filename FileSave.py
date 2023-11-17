from pathlib import Path
import json
import os

savePath = Path(os.getcwd() + '/saves/')
saveFile = Path('students.txt')

def CreatePath() -> None:
    # creates saves directory for datasheets 
    if not(os.path.isdir(savePath)) == True: # checks if the directory doesn't exist
        os.mkdir(savePath) # makes directory
        _prevdir = ConnectPath()
        _stream = open(saveFile, 'w+') # creates new text file for student grades
        CloseSave(_stream, _prevdir)

def ConnectPath() -> None:
    prevdir = os.getcwd()
    '''
    current directory saved as variable 'prevdir' to return to after closing function
    without returning to prevdir, imports may not work in Prog
    '''
    os.chdir(savePath) # changes directory to save directory
    return prevdir # previous directory returned

def OpenSave():
    prevdir = ConnectPath()
    if saveFile.is_file() == True:
        return open(saveFile, 'r+'), prevdir
    # open(fileName, flag) locates and opens file of given name. returns fileStream to read and cha
    # r+ flag opens file without truncating (removing the content) 
def CloseSave(stream, dir) -> None:
    stream.close()
    os.chdir(dir) #changes directory to pass Path, this case the previous directory

def LoadData(students) -> None:
    save, prevdir = OpenSave()
    students.clear() # deletes all previous dictionaries to remove chance of duplicates
    for line in save.readlines():
        students.append(json.loads(line)) # json.loads() converts line from text file to python dictionary
    CloseSave(save, prevdir)

def SaveData(students) -> None:
    save, prevdir = OpenSave()
    save.truncate(0) # removes all previous content
    for student in students:
        save.write(json.dumps(student)+'\n') # json.dumps() converts python dictionary to text file
    CloseSave(save, prevdir)