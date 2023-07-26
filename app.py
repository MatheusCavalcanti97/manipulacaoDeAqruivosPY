import datetime
def minhas_linhas():
    linhas = '-'*150
    return linhas

def verificacao_de_duplicidade_cpfs_ou_existencia(cpf_chefe_familiar:str, dicionario_familias: dict) -> bool:
    if cpf_chefe_familiar in dicionario_familias:
        return True
    else:
        return False
    
def organizar_txt_pra_leitura(var_leitura: list) -> list:
    var_valor = ''
    lista_aux = []
    for valor in range(len(var_leitura)):
        var = ''
        if valor <= len(var_leitura):
            var = str(var_leitura[valor]).replace(',', '').split()
            lista_aux.append(var)
        for x in range(len(lista_aux)):
            lista_aux[x][0] = str(lista_aux[x][0])
            lista_aux[x][1] = int(lista_aux[x][1])
            lista_aux[x][2] = float(lista_aux[x][2])
            lista_aux[x][3] = float(lista_aux[x][3])
    return lista_aux

def retorna_info_pelo_cpf(cpf_chefe_familia: str):
    listao = []
    lista = organizar_txt_pra_leitura(var_leitura)
    var = ''
    for x in range(len(lista)):
        if cpf_chefe_familia == lista[x][0]:
            var = f'Renda Total da Família: {lista[x][2]}\nQuantidade de Membros da Família: {lista[x][1]}\nRenda Média da Família: {lista[x][3]}'
            return var
            break
        else:
            var = 'CPF NÃO ENCONTRADO.'
    return var

def calcular_renda_media_salario_cidade():
    with open('my_app.txt', 'r', encoding='UTF-8') as archive:
        var_leitura = archive.readlines()
        quant_familias = int(len(organizar_txt_pra_leitura(var_leitura)))
        soma_rendas_totais = float(0)
        media_salarios_familias_cidade = float(0)
        for x in range(len(organizar_txt_pra_leitura(var_leitura))):
            soma_rendas_totais += organizar_txt_pra_leitura(var_leitura)[x][3]
        media_salarios_familias_cidade = soma_rendas_totais / quant_familias
    return media_salarios_familias_cidade

def calcular_numero_medio_individuos_fam():
    total_total_ind = int(0)
    total_familias = 0
    media_individuos_por_familias = int(0)
    with open('my_app.txt', 'r', encoding='UTF-8') as archive:
        var_leitura = archive.readlines()
        total_familias = int(len(organizar_txt_pra_leitura(var_leitura)))
        for x in range(len(organizar_txt_pra_leitura(var_leitura))):
            total_total_ind += organizar_txt_pra_leitura(var_leitura)[x][1]
        media_individuos_por_familias = int(total_total_ind / total_familias)
    return media_individuos_por_familias

def percentual_media_salarial_menor_de_1s():
    cont = int(0)
    media_salario = float(0)
    porcentagem_em_relacao_ao_tot = float(0)
    SALARIO_MINIMO = float(1320)
    flag = True
    with open('my_app.txt', 'r', encoding='UTF-8') as archive:
        var_leitura = archive.readlines()
        for x in range(len(organizar_txt_pra_leitura(var_leitura))):
            media_salario = organizar_txt_pra_leitura(var_leitura)[x][3]
            if media_salario < SALARIO_MINIMO:
                cont += 1
        porcentagem_em_relacao_ao_tot = (cont * 100.0) / len(organizar_txt_pra_leitura(var_leitura))
    return porcentagem_em_relacao_ao_tot

def quant_familias_renda_media_maior_de_10s():
    cont = int(0)
    media_salario = float(0)
    porcentagem_em_relacao_ao_tot = float(0)
    SALARIO_MINIMO = float(1320)
    flag = True
    with open('my_app.txt', 'r', encoding='UTF-8') as archive:
        var_leitura = archive.readlines()
        for x in range(len(organizar_txt_pra_leitura(var_leitura))):
            media_salario = organizar_txt_pra_leitura(var_leitura)[x][3]
            if media_salario > (10 *SALARIO_MINIMO):
                cont += 1
    return cont

def criando_arq_txt_backup():
    with open('backup.txt', 'a', encoding='UTF-8') as archive:
        leitura_backup = archive.write('0\n')

