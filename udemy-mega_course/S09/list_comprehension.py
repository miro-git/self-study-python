temps = [122,234,333]

# list comprehension is a way to build new list
temps_decimal = [temp/10 for temp in temps]
print (temps_decimal)


temps_below_25 = [temp/10 for temp in temps_decimal if temp < 25] 
print (temps_below_25)
