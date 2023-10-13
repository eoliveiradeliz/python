import sympy as sp

# Definir a variável simbólica
x = sp.symbols('x')

# Criar a equação
equacao = 2*x + 3 - 7

# Resolver a equação
solucao = sp.solve(equacao, x)

# Exibir as soluções
print(solucao)
