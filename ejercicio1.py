class AFD:
    def __init__(self, Q, sigma, delta, q0, F):
        self.Q = Q            # Conjunto de estados
        self.sigma = sigma    # Alfabeto (símbolos permitidos)
        self.delta = delta    # Función de transición: {(estado, simbolo): nuevo_estado}
        self.q0 = q0          # Estado inicial
        self.F = F            # Conjunto de estados de aceptación (finales)

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


# Quíntupla del Ejercicio 1
Q = {'q0', 'q1', 'q2', 'q3', 'q4'}
sigma = {'a', 'b'}
q0 = 'q0'
F = {'q2', 'q4'}

delta = {
    ('q0', 'a'): 'q1', ('q0', 'b'): 'q3',
    ('q1', 'a'): 'q2', ('q1', 'b'): 'q3',
    ('q2', 'a'): 'q1', ('q2', 'b'): 'q3',
    ('q3', 'a'): 'q1', ('q3', 'b'): 'q4',
    ('q4', 'a'): 'q1', ('q4', 'b'): 'q3'
}

afd = AFD(Q, sigma, delta, q0, F)

# Casos de prueba
cadenas = ['aa', 'bb', 'aaaa', 'bbaa', 'abba', 'baab', 'a', 'b', 'ab', 'ba']
print("-- Pruebas Ejercicio 1 --")
for cadena in cadenas:
    resultado = afd.procesar(cadena)
    veredicto = "aceptada" if resultado else "rechazada"
    cadena_mostrar = "ε" if cadena == "" else cadena
    print(f"La cadena '{cadena_mostrar}' es {veredicto}.")