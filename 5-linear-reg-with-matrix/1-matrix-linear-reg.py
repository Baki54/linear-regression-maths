import numpy as np

ar1=np.array([[1,  -1.0, -2.0], 
              [1,  -0.8, -1.02], 
              [1,  -0.6, -0.43], 
              [1,  -0.4, -0.13], 
              [1,  -0.2, -0.02], 
              [1,  -0.0, -0.0], 
              [1,  0.2, 0.02], 
              [1,  0.4, 0.13], 
              [1,  0.6, 0.43], 
              [1,  0.8, 1.02]])  # 1 is added to the first column
x=ar1[:,0:2]
y=ar1[:,2]


ans2=(np.linalg.inv(x.T@x))@x.T@y
print(ans2)