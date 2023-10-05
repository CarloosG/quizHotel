


class Huesped:
    def __init__(self,nombre,cedula,llegada,room):
    
     self.nombre= nombre
     self.cc = cedula
     self.llegada = llegada
     self.siguiente = None
     self.rm = room
     
class LibroEntrada:
      def __init__(self,cabeza = None):
        self.cabeza = cabeza
        self.habitaciones_disponibles = 10
        self.habitaciones_ocupadas = 0 

    
    
      def insertarInicio(self, nombre, cedula, llegada,room):
              if self.habitaciones_disponibles > 0:
                Huesped_nuevo = Huesped(nombre,cedula,llegada,room)
                Huesped.siguiente = self.cabeza
                self.cabeza = Huesped_nuevo
                self.habitaciones_disponibles -= 1
                self.habitaciones_ocupadas +=1
              else:
                print("No se puede agregar el huesped,no hay habitaciones disponibles")



    
    
      def insertarFinal(self, nombre,cedula,llegada,room):
          if self.habitaciones_disponibles > 0:
            Huesped_nuevo = Huesped(nombre,cedula,llegada,room)
            if not self.cabeza:
              self.cabeza = Huesped_nuevo
              return
            Huesped_recorre = self.cabeza
            while Huesped_recorre.siguiente:
              Huesped_recorre = Huesped_recorre.siguiente
            Huesped_recorre.siguiente = Huesped_nuevo
            self.habitaciones_disponibles -= 1
            self.habitaciones_ocupadas +=1
          else:
              print("No se puede agregar el huesped,no hay habitaciones disponibles")
             


      def habitacionesDisponibles(self):
         print("Hay " + str(self.habitaciones_disponibles) + " habitaciones disponibles")
         if self.habitaciones_disponibles <= 0:
            print("No hay habitaciones disponibles")
      def habitacionesOcupados(self):
         print("Hay " + str(self.habitaciones_ocupadas) + " habitaciones ocupadas")


    
      def imprimir(self):
        
        Huesped_recorre = self.cabeza
        while (Huesped_recorre):
          print("Nombre del huesped: " + Huesped_recorre.nombre +"  " + "Cedula: " +str(Huesped_recorre.cc) +"  " + "Llegada: " + str(Huesped_recorre.llegada )+"  " + "Habitacion: " + str(Huesped_recorre.rm))
          
          Huesped_recorre = Huesped_recorre.siguiente
    
      def eliminarElemento(self, x):
            if not self.cabeza:
             return
            if self.cabeza.rm == x:
              self.cabeza = self.cabeza.siguiente
              return
            Huesped_recorre = self.cabeza
            while Huesped_recorre.siguiente:
             if Huesped_recorre.siguiente.rm == x:
                Huesped_recorre.siguiente = Huesped_recorre.siguiente.siguiente
                return
            Huesped_recorre = Huesped_recorre.siguiente
    
      def buscarHuesped(self, nombre):
          Huesped_actual = self.cabeza
          while Huesped_actual:
              if Huesped_actual.nombre == nombre:
                print("Nombre del huesped: " + Huesped_actual.nombre +"  " +"Cedula: " + str(Huesped_actual.cc) +"  " +"Llegada: "+ str(Huesped_actual.llegada )+"  " + "Habitacion: "+ str(Huesped_actual.rm))
              Huesped_actual = Huesped_actual.siguiente
          return False
      def buscarCedula(self, cedula):
          Huesped_actual = self.cabeza
          while Huesped_actual:
              if Huesped_actual.cc == cedula:
                print("Nombre del huesped: " + Huesped_actual.nombre +"  " +"Cedula: " + str(Huesped_actual.cc) +"  " +"Llegada: "+ str(Huesped_actual.llegada )+"  " + "Habitacion: "+ str(Huesped_actual.rm))
              Huesped_actual = Huesped_actual.siguiente
          return False
      def buscarLlegada(self, llegada):
          Huesped_actual = self.cabeza
          while Huesped_actual:
              if Huesped_actual.llegada == llegada:
                print("Nombre del huesped: " + Huesped_actual.nombre +"  " +"Cedula: " + str(Huesped_actual.cc) +"  " +"Llegada: "+ str(Huesped_actual.llegada )+"  " + "Habitacion: "+ str(Huesped_actual.rm))
              Huesped_actual = Huesped_actual.siguiente
          return False    


libro = LibroEntrada()


libro.insertarInicio("Juhn",12,1,301)
libro.insertarFinal("Roman",112,2,321)
libro.insertarFinal("carlos",1223,3,3333)
libro.insertarFinal("carlos",1223,3,3333)
libro.insertarFinal("carlos",1223,3,3333)
libro.insertarFinal("carlos",1223,3,3333)
libro.insertarFinal("carlos",1223,3,3333)
libro.insertarFinal("carlos",1223,3,3333)
libro.insertarFinal("carlos",1223,3,3333)
libro.insertarFinal("carlos",1223,3,3333)
libro.insertarFinal("carlos",1223,3,3333)
libro.habitacionesOcupados()
# libro.imprimir()
# libro.buscarHuesped("karol")
# libro.buscarHuesped("Juhn")
# libro.buscarCedula(1223)
# libro.buscarLlegada(2)



