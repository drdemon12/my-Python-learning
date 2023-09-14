import numpy as np 
result = np.array( [10,15,30,45,60] ) 
result = np.arange(5,15)
result = np.arange(50,100,5)
result = np.zeros(10)
result = np.ones(10)
result = np.linspace(0,100,5) 
result = np.random.randint(10,30,5)
result = np.random.randn(10)
result1 = np.random.randint(-50,50,15).reshape(3,5)
result = np.random.randint(10,20,5)[0:3]
result = np.random.randint(10,20,5)[::-1]
result = result1[0]
result = result1[1][2]
result = result1[:,0]
result = result1**2
result2 = result1[result1%2==0]
result = result2[result2>0]
print(result)
print(result1)