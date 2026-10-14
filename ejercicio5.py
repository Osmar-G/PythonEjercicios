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


# Quíntupla del Ejercicio 5
Q = {'A', 'B', 'C', 'D', 'E'}
sigma = {'0', '1'}
q0 = 'C'
F = {'C', 'E'}

delta = {
    ('A', '0'): 'B', ('A', '1'): 'B',
    ('B', '0'): 'C', ('B', '1'): 'E',
    ('C', '0'): 'D', ('C', '1'): 'A',
    ('D', '0'): 'B', ('D', '1'): 'E',
    ('E', '0'): 'D', ('E', '1'): 'D'
}

afd = AFD(Q, sigma, delta, q0, F)

# Casos de prueba
cadenas = ['', '0', '1', '10', '11', '00', '01', '0100', '10101', '101']
print("-- Pruebas Ejercicio 5 --")
for cadena in cadenas:
    resultado = afd.procesar(cadena)
    veredicto = "aceptada" if resultado else "rechazada"
    cadena_mostrar = "ε" if cadena == "" else cadena
    print(f"La cadena '{cadena_mostrar}' es {veredicto}.")