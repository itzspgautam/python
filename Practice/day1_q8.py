p = float(input("Enter principle amount: "))
r = float(input("Enter rate of intrest in percentage: "))
t = float(input("Enter duration in years: "))

si = (p*r*t)/100
print("Simple Intrest: ", si)

total_si = si+p;

ci_amount = p*(1+r/100) **t
ci = ci_amount-p
print("Compount Intrest: ", ci)