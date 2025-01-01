#Graph Codes
#Vertical Bar Graph
import matplotlib.pyplot as plt
categories = ['A','B','C','D']
values = [10 , 20, 15, 25]
plt.bar( categories , values , color ='skyblue')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Vertical Bar Chart')
plt.show()

#Horizontal Bar Graph
categories = ['A','B','C','D']
values = [10 , 20, 15, 25]
plt.barh( categories , values , color ='skyblue')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Horizontal Bar Chart')
plt.show()

#Grouped Bar Chart
import matplotlib . pyplot as plt
import numpy as np
categories = ['A','B','C','D']
values1 = [10 , 20, 15, 25] 
values2 = [12 , 22, 17, 27]
n = len( categories )
x = np.arange (n)
width = 0.35 
fig , ax = plt . subplots ()
bars1 = ax.bar(x - width /2, values1 , width ,label ='Group 1', color ='skyblue')
bars2 = ax.bar(x + width /2, values2 , width ,label ='Group 2', color ='salmon')
ax.set_xlabel ('Categories')
ax.set_ylabel ('Values')
ax.set_title ('Grouped Bar Chart')
ax.set_xticks (x)
ax.set_xticklabels ( categories )
ax.legend ()
plt.show ()

#Stacked Bar Chart
import matplotlib . pyplot as plt
import numpy as np
categories = ['A','B','C','D']
values1 = [10,15,20,25] 
values2 = [5,10,10,20]
n = len( categories )
x = np. arange (n)
width = 0.5 
fig , ax = plt . subplots ()
bars1 = ax.bar(x, values1 , width ,label ='Group 1', color ='skyblue')
bars2 = ax.bar(x , values2 , width ,label ='Group 2', color ='salmon')
ax.set_xlabel ('Categories')
ax.set_ylabel ('Values')
ax.set_title ('Stacked Bar Chart')
ax.set_xticks (x)
ax.set_xticklabels ( categories )
ax.legend ()
plt.show ()

#Line Chart
import matplotlib . pyplot as plt
years = [2020 , 2021 , 2022 , 2023]
values = [100 , 150 , 200 , 250]
plt. plot (years , values , marker ='o',linestyle ='-', color ='green')
plt. xlabel ('Year')
plt. ylabel ('Values')
plt. title ('Line Chart')
plt. show ()

#Multiple Line Chart 
import matplotlib . pyplot as plt
months= ['Jan','Feb','March','April','May','June','July','Aug','Sept','Oct','Nov','Dec']
A = [500,700,800,650,900,1000,1100,950,1150,1200,1300,1400]
B = [400,600,700,800,900,1000,200,300,700,1000,500,900]
plt. plot (months,A, values , marker ='o',linestyle ='-', color ='green',label='Store A revenue')
plt. plot (months,B, values , marker ='o',linestyle ='-', color ='green',label='Store A revenue')
plt. xlabel ('Months')
plt. ylabel ('Revenue')
plt. title ('Monthly Revenue of store A and store B')
plt. show ()


#Pie Chart
import matplotlib . pyplot as plt
cars = ['AUDI', 'BMW', 'FORD','TESLA', 'JAGUAR', 'MERCEDES']
data = [23, 17, 35, 29, 12, 41]
fig = plt.figure(figsize=(10, 7))
plt.pie(data, labels=cars,autopct='%1.1f%%',startangle=90,shadow=True)
plt.show()

#Scatter Plot
import matplotlib . pyplot as plt
x = [1, 2, 3, 4, 5]
y = [10 , 20, 15, 25, 30]
plt. scatter (x, y, color ='red')
plt. xlabel ('X Axis')
plt. ylabel ('Y Axis')
plt. title ('Scatter Plot')
plt. show ()

#Annotated Scatter Plot
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 3, 5]
annotations = ['A', 'B', 'C', 'D', 'E']
plt.figure(figsize=(8, 6))
plt.scatter(x, y, color='blue', marker='o')
for i, label in enumerate(annotations):
    plt.text(x[i], y[i] + 0.2, label, fontsize=10, ha='center', color='red')
plt.title("Annotated Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()


#Histogram
import matplotlib . pyplot as plt
ages = [23,45,23,34,25,30,40,45,23,22]
plt.hist(ages,bins=8, color ='blue',edgecolor='black')
plt. xlabel ('Age')
plt. ylabel ('No. of Participation')
plt. title ('Histogram')
plt. show ()
