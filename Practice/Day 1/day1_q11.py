HRA = 10/100
TA = 5/100

basic = float(input("Enter basic pay: "));
hra_amt = basic*HRA
ta_amt = basic*TA
salary = hra_amt+ta_amt+basic

print("Basic pay: ", basic)
print("HRA amount: ", hra_amt)
print("TA amount ", ta_amt)
print("Total salary: ", salary)
