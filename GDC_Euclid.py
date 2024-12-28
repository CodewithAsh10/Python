def gcd_euclid(x,y):
    while y:
        x,y = y,x%y
    return x

n1 = int(input("Enter the first no: "))
n2 = int(input("Enter the second no: "))
print(f"The Greatest common divisor between {n1} and {n2} is {gcd_euclid(n1,n2)}")
