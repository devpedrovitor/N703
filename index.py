# Função lambda:
quadrado = lambda x: x ** 2

# List comprehension
lista_quadrados = [quadrado(x) for x in range(1, 11)]

# Closure:
def contador():
    contagem = 0
    def incrementar():
        nonlocal contagem
        contagem += 1
        return contagem
    return incrementar

# Função de alta ordem:
def aplicar_funcao(funcao, lista):
    return [funcao(x) for x in lista]

# Uso da função de alta ordem
resultados = aplicar_funcao(quadrado, lista_quadrados)

# Exibindo os resultados
print("Lista de quadrados:", lista_quadrados)
print("Resultados após aplicar a função:", resultados)

# Testando a closure
contador_iniciar = contador()
print("Contador:", contador_iniciar()) 
print("Contador:", contador_iniciar())  
print("Contador:", contador_iniciar())  