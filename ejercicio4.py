class AFD:
    def __init__(self, Q, sigma, delta, q0, F):
        self.Q = Q
        self.sigma = sigma
        self.delta = delta
        self.q0 = q0
        self.F = F

    def procesar(self, cadena):
        estado_actual = self.q0
        for simbolo in cadena:
            if simbolo not in self.sigma:
                return False
            if (estado_actual, simbolo) in self.delta:
                estado_actual = self.delta[(estado_actual, simbolo)]
            else:
                return False
        return estado_actual in self.F


# Quíntupla del Ejercicio 4
Q = {'q1', 'q3', 'q4'}
sigma = {'a', 'b'}
q0 = 'q1'
F = {'q4'}

delta = {
    ('q1', 'a'): 'q1',
    ('q1', 'b'): 'q3',
    ('q3', 'a'): 'q1',
    ('q3', 'b'): 'q4',
    ('q4', 'a'): 'q4',
    ('q4', 'b'): 'q4'
}

afd = AFD(Q, sigma, delta, q0, F)

# Casos de prueba
cadenas = ['bb', 'abb', 'bba', 'bbbb', 'aabb', 'a', 'b', 'ab', 'ba', 'aba']
print("-- Pruebas Ejercicio 4 --")
for cadena in cadenas:
    resultado = afd.procesar(cadena)
    veredicto = "aceptada" if resultado else "rechazada"
    cadena_mostrar = "ε" if cadena == "" else cadena
    print(f"La cadena '{cadena_mostrar}' es {veredicto}.")