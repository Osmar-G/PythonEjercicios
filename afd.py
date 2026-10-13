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
            # Si el símbolo no pertenece al alfabeto, la cadena se rechaza
            if simbolo not in self.sigma:
                return False
                
            # Si existe una transición válida, cambiamos de estado
            if (estado_actual, simbolo) in self.delta:
                estado_actual = self.delta[(estado_actual, simbolo)]
            else:
                # Si no hay transición definida, la cadena se rechaza
                return False
                
        # La cadena es aceptada si el estado final pertenece a F
        return estado_actual in self.F

# --- ESTO DEBE IR FUERA DE LA CLASE (SIN INDENTACIÓN) ---

# AFD que solo acepta la palabra "01"
# 1. Quíntupla del AFD
Q = {'q0', 'q1', 'q2', 'q_trampa'}
sigma = {'0', '1'}
delta = {
    ('q0', '0'): 'q1',
    ('q0', '1'): 'q_trampa',
    ('q1', '0'): 'q_trampa',
    ('q1', '1'): 'q2',
    ('q2', '1'): 'q_trampa',
    ('q2', '0'): 'q_trampa',
    ('q_trampa', '0'): 'q_trampa',
    ('q_trampa', '1'): 'q_trampa'
}
q0 = 'q0'  # Estado Inicial
F = {'q2'}  # Estado Final de Aceptación

# Construcción del AFD
mi_afd = AFD(Q, sigma, delta, q0, F)

# Casos de prueba
cadenas = ['01', '0', '1', '010', '011', '001', '101', '0101']
print("--Prueba--")
for cadena in cadenas:
    resultado = mi_afd.procesar(cadena)
    veredicto = "aceptada" if resultado else "rechazada"
    print(f"La cadena '{cadena}' es {veredicto}.")

            