class Student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_students(student_list):
  #Sort the list of students in descending order of CGPA key=lambda student: student.cgpa,
  sorted_students = sorted(student_list,
       key=lambda student: student.cgpa,
       reverse=True)
#Syntax - lambda arg:exp
  return sorted_students


#Example usage:
students = [
    Student("Abinaya", "c2s32551", 7.8),
    Student("Chandra", "c2s32555", 8.9),
    Student("Bhuvana", "c2s32554", 9.1),
    Student("Uma", "c2s32582", 9.9),
]
  
sorted_students = sort_students(students)

# Print the sorted list of students
for student in sorted_students:
  print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name,
                                    student.roll_number,
                                                     student.cgpa))