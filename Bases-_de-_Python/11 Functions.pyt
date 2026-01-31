# Estos  son functions  en python #

from email.mime import text


def my_function():
    print("esto es una funcion ")

def sum_two_values(first_number, second_number):
    print(first_number + second_number)

sum_two_values(10, 8)

def sum_two_values_with_return(first_number, second_number):
    return first_number + second_number
result = sum_two_values_with_return(15, 25)
print(result)

def print_name(name,surmane):
    print(f"{name} {surmane}")

print_name("Alejandro", "Lanchimba") 

def print_with_default(name, surname, alias):
    print(f"{name} {surname} {alias}")
print_with_default("Alejandro", "Lanchimba", "Jaguar Ew")  
 
def print_texts(texts):
   print(texts)

my_texts = ["Hola que tal"]
print_texts(my_texts)

print("language".capitalize())
print("language".upper())
print("LANGUAGE".lower())



     




