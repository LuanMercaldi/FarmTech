#Calcula a area
def calcular_area_triangulo(base, altura):
    area = (base * altura) / 2
    return area

# Cria uma lista pra guardar as informações
lista_areas = []
lista_culturas = []
lista_insumos = []
lista_qtd_insumos = []

#Constantes
hectare = 10000
zinco_hectare = 2
fostato_metro = 0.5

#Menu de interação
while True:
    print('\n--- FarmTech Solutions ---')
    print('1. Inserir Novo Plantio')
    print('2. Relátorio de Áreas Cadastradas')
    print('3. Excluir Plantio')
    print('0. Sair')

    #Pede pro usuário escolher a cultura
    opcao = input('Escolha uma opção: ')
    if opcao == '1':
        print('\n--- Cadastro de Novo Plantio ---')
        print('Qual a cultura? (1. Café | 2. Soja)')
        escolha = input('Escolha o número: ')
        if escolha == '1':
            cultura = 'Café'
            produto = 'Fosfato'
            unidade = 'Litros'

            # Pede pro usuário inserir alguns dados
            base = float(input('Digite a base: '))
            altura = float(input('Digite a altura: '))

            # Resultado do calculo da area e adição na lista
            area_triangulo = calcular_area_triangulo(base, altura)
            lista_areas.append(area_triangulo)
            lista_culturas.append(cultura)

            # calculo insumos
            produto_necessario = area_triangulo * fostato_metro
            lista_insumos.append(produto)
            lista_qtd_insumos.append(produto_necessario)

            # Mostra o resultado
            print(f'Cultura {cultura} cadastrada com area {area_triangulo:.2f} m².')
            pass

        elif escolha == '2':
            cultura = 'Soja'
            produto = 'Zinco'
            unidade = 'Kilos'

            # Pede pro usuário inserir alguns dados
            base = float(input('Digite a base: '))
            altura = float(input('Digite a altura: '))

            # Resultado do calculo da area e adição na lista
            area_triangulo = calcular_area_triangulo(base, altura)
            lista_areas.append(area_triangulo)
            lista_culturas.append(cultura)

            #calculo insumos
            produto_necessario = (area_triangulo / hectare) * 2
            lista_insumos.append(produto)
            lista_qtd_insumos.append(produto_necessario)

            # Mostra o resultado
            print(f'Cultura {cultura} cadastrada com area {area_triangulo:.2f} m².')
            pass

        else:
            print('Opção Invalida! Usando INDEFINIDO.')
            cultura = 'INDEFINIDO'

    elif opcao == '2':
        print('\n--- Relátorio de Áreas Cadastradas ---')

        # O range(len(...)) cria uma lista de números (0, 1, 2...) do tamanho da lista
        for i in range(len(lista_culturas)):
            cultura = lista_culturas[i]
            area_triangulo = lista_areas[i]

            # CRIANDO VARIÁVEIS NOVAS (produto e quantidade) para não destruir as listas:
            insumos = lista_insumos[i]
            qtd_insumos = lista_qtd_insumos[i]

            # Imprimindo de forma genérica para funcionar com qualquer cultura
            print(f'{i + 1}. Cultura: {cultura} | Área: {area_triangulo:.2f} m²')
            print(f'   Insumo necessário: {qtd_insumos:.2f} {unidade} de {insumos}')
        print(f'Total da Fazenda: {sum(lista_areas):.2f} m² ')

    # Excluir Informações
    elif opcao == '3':
        print('\n--- Excluindo Plantio ---')
        numero_deletar = int(input('Qual o plantio que você deseja deletar?: '))
        indice_deletar = numero_deletar - 1

        lista_areas.pop(indice_deletar)
        lista_culturas.pop(indice_deletar)
        lista_insumos.pop(indice_deletar)
        lista_qtd_insumos.pop(indice_deletar)

        print('Plantio Deletado com Sucesso!')

        pass

    elif opcao == '0':
        print('Saindo do sistema')
        break

    else:
        print('Opção Invalida')
