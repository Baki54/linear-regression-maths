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
differ=np.diff(ar1,axis=0)

sum_m=0
for row in differ:
    m=row[1]/row[0]
    sum_m=sum_m + m
    

slope=sum_m/9
print(slope)

c=0
for row in ar1:
    c=row[1] - slope*row[0] +c
    
c=c/10
print(c)