def criando_arq_version__txt_backup():
    with open('version_backup.txt', 'a', encoding='UTF-8') as archive:
        leitura_backup = archive.write('')

def incrementa_versao_backup():
    with open('version_backup.txt', 'r', encoding='UTF-8') as archive:
        b = archive.readlines()
        
    with open('version_backup.txt', 'a', encoding='UTF-8') as archive:
            tam = int(len(b))
            archive.write(f'{tam}')
            
def criacao_backup(var_leitura: list):
    quant_linhas = 0
    data_e_hora = datetime.datetime.now()
    data = data_e_hora.strftime('%d/%m/%Y')
    hora = data_e_hora.strftime('%H:%M')
    
    with open('backup.txt', 'r', encoding='UTF-8') as archive:
        b = archive.readlines()
        quant_linhas = len(b)

    with open('version_backup.txt', 'r', encoding='UTF-8') as archive:
        vb = archive.read()
        tam = len(vb)
        var = f'{data} {hora}hs {quant_linhas} v{tam}'

    with open('backup.txt', 'w', encoding='UTF-8') as archive:
         archive.write(f'{var}\n')
         for i in var_leitura:
             archive.write(f'{i}')
    return var
def add_arq_dados(dicionario_familias):
    with open('my_app.txt', 'a', encoding='UTF-8') as archive:
        var = ''
        for chave in dicionario_familias.keys():
            var = f'{chave},{dicionario_familias[chave]}'
            var = var.replace('[','').replace(']','').replace(',', ' ')
        archive.write('{}\n'.format(var))
def letraC():
    with open('my_app.txt', 'r', encoding='UTF-8') as archive:
        var_leitura = archive.readlines()
        var = f'Todos CPF"s Cadastrados no Sistem\n'
        cont = 0
        for x in range(len(organizar_txt_pra_leitura(var_leitura))):
            cont +=1
            if cont <= len(organizar_txt_pra_leitura(var_leitura))-1:
                var += f'{cont} - {organizar_txt_pra_leitura(var_leitura)[x][0]}\n'
            if cont == len(organizar_txt_pra_leitura(var_leitura)):
                var += f'{cont} - {organizar_txt_pra_leitura(var_leitura)[x][0]}\n'
    return var

def letraD():
    with open('my_app.txt', 'r', encoding='UTF-8') as archive:
        var_leitura = archive.readlines()
        var = f'|    Renda Total R$  |    Número de Indíviduos |    Renda Média R$ |\n'
        for x in range(len(organizar_txt_pra_leitura(var_leitura))):
            var += f'\t{organizar_txt_pra_leitura(var_leitura)[x][2]}\t\t'
            var += f'\t   {organizar_txt_pra_leitura(var_leitura)[x][1]}\t\t'
            var += f'\t {organizar_txt_pra_leitura(var_leitura)[x][3]}\n'
    return var

def letraE():
    mostra_info = ''
    with open('my_app.txt', 'r', encoding='UTF-8') as archive:
        mostra_info = f'''Media Salarial das Famílias da Cidade: {calcular_renda_media_salario_cidade()}.
        \nNúmero Médio de Indivíduos por Famílias da Cidade: {calcular_numero_medio_individuos_fam()}.
        \nPercentual de Famílias que têm Renda média Salarial Menor do que 1 Salário Mínimo (R$1.320,00): {percentual_media_salarial_menor_de_1s():.2f}%.
        \nQuantidade de Famílias que têm Renda média Salarial Maior do que 10 Salário Mínimo (R$13.200,00): {quant_familias_renda_media_maior_de_10s()} Família(s).'''
    return mostra_info
#----------------------------
flag_menu = True
flag_menu_do_menu = True
var_menu = ''
menu_do_menu = ''
dicionario_familias = {}
#----------------------------
cpf_chefe_familia = str('')
quantidade_membros_familia = int()
renda_por_ind = float(0)
renda_total_familia = float(0)
renda_media_familia = float(0)
lista_auxiliar = []
var = str('')
cont = int(0)
#----------------------------



