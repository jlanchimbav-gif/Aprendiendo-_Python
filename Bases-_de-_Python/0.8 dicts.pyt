# Estos  son diccionarios en python#
My_dict=dict()
my_other_dict={}
print(type(My_dict))
print(type(my_other_dict))
# Agregar elementos al diccionario #
My_dict["Nombre"]="Alejandro"
My_dict["Edad"]=26
My_dict["Ciudad"]="Quito"
print(My_dict)
# Update values and add idiomas list
My_dict["Edad"]=27
My_dict["idiomas"]=["español","ingles","ruso"]
My_dict.update({"Estatura":1.68})
print(My_dict)
# Acceder a los valores del diccionario #
My_dict={
    "nombre":"Alejandro",
    "edad":27,
    "ciudad":"Quito",
    "idiomas":["español","ingles","ruso"],
    "estatura":1.68,
}
print(my_other_dict)
print(My_dict)
print(len(My_dict))
print(My_dict["nombre"])
My_dict["pais"]="Ecuador"
print(My_dict)
# Eliminar elementos del diccionario #
del My_dict["ciudad"]
print(My_dict)
my_new_dict=My_dict.fromkeys ("Nombre","Alejandro")
print(my_new_dict)
