import os
import re
import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np

a = []
b = []

print('___  ___ _____ _____ ___  _____  _____ _   _ ________  ________ _____ ')
print('|  \/  ||  ___|_   _/ _ \|  __ \|  ___| \ | |  _  |  \/  |_   _/  __ \ ')
print('| .  . || |__   | |/ /_\ \ |  \/| |__ |  \| | | | | .  . | | | | /  \/')
print('| |\/| ||  __|  | ||  _  | | __ |  __|| . ` | | | | |\/| | | | | |    ')
print('| |  | || |___  | || | | | |_\ \| |___| |\  \ \_/ / |  | |_| |_| \__/\ ')
print('\_|  |_/\____/  \_/\_| |_/\____/\____/\_| \_/\___/\_|  |_/\___/ \____/')
print('\n')

# Parseia os dados do arquivo teste.txt
for line in open('/home/ryukahtk/teste.txt', 'r'):
    a.append(re.findall(r"[\S']+", line)[0])
    b.append(re.findall(r"[\S']+", line)[5])

print(b[1])
print(a[1])

menu = input('Selecione o nivel da classificação')
if menu == '1':
    labels = ['Sample 1']
    classified = float(a[1])
    unclassified = float(a[0])
    width = 2.0       # the width of the bars: can also be len(x) sequence

    fig, ax = plt.subplots()

    ax.bar(labels, classified, width, label='classified', color=['green'])
    ax.bar(labels, unclassified, width, label='unclassified', color=['blue'])

    ax.set_ylabel('Signifiance')
    ax.set_title('Sample 1')
    ax.legend()

    plt.show()

elif menu == '2':
    labels = ['Sample 1']
    proteo = float(a[4])
    actino = float(a[228])
    firmic = float(a[283])
    chrolo = float(a[326])
    teneri = float(a[335])
    bacteriori = float(a[346])
    gemma = float(a[397])
    acidob = float(a[405])
    nitros = float(a[432])
    defferi = float(a[437])
    width = 2.0       # the width of the bars: can also be len(x) sequence

    fig, ax = plt.subplots()

    ax.bar(labels, proteo, width, label='Proteobacteria', color=['green'])
    ax.bar(labels, actino, width, label='Actinobacteria', color=['blue'])
    ax.bar(labels, firmic, width, label='Firmicutes', color=['yellow'])
    ax.bar(labels, chrolo, width, label='Chloroflexi', color=['orange'])
    ax.bar(labels, teneri, width, label='Tenericutes', color=['black'])
    ax.bar(labels, bacteriori, width, label='Bacteroidetes', color=['pink'])
    ax.bar(labels, gemma, width, label='Gemmatimonadetes', color=['gray'])
    ax.bar(labels, acidob, width, label='Acidobacteria', color=['red'])
    ax.bar(labels, nitros, width, label='Nitrospirae', color=['purple'])
    ax.bar(labels, defferi, width, label='Deferribacteres', color=['blue'])
    ax.set_ylabel('Signifiance')
    ax.set_title('Sample 1')
    ax.legend()

    plt.show()

else:
    print('Opção invalida')
