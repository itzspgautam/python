totalItems = int(input("Enter total number of items: "));

items= [];

for i in range(totalItems):
    name = input("Enter item name: ")
    qty = int(input("Enter quantity: "))
    price = float(input("Enter price: "))
    subtotal = qty*price
    
    items.append({
       "Name": name, "Quantity": qty, "Price": price, "Subtotal": subtotal
        })
    
  
print("=============INVOICE=============")
print("NAME          Price          Quantity          Subtotal")
total =0;
for item in items:
    print(item['Name']+"          ",item['Price'],"          ",item['Quantity'],"          ",item['Subtotal'])    
    total+=item["Subtotal"]
    
print("Total Payble: ", total)