class student:
  def __init__(self,name,age,grade):
    self.name=name
    self.age=age
    self.grade=grade


  def average(self):
    return sum(self.grade)/len(self.grade)

first_student = student("Harshit" , 20 , [20,30,40,50])
print(first_student.name)
print(first_student.average())