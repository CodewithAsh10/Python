print("Pattern 1")
print()
a = int(input("Enter = "))
for i in range(1,a+1):
    for j in range(0,i):
        print(i,end = " ")
    print("")
#*********************************************************
print()
print("Pattern 2")
print()
n = int(input("Enter: ").strip())
for i in range(1,n+1):
    for j in range(0,n-i):
        print(end=" ")    
    for k in range(1,i+1):
        print(i,end = "")        
    print()
#**********************************************************
print()
print("Pattern 3")
print()
a = int(input("Enter = "))
for i in range(1,a+1):
    for k in range(a-i):
        print(" ",end='')
    for j in range(0,i):
        print(i,end = " ")
    print("")
#********************************************************
print()
print("Pattern 4")
print()  
n = int(input("Enter: ").strip())
for i in range(1, n+1):
    for j in range(0, i):
        print(i, end=' ')
    print()


for i in range(n, 0, -1):
    for j in range(0, i):
        print(i, end=' ')
    print()
#*****************************************************
print()
print("Pattern 5")
print()
n = int(input("Enter: ").strip())
for i in range(1,n+1):
    for j in range(0,n-i):
        print(end=" ")    
    for k in range(1,i+1):
        print(i,end = "")        
    print("")

for i in range(n,0,-1):
    for j in range(0,n-i):
        print(end=" ")    
    for k in range(0,i):
        print(i,end = "")        
    print("")
#**********************************************************

print()    
print("Pattern 6")
print()
n = int(input("Enter: ").strip())
for i in range(1, n+1):
    for k in range(0,n-i):
        print(end=" ")
    for j in range(0, i):
        print(i, end=' ')
    print()


for i in range(n, 0, -1):
    for k in range(0,n-i):
        print(end=" ")
    for j in range(0, i):
        print(i, end=' ')
    print()
#*************************************************
