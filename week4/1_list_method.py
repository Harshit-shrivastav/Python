# List
L = [1, 2, 3, 4, 5]
# Appending to list
L.append(6)

# Printing list 
print(L)
# --> [1, 2, 3, 4, 5, 6]


# Removing an element from list
L.remove(2)
print(L)
#--> [1, 3, 4, 5, 6]
# ------------------------------>

# Nested list
L = [1 , 2, 3, 4, 5]

# Appending to list
M = [6, 7, 8, 9, 10]

# Creating Empty list X
X = []

X.append(L)
X.append(M)

print(X)
#Output Appending L and M to X
# --> [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]

# New list T
T = []
T.append(X)
print(T)
# --> [[[1, 2, 3, 4,5] , [6, 7, 8, 9, 10]]]

# Appending directly to list X
T.append([11, 12, 13, 14, 15])

print(T)
# --> [[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]]

print(T[0])
# --> [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]

#---Creating Matrix with list--->
print("--Creating Matrix with list--")
l = []
l.append([1, 2, 3])
l.append([4,5,6])
l.append([7,8,9])
print(l)
# --> [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Accessing elements in matrix
print(l[0]) # --> [1, 2, 3]
print(l[0][0]) # --> 1
print(l[0][1]) # --> 2