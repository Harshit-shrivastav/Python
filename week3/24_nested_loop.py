word = int(input("Enter the word:"))
len = len(word)
maxLen= 0
while(word != -1):
    if len > maxLen:
         len = maxlen
         cW = word 
    word = int(input("Enter thr number:"))
print(word)



#---------Problem 2-----------
word = str(input("Enter the word:"))
maxLen= ""
while(word != '-1'):
    if len(word) > len(maxLen):
         maxLen = word
    word = str(input("Enter the word:"))
print(len(maxLen))
