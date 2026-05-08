import matplotlib.pyplot as plt 
import numpy as np 
data=np.random.normal(20,10,50)
plt.figure(figsize=(6,4))
plt.title("Cars sales Frequency(Histogram)")
plt.hist(data,bins=5,color='lightgreen',edgecolor='green')
plt.xlabel("Number of cars sold")
plt.ylabel("Frequency")
plt.show()