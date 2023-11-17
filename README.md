# Grade-Tracker
College group project for course PHYS165-A, Introduction to Data Science
Group members: Alex Burns, Gwendolyn Mick, Kurt Prado

Program is broken into six files mentioned below. This maintains modularity (at least attempts to)
and helps isolate and locate bugs in the code.
For optimal usage, ensure your IDE or text editor is configured to execute the program in a separate
terminal.

File purposes:
GradeTracker     - Handles main program features.
                   Student datasheet creation, altering student grades, adding new tracked
                   subjects, retrieving data from datasheets.
InputValidation  - Handles input validation i.e., user inputs when altering student grades.
                   Selected grade format is percentages (0-100).
FileSave         - Handles data persistence. Current changes to datasheets are saved as text files, 
                   previous datasheets loaded from text files. JSON used for translation.
Prog             - User Interface of the project. This file is to be executed during debugging
                   to run the main program.
TblDisplay       - Handles displaying student grades and grade averages in tabular format.

To use sample data:
    1. Run Prog to create the saves/ directory (folder for Windows users).
    2. Rename 'Sample Data' to 'students' and move it the saves/ directory.
