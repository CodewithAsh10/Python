def arithmetic_sequence (a1 , d , n):
    return [ a1 + (i - 1) * d for i in range (1 , n + 1) ]
a1 = 3 # first term
d = 4 # common difference
n = 5 # number of terms
arithmetic_seq = arithmetic_sequence (a1 , d , n)
print (" Arithmetic Sequence :", arithmetic_seq )

#******************************************************************************
def geometric_sequence ( a1 , r , n):
    return [ a1 * (r ** (i - 1) ) for i in range (1 , n + 1) ]
a1 = 2 # first term
r = 3 # common ratio
n = 4 # number of terms
geometric_seq = geometric_sequence ( a1 , r , n)
print (" Geometric Sequence :", geometric_seq )

#******************************************************************************
def fibonacci_sequence ( n):
    fib_seq = [0 , 1]
    for i in range (2 , n ):
        fib_seq . append ( fib_seq [ -1] + fib_seq [ -2])
    return fib_seq [: n]
n = 10 # number of terms
fibonacci_seq = fibonacci_sequence ( n)
print (" Fibonacci Sequence :", fibonacci_seq )

#******************************************************************************

def harmonic_sequence (n ):
    return [1 / i for i in range (1 , n + 1) ]
n = 5 # number of terms
harmonic_seq = harmonic_sequence (n)
print (" Harmonic Sequence :", harmonic_seq )

#******************************************************************************
def square_numbers (n):
    return [i **2 for i in range (1 , n + 1) ]
n = 5 # number of terms
square_seq = square_numbers (n)
print (" Square Numbers :", square_seq )

#******************************************************************************

def cube_numbers (n ):
    return [i **3 for i in range (1 , n + 1) ]
n = 5 # number of terms
cube_seq = cube_numbers (n )
print (" Cube Numbers :", cube_seq )

#******************************************************************************
def triangular_numbers ( n):
    return [i * (i + 1) // 2 for i in range (1 , n + 1) ]
n = 5 # number of terms
triangular_seq = triangular_numbers (n)
print (" Triangular Numbers :", triangular_seq )

#******************************************************************************

def is_prime ( num ):
    if num <= 1:
        return False
    for i in range (2 , int ( num **0.5) + 1) :
        if num % i == 0:
            return False
        return True
def prime_numbers ( n):
    primes = []
    num = 2
    while len ( primes ) < n:
        if is_prime ( num ):
            primes . append ( num )
        num += 1
    return primes
n = 6 # number of terms
prime_seq = prime_numbers ( n)
print (" Prime Numbers :", prime_seq )

#******************************************************************************

def factorial_sequence ( n):
    factorials = [1]
    for i in range (1 , n + 1) :
        factorials . append ( factorials [ -1] * i)
    return factorials
n = 5 # number of terms
factorial_seq = factorial_sequence ( n)
print (" Factorial Sequence :", factorial_seq )

#******************************************************************************

def alternating_sequence (n):
    return [( -1) ** i for i in range (n) ]
n = 10 # number of terms
alternating_seq = alternating_sequence ( n)
print (" Alternating Sequence :", alternating_seq )

#******************************************************************************

def exponential_sequence (b , n):
    return [b ** i for i in range (1 , n + 1) ]
b = 2 # base
n = 5 # number of terms
exponential_seq = exponential_sequence (b , n )
print (" Exponential Sequence :", exponential_seq )

#******************************************************************************

from math import comb
def catalan_numbers (n):
    return [ comb (2 * i , i) // ( i + 1) for i in range (n) ]
n = 5 # number of terms
catalan_seq = catalan_numbers (n)
print (" Catalan Numbers :", catalan_seq )