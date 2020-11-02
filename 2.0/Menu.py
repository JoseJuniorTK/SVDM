import os
import readline
import Nucleo
import subprocess
import shlex
readline.parse_and_bind("tab: complete")

a = []
b = []

print('Projeto Visualização de Dados 0.2')
print('')
print('')
# Menu simples
print('              __Menu__               ')
print('')
print('1) Classificação e plotagem de gráfico')
print('2) Somente plotagem de gráfico')
escolha = input('Digite sua escolha: ')
if escolha == "1":
    print('Escolha o aplicativo de classificação: ')
    print('1) Kraken')
    print('-------------------------------')
    escolha2 = input('')
    if escolha2 == "1":
        fileinputclass = input("Insira o arquivo a ser classificado: ")
        krakenthreads = input("Insira quantos nucleos de processamento a serem utilizados: ")
        # Parametros de utilização do kraken
        if fileinputclass.endswith('.fasta.gz'):
            print('Parametros válidos, iniciando KRAKEN, por favor aguarde...')
            programa = './kraken'
            arg1 = '--db'
            arg2 = 'minikraken_20171013_4GB/'
            arg3 = str(fileinputclass)
            arg4 = '--preload'
            arg5 = '--threads'
            arg6 = str(krakenthreads)
            arg7 = '--output'
            arg8 = 'tmp.txt'
            subprocess.call([programa, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8], shell=False)
            subprocess.run("./kraken-report --db minikraken_20171013_4GB/ tmp.txt > tmp2", shell=True)
            escolha3 = input('Deseja fazer a plotagem de gráfico?')
            if escolha3 == 's':
                fileinput = "tmp2"
                Nucleo.Main(a, b, fileinput)
            else:
                print('Processo finalizado..')
    else:
        print('Parametros Invalidos')

elif escolha == "2":
    fileinput = input("Input file: ")
    Nucleo.Main(a, b, fileinput)
else:
    print('Escolha invalida')
print("Finalizado")
