import numpy as np

ar1=np.array([[-1.0, -2.0], 
              [-0.8, -1.02], 
              [-0.6, -0.43], 
              [-0.4, -0.13], 
              [-0.2, -0.02], 
              [-0.0, -0.0], 
              [0.2, 0.02], 
              [0.4, 0.13], 
              [0.6, 0.43], 
              [0.8, 1.02]])


xa=np.mean(ar1[:,0])
ya=np.mean(ar1[:,1])

h=0
l=0

for row in ar1:
    h=h+  ((row[0]-xa)*(row[1]-ya))  
    l=l+  (row[0]-xa)**2
m=h/l
print(m)

c=ya-m*xa
print(c)