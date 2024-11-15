#!/usr/bin/env python3
# Author ID: [seneca_id]

class Student:
    # Define the name and number when a student object is created
    def __init__(self, name, number):
        self.name = name
        self.number = str(number)  # Convert to string to handle integer input
        self.courses = {}

    # Return student name and number
    def displayStudent(self):
        return f'Student Name: {self.name}\nStudent Number: {self.number}'

    # Add a new course and grade to the student's record
    def addGrade(self, course, grade):
        self.courses[course] = grade

    # Calculate and return the grade point average of all courses
    def displayGPA(self):
        if not self.courses:
            return f'GPA of student {self.name} is 0.0'  # Handle no courses case
        total_grades = sum(self.courses.values())
        gpa = total_grades / len(self.courses)
        return f'GPA of student {self.name} is {gpa}'

    # Return a list of courses that the student passed (grade > 0.0)
    def displayCourses(self):
        passed_courses = [course for course, grade in self.courses.items() if grade > 0.0]
        return passed_courses

if __name__ == '__main__':
    # Create first student object and add grades for each class
    student1 = Student('John', '013454900')
    student1.addGrade('uli101', 1.0)
    student1.addGrade('ops245', 2.0)
    student1.addGrade('ops445', 3.0)

    # Create second student object and add grades for each class
    student2 = Student('Jessica', 123456)
    student2.addGrade('ipc144', 4.0)
    student2.addGrade('cpp244', 3.5)
    student2.addGrade('cpp344', 0.0)

    # Display information for student1 object
    print(student1.displayStudent())
    print(student1.displayGPA())
    print(student1.displayCourses())

    # Display information for student2 object
    print(student2.displayStudent())
    print(student2.displayGPA())
    print(student2.displayCourses())