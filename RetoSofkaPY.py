# encoding: utf-8
#format %
from distutils.command.clean import clean
from re import S, T
import random

#Creacion del banco de preguntas y respuestas
banco_preguntas = [["Cuanto es 2 mas 2 1) 3 2) 4 3) 6 4) 2","Cuanto es 3 mas 4 1) 4 2) 5 3) 7 4) 1","De que color es el cielo 1) Negro 2) Verde 3) Morado 4) Azul","Que respiramos 1) Fuego 2) Aire 3) Tierra 4) Agua", "De que color es el césped 1) Negro 2) Verde 3) Morado 4) Azul"],["Raiz cuadrada de 9 1) 4 2) 3 3) 6 4) 1", "81 dividido 9 1) 10 2) 13 3) 12 4) 9", "Cual es la formula del oxigeno 1) Ho 2) O2 3) O 4) H2O", "Icono de colombia 1) Goku 2) YaoMing 3) Fraijelon Ernesto Perez 4) Saitama", "De que en su mayoria estan conformadas las nubes 1) Algodon 2) Queso 3) Contaminacion 4) Agua"],["Cuál de estos nombres no aparece en el título de una obra de Shakespeare 1) Hamlet 2) Romeo 3) Macbeth 4) Darren ", "Cuales de estas aplicaciones ofrecen mas o menos el mismo tipo de servicio 1) Snapchat y Grubhub 2) Whatsapp y Shareit 3) Lyft y Uber 4) Tiktok y spotify", "Que planta es el simbolo nacional de Irlanda 1) Rosa 2) Cardo 3) Puerro 4) Trebol", "Cual de estos es un instrumento musical 1) Mandragora 2) Mandolina 3) Mandalay 4) Mandril", "Como se llamaba la banda cuyo lider era Jim Morrison 1) The Windows 2) The cure 3) The Doors 4) Pink Floyd"], ["Si un dia decidieras sembrar semillas de Quercus robur. Que creceria 1) Arbol 2) Flores 3) Verduras 4) Grano", "Los neurologos creen que la corteza prefrontal del cerebro se activa cuando... 1) Tienes un ataque de panico 2) Recuerdas un nombre 3) Entiendes una broma 4) Escuchas musica", "Cuantos mares rodean la peninsula de los Balcanes 1) 3 2) 4 3) 5 4) 6", "Que nombre nunca ha adoptado un papa 1) Valentin 2) Eugenio 3) Gregorio 4) Jorge", "Cual de estas leyes es falsa en Chile 1) Prohibido tocar las campanas para incitar al pueblo a sublevarse 2) Prohibido andar en carruaje donde haya una multitud de gente 3) Prohibido poner plantas con maceteros en tus balcones o ventanas 4) Prohibido montar en burros o mulas estando bajo los efectos del alcohol"],["Cual el fin ultimo de la vida 1) Ser feliz 2) trabajar 3) No lo hay 4) programar", "Tu eres principalmente 1) Energia 2) carne 3) un nombre 4) una profesion", "Cual es el activo mas importante que tienes 1) Dinero 2) Tiempo 3) Amigos 4) Propiedades", "Todos estamos conectados debido a 1) Tuneles de guzano 2) entrelazamiento cuantico 3) no lo estamos 4) Magia", "La realidad y materia que percibes es 1) 10 porciento vacia 2) 13 porciento vacia 3) 99 porciento vacia 4) 30 porciento vacia"]]
banco_respuestas = [[2,3,4,2,2],[2,4,2,3,4],[4,3,4,2,3],[1,3,4,4,4],[1,1,2,2,3]]
historial = []
#Crear la clase de jugador y los atributos que necesitaremos durante la partida
class Jugador:
    def __init__(self,nombre,puntos,ronda,respuesta):
        self.__nombre = nombre
        self.__puntos = puntos
        self.__ronda = ronda
        self.__respuesta = respuesta
    
    def __getnombre(self):
        return self.__nombre
    def __getpuntos(self):
        return self.__puntos
    def __getronda(self):
        return self.__ronda
    def __getrespuesta(self):
        return self.__respuesta


    def __setnombre(self,nombre):
        self.__nombre = nombre
    def __setpuntos(self,puntos):
        self.__puntos = puntos
    def __setronda(self,ronda):
        self.__ronda = ronda
    def __setrespuesta(self,respuesta):
        self.__respuesta = respuesta

    def __delnombre(self):
        del self.__nombre
    def __delpuntos(self):
        del self.__puntos
    def __delronda(self):
        del self.__ronda
    def __delrespuesta(self):
        del self.__respuesta
    
    nombre = property(fget = __getnombre, fset= __setnombre, fdel= __delnombre)
    puntos = property(fget = __getpuntos, fset= __setpuntos, fdel = __delpuntos)
    ronda = property(fget= __getronda, fset= __setronda, fdel= __delronda)
    respuesta = property(fget= __getrespuesta, fset= __setrespuesta, fdel= __delrespuesta)

