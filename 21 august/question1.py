str=input("enter your birth date: ")

str2=str.split("-")
str3=str.split("-")
print("\n\nthe entered birth date is:", "/".join(str2))

mydict=dict()

mydict["Day"]=str3[0]
mydict["Month"]=str3[1]
mydict["Year"]=str3[2]

print(mydict)
