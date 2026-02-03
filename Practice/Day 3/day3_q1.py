def find_ch(string, pos):
    if(pos>len(string)):
        print("Character not found at position", pos)
    print("Character",string[pos], " found at Position ", pos)
    
    
    
string =  input("Enter string: ")
pos = int(input("Enter position to search: "))

search = find_ch(string, pos-1)
