a=(int)(input("enter first number"))
b=(int)(input("enter second number"))
hcf=1
lcm=a*b
for i in range(2,min(a,b)):
    if a%i==0 and b%i==0:
        hcf=i

print("the HCF of given numbers is: ",hcf)

for i in range(max(a,b),a*b+1):
    if i%a==0 and i %b==0:
        lcm=i
        break
print("the LCM of the given two numbers is: ",lcm)