nums = [1,2,3,4,5,6,7,8,34,5,6,7,87,12,67,5,7,98,12,98,7,3,76,8,12,8,7,9,90,7,45];
even  = []
odd = []

for n in nums:
    if n%2==0:
        even.append(n)
    else:
        odd.append(n)
        
        
print("Odd Numbers:" , odd)
print("Even Numbers: ", even)