#Las etapas del juego
class Juego(Jugador):
    
    
    def __init__(self):
        pass
     
    def configurar_juego(self):
        print("se esta configurando el juego..")
        nuevo_jugador.nombre = raw_input("escribe tu nombre -> ")
        nuevo_jugador.puntos = 0
        nuevo_jugador.ronda = 0
        nuevo_jugador.respuesta = 0
    def iniciar_ronda(self):
        print("RONDA NUMERO % s"%nuevo_jugador.ronda)
        print("LEE LA PREGUNTA Y ELIGE SI DESEAS RESPONDERLA O RETIRARTE")
        print("Pregunta:")
    def victoria(self):
        print("Lo lograste!!!!!!! Que epico!!")
        print("% s te llevas a casa la suma de % s"%(nuevo_jugador.nombre,nuevo_jugador.puntos))
        print("Eres genial sigue asi!")
    def finalizar(self):
        print("has perdido % s"%nuevo_jugador.nombre)
        nuevo_jugador.puntos= 0
        print("Esta vez te vas a casa con las manos vacias pero la vida se trata de riesgos! Se trata de divertirse")
    def finalizar_voluntario(self):
        print("% s Saber cuando retirarse es una habilidad que pocos poseen "%nuevo_jugador.nombre)
        print("Te vas a casa con un premio en dolares de % s"%nuevo_jugador.puntos)
        
    def advertencia(self):
        print("% s ADVERENTCIA!"%nuevo_jugador.nombre)
        print("Deseas continuar y arriesgarte o...")
        print("Deseas retirarte con tu premio actual de % s dolares"%nuevo_jugador.puntos)
    

nuevo_jugador = Juego()
nuevo_jugador.configurar_juego()


while nuevo_jugador.ronda <= 5:
    #preparacion de preguntas y respuestas
    numero_aleatorio = random.randint(0, 4)
    preguntas_ronda = banco_preguntas[nuevo_jugador.ronda]
    pregunta_ronda = preguntas_ronda[numero_aleatorio]
    respuestas_ronda = banco_respuestas[nuevo_jugador.ronda]
    #visualizacion de pregunta correspondiente
    nuevo_jugador.iniciar_ronda()
    print(pregunta_ronda)
    #advertencia para que el jugador decida si retirarse con ganancias o seguir
    nuevo_jugador.advertencia()
    vida = int(input("Escribe 1 si deseas continuar, 2 si deseas retirarte -> ")) 
    if vida == 1:
        nuevo_jugador.respuesta = int(input("Exclente! Vamos por mas! Escribe el numero con un parentesis que esta antes de tu respuesta a la pregunta -> "))
        
        #el if de abajo evalua si la respuesta que puso el jugador es la misma que la de la base de datos
        
        if nuevo_jugador.respuesta == respuestas_ronda[numero_aleatorio]:

            print("Muy bien acertaste!")
            nuevo_jugador.ronda +=1
            nuevo_jugador.puntos = nuevo_jugador.puntos + nuevo_jugador.ronda*100
            #una vez lleguemos a la ronda final debe acabar el juego y mostrar las ganancias
            
            if nuevo_jugador.ronda == 5:
                nuevo_jugador.victoria()
                break
    
        else:
            nuevo_jugador.finalizar()
            break
    if vida == 2:
        nuevo_jugador.finalizar_voluntario()
        break
historial.append("el jugador % s se llevo a casa % s dolares "%(nuevo_jugador.nombre, nuevo_jugador.puntos))
#print(historial)
#Hubiera sido divertido con algo mas de tiempo poder hacerlo mas visual, tal vez con la libreria Tkinter 
#No me gusta la parte de verificacion de seguir o retirarse con un 1 o un 2 pues es confuso pero por temas personales solo tuve un dia y medio para realizar el codigo, no logre formular una alternativa mas elegante pero creo que es necesaria
#

    
    
        
