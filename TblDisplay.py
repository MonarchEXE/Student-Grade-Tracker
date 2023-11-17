'''
File creates a table to display average grades in table format.
Contains four functions:
    HorizontalBar()
    VerticalBar(title)
    GradeBar(subject, grade)
    DisplayGrades(students, title, function)
'''
def HorizontalBar() -> str:
    horizontalBar = ''
    '''
    returns string of 50 dashes
    used to show the beginning/end of a table
    '''
    for i in range(0,50):
        horizontalBar += '-'
    return horizontalBar
def VerticalBar(title) -> str:
    '''
    function that returns row containing title
    title is passed as parameter when called
    '''
    vBar = '|   '
    vBar += title
    for i in range(0,45-len(str(title))):
        vBar += ' '
    vBar += '|'
    return vBar
def GradeBar(subject, grade) -> str:
    '''
    prints row of width 50 split in two columns
    column one contains subject/student name, two shows the grade.
    '''
    vBar = '| '
    vBar += subject
    for i in range(0,(30-len(subject))):
        vBar += ' '
    vBar += '|'
    for i in range(0,(15-len(str(grade)))):
        vBar += ' '
    vBar += str(grade)
    vBar += ' |'
    print(vBar)

def DisplayAvgs(students, title, function) -> None:
    '''
    function parameter takes a function that collects and calculates grade averages
    function import only needed in Prog() where this function is called.
    '''
    xBar = HorizontalBar()
    titleBar = VerticalBar(title)

    print(xBar)
    print(titleBar)
    print(xBar)
    gradeAvgs = function(students)
    for subject, grade in gradeAvgs.items():
        GradeBar(subject, grade)
    print(xBar)

def DisplayGrades(students, _func):
    student = _func(students)
    if(student == None):
        print('\nStudent not found.\n')
        return
    xBar = HorizontalBar()
    titleBar = VerticalBar(student.get('name'))

    print(xBar)
    print(titleBar)
    print(xBar)
    for subject, grade in student['grades'].items():
        GradeBar(subject, grade)
    print(xBar)