print(minhas_linhas())
while flag_menu != False:
    
    var_menu = str(input('''Escolha Uma das Opções a Seguir.\n
A. Inserção de dados das Familias (CPF, QUANTIDADE DE MEMBROS, RENDA POR INDIVIDUO, RENDA TOTAL DA FAMILIA, RENDA MEDIA FALILIAR).
B. Buscar os Dados dos Familiares.
C. Listagem de CPF's Cadastrados.
D. Listagem dos Dados das Famílias.
E. Listagem dos Dados Consolidados.
F. Criação de Backup de Redundância de Dados.
S. Sair.\n''' + minhas_linhas() + '\nOpção Escolhida-> ')).upper()

    match var_menu:

        case 'A':
            cont = 0
            renda_total = 0
            print(minhas_linhas())                   
            cpf_chefe_familia = str(input('Informe o CPF do Chefe da Familia: ')).replace('.','').replace(',','').replace('-','').replace('',' ').split()
            if len(cpf_chefe_familia)== 11:
                cpf_chefe_familia = ''.join(cpf_chefe_familia)
                if verificacao_de_duplicidade_cpfs_ou_existencia(cpf_chefe_familia, dicionario_familias) == True:
                    print(minhas_linhas())
                    print('CPF já inserido.\nExecute a próxima ação.') 
                else:
                    #começando a modificar daqui:
                    print(minhas_linhas())
                    dicionario_familias[cpf_chefe_familia] = [0,0,0]
                    quantidade_membros_familia = int(input('Informe quantos membros têm a sua familia (Obs: Você deve estar incluído): '))
                    dicionario_familias[cpf_chefe_familia][0] = quantidade_membros_familia
                                            
                    if quantidade_membros_familia >= 1:

                        print(minhas_linhas())
                        for x in range(quantidade_membros_familia):
                            cont +=1
                            renda_total += float(input(f'Informe os rendimentos da {cont}º Pessoa da Familia: '))
                        dicionario_familias[cpf_chefe_familia][1] = renda_total
                        dicionario_familias[cpf_chefe_familia][2] = renda_total / dicionario_familias[cpf_chefe_familia][0]
                        print(minhas_linhas() + '\n\n') 
                        for chave in dicionario_familias:
                            print('Chefe da Familia: {} -- Info: {}'.format(chave,dicionario_familias[chave]))           
                        add_arq_dados(dicionario_familias)
                        print(minhas_linhas())
                        print('Dados Inseridos com Sucesso.')
                        print(minhas_linhas() + '\n\n') 
                    else:
                        print(minhas_linhas())
                        print('A quantidade de membros deverá ser no mínimo 1. ')
                        print(minhas_linhas() + '\n\n') 
            else:
                print(minhas_linhas())
                print('Informe um CPF Válido.')
                print(minhas_linhas() + '\n\n')     
        case 'B':
            with open('my_app.txt', 'r', encoding='UTF-8') as archive:
                print(minhas_linhas())
                var_leitura = archive.readlines()
                cpf_chefe_familia = str(input('Informe o CPF do Chefe da Familia: ')).replace('.','').replace(',','').replace('-','').replace(' ','')
                print(minhas_linhas())
                if len(cpf_chefe_familia)== 11:
                    cpf_chefe_familia = ''.join(cpf_chefe_familia)   
                    print(retorna_info_pelo_cpf(cpf_chefe_familia))
                else:
                    print(minhas_linhas())
                    print('Informe um CPF Válido.')
                print(minhas_linhas() + '\n\n') 
        case 'C':
            print(minhas_linhas())
            print(letraC().strip())
            print(minhas_linhas() + '\n\n')                                         
        case 'D':
                print(minhas_linhas())
                print(letraD().strip())
                print(minhas_linhas() + '\n\n') 
        case 'E':
            print(minhas_linhas())
            print(letraE())
            print(minhas_linhas() + '\n\n') 
        case 'F':
            with open('my_app.txt', 'r', encoding='UTF-8') as archive:
                var_leitura = archive.readlines()
                criando_arq_version__txt_backup()
                incrementa_versao_backup()
                criando_arq_txt_backup()
                print(minhas_linhas())
                print('Versão do Backup: ', criacao_backup(var_leitura))
                print(minhas_linhas() + '\n\n') 
        case 'S':
            flag_menu = False
        case __:
            print(minhas_linhas())
            print('Informe uma Opção Correta.')
            print(minhas_linhas() + '\n\n')         