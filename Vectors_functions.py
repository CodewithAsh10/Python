import numpy as np
import math
a=np.array([1,2,3])
b=np.array([4,5,6])
dot_ab=np.dot(a,b)
print("Dot Product is = ",dot_ab)
cross_ab=np.cross(a,b)
print("Cross Product is = ",cross_ab)
mag_a = np.linalg.norm(a)
mag_b = mag_a = np.linalg.norm(b)

print("Magnitude of A: ",mag_a)
print("Magnitude of B: ",mag_b)
cos_theta = dot_ab / (mag_a * mag_b)
ang_ab=np.arccos(cos_theta)
angle_degree = np.degrees(ang_ab)
print("Angle b/w AB (in radians) : ",ang_ab)
print("Angle b/w AB (in degree) : " ,angle_degree)