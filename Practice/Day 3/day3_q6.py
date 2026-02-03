def charConcat(string):
    if(len(string)<=2): return ""
    return string[:2]+string[-2:]
    
string = input("Enter string: ")
print("Result: ", charConcat(string))