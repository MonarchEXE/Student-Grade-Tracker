def AddStudentKeys(student, grades):
    if not(student.get('name') in grades):
        grades.update({student.get('name') : [0,0]}) 
        # student grade total held as name : [total grade, count]
        # count is num of grades student has, used to calc grade avg later on
def CollStudentGrades(stdGrades, grades, stdName):
    for grade in stdGrades.values():
        grades[stdName][0] += grade # increments total grade by subject grade
        grades[stdName][1] += 1 # increments number of grades by 1

def AddSubjectKeys(student, grades):
    for key in student['grades'].keys():
        if not(key in grades):
            grades.update({key : [0,0]})    
            # stubject grade total held as subject : [total grade, count]
            # count is num of students subject is taken by, used to calc grade avg later on
def CollSubjectGrades(stdGrades, grades) -> None:
    for subject, grade in stdGrades.items():
        grades[subject][0] += grade # increments total grade by subject grade
        grades[subject][1] += 1 # increments number of grades by 1

# used by both Grades functions, divides total grade by number of counted grades
def AvgGrades(collectedGrades, avgs) -> None:
    for subject, tuple in collectedGrades.items():
        avgGrade =  tuple[0]/tuple[1] # total grade/number of grades to get grade avg
        if not(subject in avgs):
            # avgs dictionary holds key : value of subject/student : grade average
            avgs.update({subject : avgGrade})

def SubjectGrades(students):
    listGrades = {} # holds grade totals as subject : [total grade, count] pairs 
    gradeAvgs = {} # holds grade avgs as subject : grade pairs
    for student in students:
        AddSubjectKeys(student, listGrades)
        CollSubjectGrades(student['grades'], listGrades)
    AvgGrades(listGrades, gradeAvgs)
    return gradeAvgs

def StudentGrades(students):
    listGrades = {} # hold grade totals as student name : [total grade, count] pairs
    gradeAvgs = {} # holds grade avgs as student name : grade pairs
    for student in students:
        if(len(student['grades'].values()) == 0):
            continue # skips student if they have no grades being tracked
        AddStudentKeys(student, listGrades)
        CollStudentGrades(student.get('grades'),listGrades,student.get('name'))
    AvgGrades(listGrades, gradeAvgs)
    return gradeAvgs

