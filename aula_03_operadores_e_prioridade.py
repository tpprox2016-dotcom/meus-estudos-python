# --- ESTUDO DE PRECEDÊNCIA (Quem manda mais?) ---

# A potência (**) tem prioridade sobre o sinal de negativo (-)
print(-3 ** 2)    # Resultado: -9 (O Python faz 3**2 primeiro)

# Usando parênteses para mudar a prioridade
print((-3) ** 2)  # Resultado: 9 (O Python eleva o número negativo ao quadrado)

# Outro exemplo: Multiplicação vs Soma
print(10 + 2 * 5)   # Resultado: 20 (Faz 2*5 primeiro)
print((10 + 2) * 5) # Resultado: 60 (Faz a soma primeiro por causa dos parênteses)
