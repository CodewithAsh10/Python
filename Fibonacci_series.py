num =int(input("Enter the No. of Terms: "))
a,b=0,1
print(a)
print(b)
for i in range(0,num-2):
    c=a+b
    print(c)
    a=b
    b=c