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


# Quíntupla del Ejercicio 2 (convertido a AFD completo)
Q = {'q2', 'q3', 'q_trampa'}
sigma = {'a', 'b'}
q0 = 'q2'  # q2 actúa como inicio tras absorber la ε-transición desde q1
F = {'q2'}

delta = {
    ('q2', 'a'): 'q3',
    ('q2', 'b'): 'q_trampa',
    ('q3', 'a'): 'q2',
    ('q3', 'b'): 'q3',
    ('q_trampa', 'a'): 'q_trampa',
    ('q_trampa', 'b'): 'q_trampa'
}

afd = AFD(Q, sigma, delta, q0, F)

# Casos de prueba
cadenas = ['', 'a', 'aa', 'ab', 'aba', 'abb', 'b', 'ba', 'bb', 'bab']
print("-- Pruebas Ejercicio 2 --")
for cadena in cadenas:
    resultado = afd.procesar(cadena)
    veredicto = "aceptada" if resultado else "rechazada"
    cadena_mostrar = "ε" if cadena == "" else cadena
    print(f"La cadena '{cadena_mostrar}' es {veredicto}.")