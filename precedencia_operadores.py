# --- DESAFIO DE EXPRESSÃO COMPLEXA ---
# Regra: De dentro para fora, seguindo os parênteses.
# ((5 * ((25 % 13) + 100) / (2 * 13)) // 2)

# 1. 25 % 13 = 12
# 2. 12 + 100 = 112
# 3. 5 * 112 = 560
# 4. 2 * 13 = 26
# 5. 560 / 26 = 21.538...
# 6. 21.538... // 2 = 10.0
print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)
