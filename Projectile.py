import numpy as np
import matplotlib.pyplot as plt

g = 9.8  
v0 = float(input("Enter the initial velocity >> ")) 
angle = float(input("Enter the launch angle >> "))  
angle_rad = np.radians(angle)


t_flight = 2 * v0 * np.sin(angle_rad) / g

t = np.linspace(0, t_flight,100)

x = v0 * np.cos(angle_rad) * t
y = v0 * np.sin(angle_rad) * t - 0.5 * g * t**2

plt.plot(x, y, label='Trajectory of the projectile', color='b')
plt.title('Projectile Motion')
plt.xlabel('Horizontal Distance (m)')
plt.ylabel('Vertical Distance (m)')
plt.grid(True)
plt.legend()
plt.show()

