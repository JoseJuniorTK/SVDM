import os
import re
import matplotlib.pyplot as plt

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

# Input dos dados para visualizacao
labels = b[1], b[0]
sizes = [a[1], a[0]]

# Configuracao do grafico
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')

# Mostra o resultado final
plt.show()
