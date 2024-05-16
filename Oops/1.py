class first:
  x = 50
obj = first()
print(obj.x)
class faculty:
  def putdata(self):
    self.id = int(input("Enter faculty id:"))
    self.name = str(input("Enter faculty name:"))
    self.salary = str(input("Enter faculty salary:"))
  def display(self):
    print("Faculty id:",self.id)
    print("Faculty name:",self.name)
    print("Faculty salary:",self.salary)

a = faculty()
a.putdata()
a.display()