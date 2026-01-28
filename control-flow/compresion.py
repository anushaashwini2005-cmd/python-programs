c=[items**2 for items in range(1,11)]  # List comprehension
print(c)


population={
    "Mysore":100,
    "Banglore":200,
    "Manglore":250
}
b={keys:value for keys,value in population.items() if value<=200} # dictionary comprehension
print(b) 
