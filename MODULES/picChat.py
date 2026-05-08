import matplotlib.pyplot as plt 
cars=['AUDI','BMW','FORD','TESLA','JAGUAR']
data=[23,17,35,29,12]
plt.figure(figsize=(5,5))
plt.title("Cars sales details",color='red',fontsize=20)
plt.pie(data,labels=cars,autopct='%1.1f%%',startangle=90)
plt.axis('equal')
plt.show()