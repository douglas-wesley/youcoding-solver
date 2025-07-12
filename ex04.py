def hash_function(value, qtd_containers):
    return value % qtd_containers

def inserir_valores(tabela, valores_inserir, qtd_containers, tamanho_container):
    for valor in valores_inserir:
        index = hash_function(valor, qtd_containers)
        if len(tabela[index]) < tamanho_container:
            tabela[index].append(valor)

def buscar_valores(tabela, valores_buscar, qtd_containers, tamanho_container):
    resultado_operacoes = ""
    for valor_buscado in valores_buscar:
        index = valor_buscado % qtd_containers
        operacoes = 0
        encontrado = False

        if not tabela[index]:
            operacoes = 1
        else:
            for item in tabela[index]:
                operacoes += 1
                if item == valor_buscado:
                    encontrado = True
                    break

            if not encontrado:
                operacoes = tamanho_container

        resultado_operacoes += f'{str(operacoes)} '

    return resultado_operacoes

def main(entrada):
    qtd_containers = entrada[0]
    tamanho_container = entrada[1]
    qtd_insercoes = entrada[2]

    valores_inserir = entrada[3:3 + qtd_insercoes]
    valores_buscar = entrada[3 + qtd_insercoes:]

    tabela = [[] for _ in range(qtd_containers)]

    inserir_valores(tabela, valores_inserir, qtd_containers, tamanho_container)
    resultado = buscar_valores(tabela, valores_buscar, qtd_containers, tamanho_container)

    return resultado

entrada = [int(i) for i in input().split()]
print(main(entrada))