n = float(input('Quantos reais você tem na carteira? R$'))
d = float(input('Qual a cotação do dólar no dia de hoje? R$'))
e = float(input('Qual a cotação do euro no dia de hoje? R$'))
c1 = n/d
c2 = n/e
print('Com {:.2f} reais, a uma cotação de {:.2f}, você pode comprar {:.2f} dólares.'.format(n, d, c1))
print('Com {:.2f} reais, a uma cotação de {:.2f}, você pode comprar {:.2f} euros.'.format(n, e, c2))


