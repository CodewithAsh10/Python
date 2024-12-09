INFINITY_ = 99999999

def sqrtByLongDivision(n, decimal_places=5):
    if n < 0:
        raise ValueError("Cannot compute square root of negative numbers.")
    
    # Preparing for long division
    i = 0
    a = []
    
    # Dividing the number into segments of two digits
    while n > 0:
        a.append(n % 100)  # Extracting two digits (a segment)
        n //= 100          # Moving to the next two digits
        i += 1

    a.reverse()  # Reverse to start from the most significant segment

    cur_quotient = 0.0
    cur_divisor = 0.0
    cur_dividend = 0.0
    cur_remainder = 0.0

    # Start long division from the first segment
    for j in range(i):
        # Include the next segment in the current dividend
        cur_dividend = cur_dividend * 100 + a[j]
        cur_remainder = INFINITY_

        # Loop to find the largest udigit
        for udigit in range(10):
            # Check if the current divisor and udigit fit
            if (cur_remainder >= cur_dividend - ((cur_divisor * 10 + udigit) * udigit) and 
                cur_dividend - ((cur_divisor * 10 + udigit) * udigit) >= 0):
                cur_remainder = cur_dividend - ((cur_divisor * 10 + udigit) * udigit)
                quotient_units_digit = udigit

        # Update the quotient and divisor
        cur_quotient = cur_quotient * 10 + quotient_units_digit
        cur_divisor = cur_quotient * 2
        cur_dividend = cur_remainder

    # Calculate decimal places
    for _ in range(decimal_places):
        cur_dividend *= 100  # Shift the remainder for decimal place calculation
        cur_remainder = INFINITY_

        for udigit in range(10):
            if (cur_remainder >= cur_dividend - ((cur_divisor * 10 + udigit) * udigit) and 
                cur_dividend - ((cur_divisor * 10 + udigit) * udigit) >= 0):
                cur_remainder = cur_dividend - ((cur_divisor * 10 + udigit) * udigit)
                quotient_units_digit = udigit

        cur_quotient = cur_quotient * 10 + quotient_units_digit
        cur_divisor = cur_quotient * 2
        cur_dividend = cur_remainder

    # Return the square root as a float
    return cur_quotient / (10 ** decimal_places)

# Driver code
x = int(input("Enter the Number: "))
print(sqrtByLongDivision(x))  # Output: square root of 11 as float


