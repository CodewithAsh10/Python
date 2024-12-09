a = input("Enter String: ")
substr = {}
patstr = {}
for i in range(len(a)):
    n = a[i:len(a):2]
    substr[f'substr_{i}'] = n
for key, value in substr.items():
    print(f"{key}: {value}")
for key, n in substr.items():
    patstr[key] = [] 
    for j in range(len(n) - 1):
        if n[j] == n[j + 1]:
           
            patstr[key].append(1)  
            patstr[key].append(1)  
        else:
            patstr[key].append(0)  
        
           
    
    if len(n) > 0:
        patstr[key].append(0)  

    print(f"Pattern for {key}: {patstr[key]}")