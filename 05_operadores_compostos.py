# 05_operadores_compostos.py
# Este arquivo demonstra como o Python resolve contas à direita primeiro

print("--- Teste 1: Divisao Composta ---")
a = 6
b = 3
# Regra: Resolve (2 * b) primeiro, depois divide a por isso
a /= 2 * b 
print("Resultado de a /= 2 * b e:", a) # Esperado: 1.0

print("\n--- Teste 2: Multiplicacao Composta ---")
x = 10
y = 2
# Regra: Resolve (3 + y) primeiro, depois multiplica x por isso
x *= 3 + y
print("Resultado de x *= 3 + y e:", x) # Esperado: 50

print("\n--- Teste 3: O jeito 'preguicoso' (Acumulador) ---")
pontos = 100
pontos += 10 # Mesma coisa que pontos = pontos + 10
print("Meus pontos subiram para:", pontos)
