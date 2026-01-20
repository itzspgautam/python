address= input("Enter address (Comma Separeted): ")
addressArr = address.split(',')

print(addressArr)
total = len(addressArr)

for a in addressArr:
    print(a)