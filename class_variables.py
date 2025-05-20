class Student:

    class_year=2026
    num_students=0

    def __init__(self,name,age):
        self.name = name
        self.age = age
        Student.num_students += 1

student1=Student("James",61)
student2=Student("Kirk",62)
student3=Student("Jason",62)
student4=Student("Lars",61)

print(f"My graduating class of {Student.class_year} has {Student.num_students} students")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)

