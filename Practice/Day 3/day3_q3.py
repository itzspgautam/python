def count_vc(string):
    vowel=0
    cons=0
    string=string.upper()
    
    for i in range(len(string)):
        if(string[i]=="A" or string[i]=="E" or string[i]=="I" or string[i]=="O" or string[i]=="U"):
            vowel+=1
        else:
            cons+=1
        
    return vowel, cons
        

string = input("Enter String: ")

res = count_vc(string)

print("Total vowels: ", res[0], "\nTotal Consonant: ", res[1])