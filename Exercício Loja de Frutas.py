# Exercício de Loja de frutas - Python.org

# 27. Uma fruteira está vendendo frutas com a seguinte tabela de preços:

#                    Até 5 Kg              Acima de 5 Kg
#  Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#  Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00,
# receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg)
# de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

# Passo 1: Pedir a quantidade em Kg de morangos;

validamorango = False

while validamorango == False:
    try:
        peso_morango = float(input('Informar o peso em Kg de morangos: '))
        while peso_morango < 0:
            print('Favor preencher com um peso maior ou igual a zero.')
            peso_morango = float(input('Informar o peso em Kg de morangos: '))
        validamorango = True
    except ValueError:
        print('Favor digitar corretamente o peso em Kg de morangos.')


# Passo 2: Pedir a quantidade em Kg de maçãs;

validamaca = False

while validamaca == False:
    try:
        peso_maca = float(input('Informar o peso em Kg de maçãs: '))
        while peso_maca < 0:
            print('Favor preencher com um peso maior ou igual a zero.')
            peso_maca = float(input('Informar o peso em Kg de maçãs: '))
        validamaca = True
    except ValueError:
        print('Favor digitar corretamente o peso em Kg de maçãs.')

# Passo 3: Informar o preço do morango e da maçã;

preco_morango = float(0)

preco_maca = float(0)

if peso_morango > 5:
    preco_morango = float(2.2)

elif peso_morango > 0:
    preco_morango = float(2.5)

if peso_maca > 5:
    preco_maca = float(1.5)

elif peso_maca > 0:
    preco_maca = float(1.8)

# Passo 4: Calcular o preço final da compra;

compra_total = ((peso_morango * preco_morango) + (peso_maca * preco_maca))

# Passo 5: Se a compra ultrapassar R$ 25,00 considerar um desconto de 10% da compra total;


print(f'\nPreço total de morangos: R$ {peso_morango * preco_morango:_.2f}'.replace('.',',').replace('_','.')+'.')
print(f'Preço total de maçãs: R$ {peso_maca * preco_maca:_.2f}'.replace('.',',').replace('_','.')+'.')

if compra_total > 25:
    desc = compra_total * 0.1
    print(f'Valor do desconto: R$ {desc:_.2f}'.replace('.',',').replace('_','.')+'.')
    print(f'\nSua compra foi no total de R$ {compra_total:_.2f}, com desconto de R$ {desc:_.2f}, o preço final foi de R$ {compra_total - desc:_.2f}'.replace('.',',').replace('_','.')+'.')

# Passo 6: Apresentar os valores finais para o cliente.

else:
    print(f'Sua compra foi no total de R$ {compra_total:_.2f}'.replace('.',',').replace('_','.')+'.')






