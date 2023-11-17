def ValidInput() -> int:
    grade = input('Enter subject grade: ')
    if(TypeCheck(grade) == False or ValueCheck(grade) == False):
        return None
    valid = True
    return int(grade)
def ValueCheck(value) -> bool:
   #checks if the grade is within valid values
    if(int(value) < 0 or int(value) > 100):
        print('\nEnter a valid grade.\n')
        return False
    return True
def TypeCheck(value) -> bool:
    # checks if the grade is of the correct DataType (this case, an integer)
    # in the instance of a float, it just floors the value (18.95 becomes 18)
    try:
        value = int(value)
        return True
    except:
        print('\nInvalid input.\n')
        return False