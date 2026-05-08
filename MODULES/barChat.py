import matplotlib.pyplot as plt 
years=[2020,2021,2022,2023,2024]
strength=[23,45,67,43,90]
plt.figure(figsize=(6,4))
plt.bar(years,strength)
plt.title("Student admission Details(2020-2024)",color='red')
plt.xlabel("years")
plt.ylabel("Student Strength")
plt.show()