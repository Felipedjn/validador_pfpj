from validate_docbr import CPF, CNPJ
from colorama import Fore

def validador():
    cpf = CPF()
    cnpj = CNPJ()

    diretorio_erro = './dados_erro.txt'
    diretorio_saida = './saida.txt'
    diretorio_dados = './dados.txt'

    #REMOVE OS REPETIDOS
    with open(f'{diretorio_dados}') as dados:
        linhas = dados.readlines()
        linhas = [x.strip('\n') for x in linhas]
        def remove_repetidos(lista):
            l = []
            for i in lista:
                if i not in l:
                    l.append(i)
            l.sort()
            return l
        lista = remove_repetidos(linhas)


    with open(diretorio_dados, 'w') as dados:
        dados.write('\n' .join(lista))
        
    #LIMPA ARQUIVO SAÍDA E ERRO
    arquivo = open(diretorio_saida, 'w+')
    with open(diretorio_saida, 'r+') as f:
        f.truncate(0)
    with open(diretorio_erro, 'r+') as f:
        f.truncate(0)

    #SUBSTITUI ASPAS E \N POR NADA
    with open(diretorio_dados) as f:
        newText=f.read().replace('""\n', '')
    with open(diretorio_dados, 'w') as f:
        f.write(newText)

    #ARQUIVO DADOS
    with open(diretorio_dados) as dados:
        content = dados.readlines()
        content = [x.strip('\n') for x in content]
        print(content)

    #VALIDADOR
    for line in content:
        validadorcpf = cpf.validate(line)
        validadorcnpj = cnpj.validate(line)
        #VALIDADOR
        if len(line)<=11:

            #VALIDADOR CPF
            if validadorcpf == False:
                print(Fore.LIGHTRED_EX, 'CPF INVALIDO: ' + line, Fore.WHITE)
                with open(diretorio_erro, 'a') as dados_erro:
                    dados_erro.write(f'{line}\n')
            else:
                with open(diretorio_saida, 'a') as dados_cpf:
                    dados_cpf.write(f'{line}\n')
                    if len(line)==11:
                        print(f'{line};CPF', file=arquivo)

        else:
            #VALIDADOR CNPJ         
            if validadorcnpj == False:
                print(Fore.LIGHTRED_EX, 'CNPJ INVALIDO: ' + line)
                with open(diretorio_erro, 'a') as dados_erro:
                    dados_erro.write(f'{line}\n')
            else:
                with open(diretorio_saida, 'a') as dados_cnpj:
                    dados_cnpj.write(f'{line}\n')
                    if len(line)==14:
                        print(f'{line};CNPJ', file=arquivo)  

validador()
