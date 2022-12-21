# -*- coding: utf-8 -*-
"""Exercícios Listas Hashtag.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rArd0DuBpPD3TVyIij117EjJgZDYcXC0

# Exercícios

## 1. Faturamento do Melhor e do Pior Mês do Ano

Qual foi o valor de vendas do melhor mês do Ano?
E valor do pior mês do ano?
"""

meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
vendas_1sem = [25000, 29000, 22200, 17750, 15870, 19900]
vendas_2sem = [19850, 20120, 17540, 15555, 49051, 9650]

vendas_total = vendas_1sem + vendas_2sem

print(vendas_total)

maior_valor = max(vendas_total)

print(maior_valor)

valor_minim = min(vendas_total)

print(valor_minim)

"""## 2. Continuação

Agora relacione as duas listas para printar 'O melhor mês do ano foi {} com {} vendas' e o mesmo para o pior mês do ano.

Calcule também o faturamento total do Ano e quanto que o melhor mês representou do faturamento total.

Obs: Para o faturamento total, pode usar a função sum(lista) que soma todos os itens de uma lista
"""

i_maior_valor = vendas_total.index(maior_valor)
i_menor_valor = vendas_total.index(valor_minim)

print(i_maior_valor)
print(i_menor_valor)

print('O melhor mês do ano foi {} com {} vendas'.format(meses[i_maior_valor], maior_valor))
print('O pior mês do ano foi {} com {} vendas'.format(meses[i_menor_valor], valor_minim))

fat_total = sum(vendas_total)

print(fat_total)
print('Faturamento Total: R${:,}'.format(fat_total))

percentual = maior_valor/fat_total
print(percentual)
print('O melhor mês representou {:.1%} das vendas do ano'.format(percentual))

"""
top3 = []## 3. Crie uma lista com o top 3 valores de vendas do ano (sem fazer "no olho")

Dica: o método remove retira um item da lista."""

top3 = []

print(vendas_total)
maior_valor = max(vendas_total)
top3.append(maior_valor)


vendas_total.remove(maior_valor)
print(vendas_total)

maior_valor = max(vendas_total)
print(maior_valor)

top3.append(maior_valor)
vendas_total.remove(maior_valor)
print(vendas_total)

maior_valor = max(vendas_total)
top3.append(maior_valor)

print(top3)