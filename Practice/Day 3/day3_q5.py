string  = input("Input String: ")

digit=0
alpha=0
space=0
specialChar=0

for ch in string:
    if ch.isalpha():
        alpha+=1
    elif ch.isnumeric():
        digit+=1
    elif ch ==' ':
        space+=1
    else:
        specialChar+=1
        
print("Total Alphabets: ", alpha, "\nTotal Numbers: ", digit, "\nTotal Spaces: ", space,"\nSpecial Characters: ", specialChar)
        