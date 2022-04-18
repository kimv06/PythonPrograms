p=float(input(" Enter the principle amount : rs. "))
r=float(input(" Enter the rate of interest : "))
t=float(input(" Enter the time in years: "))
si= (p*r*t)/100
ci= (p*(1+r/100)**t)-p
print("The simple interest is : rs. ",si)
print("The compound interest is : rs. ",ci)
