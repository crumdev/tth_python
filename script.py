"""
The dictionary will look something like:
{'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
'Kenneth Love': ['Python Basics', 'Python Collections']}

Each key will be a Teacher and the value will be a list of courses.
"""

def num_teachers(teachers):
    """Returns the number of teachers in the dictionary"""
    return len(teachers)

def num_courses(teachers):
    """Returns the number of total courses for all teachers in the dictionary"""
    return sum(len(v) for v in teachers.values())

def courses(teachers):
    """Returns a list of all available courses in the dictionary"""
    my_list = []
    for value in teachers.values():
        for course in value:
            my_list.append(course)
    return my_list

def most_courses(teachers):
    """Returns the name of the teacher that has the most courses in the dictionary"""
    winning_teacher = ""
    count = 0
    for teacher in teachers.items():
        if len(teacher[1]) > count:
            count = len(teacher[1])
            winning_teacher = teacher[0]
    return winning_teacher

def stats(teachers):
    """
    Returns a list of lists taking a the teacher dictionary and returning list where the first
    item in each inner list is the teacher's name and the second item is the number of courses that
    teacher has.
    """
    my_list = []
    for item in teachers.items():
        my_list.append([item[0], len(item[1])])
    return my_list

MY_DATA = {
    "Nathan":["beginners 101", "beginners 102", "beginners 103"],
    "Matt":["CSC 500", "CSC 501", "CSC 502", "CSC > 9000"],
    "Jon":["ENG 400", "ENG 301", "ENG 202", "ENG 600", "ENG 701", "ENG 802"]
    }

"""Test all of the functions with my example data"""

print("Number of teachers = {}".format(num_teachers(MY_DATA)))
print("Number of course = {}".format(num_courses(MY_DATA)))
print("List of courses = {}".format(courses(MY_DATA)))
print("Teacher with the most courses = {}".format(most_courses(MY_DATA)))
print("List of teachers with their total number of courses = {}".format(stats(MY_DATA)))
