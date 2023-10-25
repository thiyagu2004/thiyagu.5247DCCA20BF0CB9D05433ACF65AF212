class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students


students = [
    Student("Hari", "A123", 7.8),
    Student("Sri", "A124", 8.9),
    Student("sai", "A125", 9.1),
    Student("Mani", "A126", 9.9),
]

sorted_students = sort_students(students)


for student in sorted_students:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")