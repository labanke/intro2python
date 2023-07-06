from databases import Student

students = Student.select()
#use forloop to display
for student in students:
    print(student.name, student.phoneno, student.age, student.gender, student.studentcode)
