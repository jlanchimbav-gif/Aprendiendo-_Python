# Estos  son exception halding  en python #

numberone=10
numbertwo=0

## try except ##
try:
    result= numberone + numbertwo
    print(" no se ha producido un error ", result)
except:
    print("se ha producido un error")

 ## try except else ##   
try:
   print(numberone + numbertwo)
   print(" no se ha producido un error ")
except:
    print("Se ha producido un error")
else:
    print("La ejecucion continuo correctamente")

 ## try except else finally ##  
try:
   print(numberone + numbertwo)
   print(" no se ha producido un error ")
except:
    print("Se ha producido un error")
else:
    print("La ejecucion continuo correctamente")
finally: 
    print("La ejecucion continua")   

 ## eceptiones por tipo ##
try : 
    print(numberone + numbertwo)
    print(" no se ha producido un error ")
except ValueError:
    print("Error de valor")    
except TypeError:
    print("Error de tipo de dato")

# captura de informacion del error ##
try : 
    print(numberone + numbertwo)
    print(" no se ha producido un error ")
except ValueError as error:
    print("Error de valor: ", error)     





