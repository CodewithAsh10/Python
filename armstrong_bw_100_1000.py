def armstrong(n):
    d = str(n)
    l = len(d)
    sum_of_cube = sum(int(d) ** l for d in d)
    return sum_of_cube == n
for n in range(100,1000):
    if armstrong(n):
        print(n)
                      
        
        