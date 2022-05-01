from django.http import HttpResponse
import datetime
from django.template import Template, Context

class Persona(object):
    
    def __init__(self, nombre2, apellido2):
        
        self.nombre2 = nombre2
        self.apellido2 = apellido2
        
def saludo(request): # primera vista
    
    p1 = Persona("Jorge", "Robles")
    
    nombre = "Jogico"
    nombre_mujer = "Pily"
    temas2 = ["Libro1", "Libro2", "Libro3", "Libro4", "Libro5", "libro6"]
    
    fecha_actual = datetime.datetime.now()
    
    doc_externo = open("C:/Users/Jr/Documents/ProjectosDjango/proyecto1/proyecto1/Plantillas/miplantilla.html")
   
    plt=Template(doc_externo.read())
   
    doc_externo.close()
   
    ctx= Context({"nombre_persona":nombre, "nombre_mujer":nombre_mujer, "fecha_actual":fecha_actual, "nombre_persona2":p1.nombre2, "apellido_persona2":p1.apellido2, "temas":["plantillas", "modelos", "formularios", "vistas", "Despliegues"], "temas2":temas2})
   
    documento = plt.render(ctx)  
    
    return HttpResponse(documento)

def despedida(request): # segunda Vista por
    
    return HttpResponse('Hasta luego alumnos')

def horafecha(request): # tercera Vista por
    
    fcha_actual = datetime.datetime.now()
    
    documento = """<html>
    <body>
    <h1>
    Hora y fecha Actual del Sistema %s
    </h1>
    </body>
    </html>""" % (fcha_actual)
        
    return HttpResponse(documento)

def calculaedad(request, edad, anio):
    
    # edadactual = 51
    periodo = anio-2022
    edadfutura = edad + periodo
    documento = """<html>
    <body>
    <h1>
    En el año %s Jorge Tendra %s años 
    </h1>
    </body>
    </html>""" %(anio, edadfutura)
            
    return HttpResponse(documento)
    
        
