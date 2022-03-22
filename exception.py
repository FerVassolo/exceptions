class MiExcepcion(Exception):
   def __init__(self, mensaje, informacion):
       self.__mensaje = mensaje
       self.__informacion = informacion


   def getMensaje(self):
       return self.__mensaje

   def getInformacion(self):
       return self.__informacion







try:
   raise MiExcepcion("Mensaje", "Informacion")
except MiExcepcion as e:
   print(e.getMensaje())
   print(e.getInformacion())

