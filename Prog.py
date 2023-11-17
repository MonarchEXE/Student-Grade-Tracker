import GradeTracker as gtDict
import GradeAvgs as gtAvgs
import TblDisplay as gtDisplay
import FileSave as gtFile

# list to locally hold all current students
# listed with a nested dict that has nested dicts
currentStudents = []

def CreateBarrier() -> None:
    # basic function that prints a barrier made of 100 dashes
    # used for dividing new menu options.
    barrier = ''
    for i in range (0,100):
        barrier += '-'
    print(barrier)
    return

def NewStudentMenu() -> None:
    CreateBarrier()
    stdName = input('Enter student\'s name (leave empty to exit): ')
    if(stdName != ''):        
        subjects = []
        print('Enter subject title (leave empty to exit): ')
        while(True):
            subject = input('')
            if(subject == ''):
                break
            subjects.append(subject)
        currentStudents.append(gtDict.CreateStudent(stdName, subjects))    
    MainMenu()

def AverageGradesMenu() -> None:
    CreateBarrier()
    print('Grade Averages Menu.')
    print('Select an option:')
    print('    1. Find average grades per student.')
    print('    2. Find average grades per subject.')
    print('    0. Exit to main menu.\n')
    choice = -1
    while(choice < 0 or choice > 2):
        try:
            choice = int(input('Enter Option: '))
        except:
            print('Invalid input.\n')
            continue
        if(choice < 0 or choice > 2):
            print('Enter a valid choice.\n')
            continue
    match choice:
        case 1:
            title = 'Grade Averages per Student'
            gtDisplay.DisplayAvgs(currentStudents,title,gtAvgs.StudentGrades)
        case 2:
            title = 'Grade Averages per Subject'
            gtDisplay.DisplayAvgs(currentStudents,title,gtAvgs.SubjectGrades)
        case 0:
            pass
    MainMenu()

def AccessGradesMenu():
    CreateBarrier()
    print('Student Grades Menu.')
    print('Select an option:')
    print('    1. Alter a student\'s subject grade.')
    print('    2. Display all student\'s grades.')
    print('    0. Exit to main menu.\n')
    choice = -1
    while(choice < 0 or choice > 2):
        try:
            choice = int(input('Enter Option: '))
        except:
            print('Invalid input.\n')
            continue
        if(choice < 0 or choice > 2):
            print('Enter a valid choice.\n')
            continue
    match choice:
        case 1:
            gtDict.AlterStudentGrade(currentStudents)
            print('\nGrade updated.\n')
        case 2:
            gtDisplay.DisplayGrades(currentStudents, gtDict.GetStudent)
        case 0:
            pass
    MainMenu()

def SaveData():
    CreateBarrier()
    print('Save/Load Data Menu.')
    print('Select an option:')
    print('    1. Save current changes to student datasheets.')
    print('    2. Load previous student datasheets.')
    print('    0. Exit to main menu.\n')
    choice = -1
    while(choice < 0 or choice > 2):
        try:
            choice = int(input('Enter Option: '))
        except:
            print('Invalid input.\n')
            continue
        if(choice < 0 or choice > 2):
            print('Enter a valid choice.\n')
            continue
    match choice:
        case 1:
            gtFile.SaveData(currentStudents)
            print('\nCurrent datasheets saved.\n')
        case 2:
            gtFile.LoadData(currentStudents)
            print('\nPrevious datasheets loaded from save directory.\n')
        case 0:
            pass
    MainMenu()

def StartMenu():
    CreateBarrier()
    print('Welcome to Student Grade Tracker!')
    gtFile.CreatePath()
def MainMenu():
    CreateBarrier()
    print('Main Menu.')
    print('Select an option: ')
    print('    1. Create a new student datasheet.')
    print('    2. Access a student\'s datasheet.')
    print('    3. Find grade averages.')
    print('    4. Save/Load student datasheets.')
    print('    0. Exit Program.\n')

    choice = -1
    while(choice < 0 or choice > 4):
        try:
            choice = int(input('Enter Option: '))
        except:
            print('Invalid input.\n')
            continue
        if(choice < 0 or choice > 4):
            print('Enter a valid choice.\n')
            continue
    match choice:
        case 1:
            NewStudentMenu()
        case 2:
            AccessGradesMenu()
        case 3:
            AverageGradesMenu()
        case 4:
            SaveData()
        case 0:
            return

import os
print(os.getcwd())
StartMenu()
MainMenu()