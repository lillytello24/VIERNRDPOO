#from cosas import *

def main():
    per1=Persona("Jose",19)
    print(per1)
    print(Persona.descripcion)

    print("-------Herencia-------")
    al1=Alumno("Jose",19,"189765", "ICO")
    print(al1)
    print(Alumno.descripcion)

    al2=Alumno.constructor_defecto()
    print(al2)
    al2.nombre="Juan"
    print(al2)
    al2.dormir()

    print("------Herencia profe------")
    profe1=Profesor("Jesús",30 + 16,363565,"Ingenieria de Software")
    print(profe1)
    profe1.dormir()

    print("------Herencia ayudante profesor------")
    ayudante = AyudanteProfesor("Adrian", 20 , "389977", "ICO", 89999, "Ingenieria de Software",4)
    print(ayudante)
    ayudante.dormir()
    ayudante.nombre = "Abraham"
    ayudante.dar_clase("POO")
    print(ayudante)

main()
