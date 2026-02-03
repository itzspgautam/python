def count_ul(string):
    lower=0
    upper=0
    
    for i in range(len(string)):
        if(string[i]==string[i].lower()):
            lower+=1
        else:
            upper+=1
        
    return lower, upper
        

string = input("Enter String: ")

res = count_ul(string)

print("Total Lower: ", res[0], "\nTotal Upper: ", res[1])