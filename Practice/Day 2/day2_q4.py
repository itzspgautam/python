nums= [1,4,1,7,8,1,9,3,10]

high=nums[0]
secondHigh=nums[0]

for n in nums:
    if n>high:
        secondHigh=high
        high = n


print("Highest: ", secondHigh)