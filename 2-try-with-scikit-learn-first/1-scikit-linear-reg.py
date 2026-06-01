from sklearn import linear_model
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

model=linear_model.LinearRegression()

modn=model.fit(ar1[:,0].reshape(-1,1),ar1[:,1])
print(modn.coef_)
print(modn.intercept_)