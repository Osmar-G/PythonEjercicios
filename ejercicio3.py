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


# Quíntupla del Ejercicio 3 (modelado con equivalencia de estados mod 6)
Q = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5'}
sigma = {'a'}
q0 = 'q0'
F = {'q0', 'q2', 'q3', 'q4'}

delta = {
    ('q0', 'a'): 'q1',
    ('q1', 'a'): 'q2',
    ('q2', 'a'): 'q3',
    ('q3', 'a'): 'q4',
    ('q4', 'a'): 'q5',
    ('q5', 'a'): 'q0'
}

afd = AFD(Q, sigma, delta, q0, F)

# Casos de prueba
cadenas = ['', 'aa', 'aaa', 'aaaa', 'aaaaaa', 'a', 'aaaaa', 'aaaaaaa']
print("-- Pruebas Ejercicio 3 --")
for cadena in cadenas:
    resultado = afd.procesar(cadena)
    veredicto = "aceptada" if resultado else "rechazada"
    cadena_mostrar = "ε" if cadena == "" else cadena
    print(f"La cadena '{cadena_mostrar}' es {veredicto}.")