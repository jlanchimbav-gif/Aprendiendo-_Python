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
