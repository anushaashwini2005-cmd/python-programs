import matplotlib.pyplot as plt 
years=[2020,2021,2022,2023,2024]

results=[83,98,91,100,100]
plt.figure(figsize=(6,4))
plt.plot(years,results,marker='o')
plt.title("Student academic performane(2020-2024",color='red')
plt.xlabel("years")
plt.ylabel("resilts(%)")
plt.show()
