isDuplicate = False
N=5
nums =[]
for n in range(N):
    num = int(input("Enter " + str(n+1) + " Number: "))
    if num in nums:
        isDuplicate=True
    nums.append(num)
        
        
        
if(isDuplicate):
    print("DUPLICATES")
else:
    print("ALL UNIQUE")