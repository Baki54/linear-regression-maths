import numpy as np

list1=[]

for x in np.arange(-1,1,.2):
    x=round(float(x),2)
    y=round(float(2*x**3),2)
    list1.append([x,y])

ar1=np.array(list1)

print(ar1)

#we will get this kind of dataset from here.
	      #[-1.0, -2.0], 
              #[-0.8, -1.02], 
              #[-0.6, -0.43], 
              #[-0.4, -0.13], 
              #[-0.2, -0.02], 
              #[-0.0, -0.0], 
              #[0.2, 0.02], 
              #[0.4, 0.13], 
              #[0.6, 0.43], 
              #[0.8, 1.02]
