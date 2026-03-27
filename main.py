#Calcula a area
def calcular_area_triangulo(base, altura):
    area = (base * altura) / 2
    return area

# Cria uma lista pra guardar as informações
lista_areas = []
lista_culturas = []


#Menu de interação
while True:
    print('\n--- FarmTech Solutions ---')
    print('1. Inserir Novo Plantio')
    print('2. Relátorio de Áreas Cadastradas')
    print('0. Sair')

    #Pede pro usuário escolher a cultura
    opcao = input('Escolha uma opção: ')
    if opcao == '1':
        print('\n--- Cadastro de Novo Plantio ---')
        print('Qual a cultura? (1. Café | 2. Soja')
        escolha = input('Escolha o número: ')
        if escolha == '1':
            cultura = 'Café'
        elif escolha == '2':
            cultura = 'Soja'
        else:
            print('Opção Invalida! Usando INDEFINIDO.')
            cultura = 'INDEFINIDO'

        # Pede pro usuário inserir alguns dados
        base = float(input('Digite a base: '))
        altura = float(input('Digite a altura: '))

        # Resultado do calculo da area e adição na lista
        area_triangulo = calcular_area_triangulo(base, altura)
        lista_areas.append(area_triangulo)
        lista_culturas.append(cultura)

        # Mostra o resultado
        print(f'Cultura {cultura} cadastrada com area {area_triangulo:.2f} m².')
        pass
    elif opcao == '2':
        print('\n--- Relátorio de Áreas Cadastradas ---')
        # O range(len(...)) cria uma lista de números (0, 1, 2...) do tamanho da lista
        for i in range(len(lista_culturas)):
            cultura = lista_culturas[i]
            area_triangulo = lista_areas[i]
            print(f'{i + 1}. Cultura: {cultura} | Área: {area_triangulo} m²')
            print(f'Total da Fazenda: {sum(lista_areas):.2f} m² ')
    elif opcao == '0':
        print('Saindo do sistema')
        break
    else:
        print('Opção Invalida')
