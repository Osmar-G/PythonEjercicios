class Nodo:
    def__init__(self,nombre ,edad, sig=None):
        self.nombre = nombre
        self.edad = edad
        self.sig = sig
class pilaE:
    def__init__(self):
        self.tope = None
        self._largo=0
    def esta_vacia(self):
        return self.tope is None
    def push(self,nombre, edad):
        self.tope = Nodo(nombre , edad, self.tope)
        self._largo +=1
    def pop(self):
        if self.esta_vacia():
            return None
        nodo_eliminado = self.tope
        self.tope = self.tope.sig
        self._largo -=1
        return (nodo_eliminado.nombre, nodo_eliminado.edad)
    def peek(self):
        if self.esta_vacia():
            #return None
            raise IndexError("La pila esta vacia)
        return (self.tope.nombre, self.tope.edad)
    def limpiar(self):
        self.tope = None
        self._largo = 0
    def imprimir(self):
        actual = self.tope
        elementos = []
        while actual:
            elementos.append(f"({actual.nombre}, {actual.edad})")
            actual = actual.sig
        print("Pila ->","->".join(elementos))
