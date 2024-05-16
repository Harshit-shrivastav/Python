empId = int(input("Enter employee ID:"))

sum = 0
amount = 1
while(empId !=-1):
    while(amount != 0):
        amount = int(input("Enter amount"))
        sum += amount
    print("Total amount for employee",empId,"is",sum)
    empId = int(input("Enter employ Id:"))
print(sum)
