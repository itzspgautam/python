string = input("Enter string: ")

if(len(string)<3):
    print(string)
else:
    last_3_char = string[-3:]
    if(last_3_char == "ing"):
        print(string+"ly")
    else:
        print(string+"ing")
    