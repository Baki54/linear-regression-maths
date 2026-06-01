import numpy as np

ar1=np.array([[3,1,-1, 3],
              [2,-8,1,-5],
              [1,-2,9, 8]])
x=ar1[:,0:3]
y=ar1[:,3]

ans=np.linalg.solve(x,y)
print(ans)

ans2=(np.linalg.inv(x.T@x))@x.T@y
print(ans2)