import matplotlib.pyplot as plt

def trapezoidal(x, a, b, c, d):
    if x < a:
        return 0
    elif a <= x < b:
        return (x - a) / (b - a)
    elif b <= x <= c:
        return 1
    elif c < x <= d:
        return (d - x) / (d - c)
    else:
        return 0

a = float(input("Enter the value for a (left base): "))
b = float(input("Enter the value for b (left top): "))
c = float(input("Enter the value for c (right top): "))
d = float(input("Enter the value for d (right base): "))

if a < b <= c < d:
    x = float(input("Enter a value for x: "))
    
    val = trapezoidal(x, a, b, c, d)
    print(f"Value for x = {x}: {val}")

    x_val = [a, b, c, d]
    y_val = [0, 1, 1, 0]
    
    plt.plot(x_val,y_val, color="red", marker="o")
    plt.xlabel("X")
    plt.ylabel("Value")
    plt.title("Trapezoidal Fuzzification")
    plt.show()
else:
    print("Invalid parameters: ensure that a < b <= c < d")
