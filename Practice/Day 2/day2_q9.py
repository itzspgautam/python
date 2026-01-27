num =130
stringify = str(num)

sum = 0
for i in range(len(stringify)):
    sum+=int(stringify[i])
    
print("Number: ", num, "\nSum of its digit: ", sum)