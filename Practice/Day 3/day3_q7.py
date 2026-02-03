string = input("Enter string: ")

if(len(string)==0):
    print("")
else:
    first_char = string[0]
    rest_string = string[1:]
    replaced = rest_string.replace(first_char,"$")
    print(first_char+replaced)

