# Estas  son listas  en python#
my_list=list()
My_other_list=[1,2,3,4,5,6,7,8,9,10]
print(len(My_other_list))
my_second_list=["jorge",26,1.70,]
print(type(my_second_list))
print(my_second_list[0])
print(my_second_list[1])
print(my_second_list[2])
print(my_second_list[-1])
#insertando elementos en la lista#
My_other_list.insert(1,"azul")
print(My_other_list)
# removiendo elementos de la lista#
My_other_list.remove("azul")
print(My_other_list)

print(My_other_list.reverse())
# La función reverse() invierte el orden de los elementos en la lista.
print(My_other_list)

# ordenando la lista#
My_other_list.sort()