#COMENTARIO UNA SOLA LINEA
# NO PONER PUNTO Y COM
'''
asdfdafsdfasdfasdf
asdfasdfasdf
asdfasdfdfa

'''
#variables, no es necesario definir el tipo de dato
from cgi import print_form
from encodings import CodecRegistryError


nombre= "cesar"#String
numero=55#Int
decimal=3,1415#Float

diaSemana=["lunes","martes","miercoles","jueves","viernes"]#Lista o Array
listaDinamica=["hola",22,False,33,4,[3,2]]#los array pueden ser de 1 o mas tipos de datos a la vez
print(diaSemana[2])#deberia imprimir miercoles
print(listaDinamica[5][1])#imprimir la posicion de una matriz

#Diccionarios -JSON - Objects
persona ={
'nombre':"Cesar",
'apellido' : "Diazgranados",
'edad':27,
'materias':["Base de datos 2","lenguaje de cuarta generacion"]

}
print(persona["nombre"])
print(persona["materias"][1])
print(persona)

#lista de diccionarios
personas=[
    {
      'nombre':"Cesar",
'apellido' : "Diazgranados",
'edad':27,
'materias':["Base de datos 2","lenguaje de cuarta generacion"]
  
    },
{
    'nombre':"camilo",
'apellido' : "hernandez",
'edad':27,
'materias':["Base de datos 2","lenguaje orientado objetos"]
},
{
    'nombre':"juan",
'apellido' : "lopez",
'edad':27,
'materias':["Base de datos 2","lenguaje orientado a eventos"]

},



]
print(personas[2]["materias"][1])


#condiciones
esMayorEdad=True
if esMayorEdad== True:
    #esto es parte del if
    print('Es mayor de edad')
else:
    #esto es parte del else
        print('no es mayor de edad')
#la tablulacion es muy importante
print('mensaje de prueba')
# and es "y" y el or es el "o"

for per in personas:
    print(per['edad'])
    print("")
    
nombrePersonas = "roberto"
print(nombrePersonas[2])
print("")



verbo = "correr" 


print(verbo [len(verbo)-1])

#hola
