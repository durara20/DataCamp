import numpy as np

attempts = int(10e4)
radius = 1

inside = 0
 
x_rand_coord = np.random.default_rng().uniform(-1, 1, attempts)
y_rand_coord = np.random.default_rng().uniform(-1, 1, attempts)
 
for i in range(attempts):
    x = x_rand_coord[i]
    y = y_rand_coord[i]
    if x**2+y**2<=radius**2:
        inside+=1
             
     
area = 4*inside/attempts
print("Pi:",area)