def power_raising(base, exponent):
    result = 1
    
    while exponent > 0:
        if exponent % 2 == 1:
            result *= base
        exponent //= 2
        base *= base
    return result

print("Exponent ...")
base = int(input("Enter the base number: "))
exponent = int(input("Enter the power: "))

result = power_raising(base, exponent)
print(f"The result of ({base}^{exponent}) is: {result}")
