# Estos  son classes en python #

class myemptyperson:
    pass

print(myemptyperson) 
print(myemptyperson())

class person:
    def __init__(self, name, surname):
        self.fullname = f"{name} {surname}"

    def walk (self):   
        print( f"{self.fullname} esta caminando")  


my_person=person("Alejandro", " Lanchimba")
print(my_person.fullname)
my_person.walk()


 




     




