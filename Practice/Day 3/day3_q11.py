string = "This movie is not that poor"

pos_poor = string.find("poor")
pos_not = string.find("not")

if(pos_not<pos_poor):
    print(string[:pos_not-1],"good")
else:
    print(string)