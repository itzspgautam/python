string = input("Enter string: ")
string2 = input("Enter 2nd string: ")


if(len(string)==0 or len(string2)==0):
    print("")
else:
    first_two_char= string[:2]
    first_two_char_str2 =string2[:2]
    print(string.replace(string[:2], first_two_char_str2)+ " "+ string2.replace(string2[:2], first_two_char))


