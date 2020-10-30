import os
import readline
import Nucleo
readline.parse_and_bind("tab: complete")

a = []
b = []

print('Projeto Visualização de Dados 0.1')
print('')
# Parseia os dados do arquivo teste.txt

fileinput = input("Input file: ")
Nucleo.Main(a,b,fileinput)
print("Finalizado")