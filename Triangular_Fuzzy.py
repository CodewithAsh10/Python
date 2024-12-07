import matplotlib.pyplot as plt
def tri(x, a, b, c):  
    if x < a:
        return 0
    elif a <= x < b:
        return (x - a) / (b - a)
    elif b <= x <= c:
        return (c - x) / (c - b)
    else:
        return 0

a = float(input("Enter the value for a (left base): "))
b = float(input("Enter the value for b (peak): "))
c = float(input("Enter the value for c (right base): "))

if a < b and b < c:
    x = float(input("Enter a value for x: "))
    
    val = tri(x, a, b, c)
    if val is not None:
        print(f"Value for x = {x}: {val}")
else:
    print("Invalid parameters: ensure that a < b < c")

x_val = [a,b,c]
y_val = [0,1,0]

plt.plot(x_val,y_val,color="red",marker="o")
plt.xlabel("X")
plt.ylabel("Value")
plt.title("Triangular Fuzzification" )
plt.show()
