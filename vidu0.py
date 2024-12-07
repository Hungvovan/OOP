from datetime import datetime

class Student:
    subject = "Python" 

    def __init__(self, student_id, name, day_birth, score1, score2):
        self.student_id = student_id 
        self.name = name  
        self.day_birth = datetime.strptime(day_birth, "%d/%m/%Y") 
        self.score1 = score1 
        self.score2 = score2

    def average_score(self):
        return (self.score1 + self.score2) / 2

    def __str__(self):
        
        avg = self.average_score()
        return f"ID: {self.student_id}, Name: {self.name}, Day of Birth: {self.day_birth.strftime('%d/%m/%Y')}, Average Score: {avg:.2f}"

    def __lt__(self, other):
        return self.day_birth < other.day_birth


def input_students():
    """Hàm nhập danh sách sinh viên"""
    n = int(input("Enter the number of students: "))
    if n < 1 or n > 50:
        return []

    students = []
    for i in range(n):
       
        student_id = input("Enter ID: ")
        name = input("Enter Name: ")
        day_birth = input()
        score1 = float(input("Enter Score 1: "))
        score2 = float(input("Enter Score 2: "))
        student = Student(student_id, name, day_birth, score1, score2)
        students.append(student)
    return students


def display_students(students):
    for student in students:
        print(student)


def main():
    students = input_students()  #
    if students:  
        students.sort() 
        display_students(students) 


if __name__ == "__main__":
    main()
