import random 
my_list = []
for i in range(100):
    my_list.append(random.randint(0, 1000))
    	
result = []

while my_list:
    min = my_list[0]
    for i in range(1, len(my_list)):
        if min > my_list[i]:
            min = my_list[i]
    result.append(min)
    my_list.remove(min)
print(result)