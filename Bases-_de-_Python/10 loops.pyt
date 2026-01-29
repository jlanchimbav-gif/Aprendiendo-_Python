# Estos  son loops en python #

#while

my_condition = 0

while my_condition < 10:
    print("El valor de la condición es:", my_condition)
    my_condition += 1

if my_condition == 10:
    print("La condición es igual a 10")
else:
    print("la ejecucion continua")


while my_condition < 20:
    my_condition+=1
    if my_condition == 15:
        print("mi condición es 15")
        break
    print(my_condition)

print("la ejecución continúa")

#for
my_list = [35, 24, 52, 12, 18]
for element in my_list:
    print("El elemento de la lista es:", element)

my_tuple = (150, 250, 350, 450, 550)
my_set = {1000, 2000, 3000, 4000, 5000}  

for element in my_tuple:
    print("El elemento de la tupla es:", element)

for element in my_set:
    print("El elemento del conjunto es:", element)