# Simulando o acúmulo de algo (como acessos ou erros)

acessos = 0
print("Início do dia, acessos:", acessos)

acessos = acessos + 1
acessos = acessos + 1
print("Após dois acessos:", acessos)

# O jeito "preguiçoso" (atribuição composta)
acessos += 5 
print("Chegaram mais 5 pessoas. Total:", acessos)
