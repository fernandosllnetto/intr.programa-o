salario = float(input('Digite seu salario mensal R$: '))
imposto =  0.0
if salario <= 2000:
    imposto = 0
    print('isento')
elif salario <= 2000 <= 3500:
    imposto = (salario - 2000) * 0.10
    print(f'Imposto de renda a pagar: R$ {imposto:.2f}')

else:
    imposto = 1500 * 0.10
    imposto += (salario - 3500) * 0.15
    print(f'Imposto de renda a pagar: R$ {imposto:.2f}')