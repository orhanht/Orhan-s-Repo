"""
Instructions:

Given students' names along with the grade that they are in, create a roster for the school.
In the end, you should be able to:
Add a student's name to the roster for a grade
"Add Jim to grade 2."
"OK."
Get a list of all students enrolled in a grade
"Which students are in grade 2?"
"We've only got Jim just now."
Get a sorted list of all students in all grades. Grades should sort as 1, 2, 3, etc., and students within a grade should be sorted alphabetically by name.
"Who all is enrolled in school right now?"
"Grade 1: Anna, Barb, and Charlie. Grade 2: Alex, Peter, and Zoe. Grade 3…"
"""

class School(object):
    def __init__(self):
        self.enrollment = {}

    def add_student(self, name, grade):
        if grade in self.enrollment:
            self.enrollment[grade].append(name)
            self.enrollment[grade] = sorted(self.enrollment[grade])
        else:
            self.enrollment[grade] = [name]

    def roster(self):
        roster_kids = []
        for i in sorted(self.enrollment.keys()):
            for j in self.enrollment[i]:
                roster_kids.append(j)
        return roster_kids

    def grade(self, grade_number):
        return self.enrollment.get(grade_number, [])
