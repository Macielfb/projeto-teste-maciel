def infracoes():

    velocidade = int(input('Digite sua velocidade:  '))

    velocidade_maxima = 80

    if velocidade <= velocidade_maxima:
        print('Nao levou multa')

    elif velocidade > velocidade_maxima and velocidade <= velocidade_maxima + 10:
        print('Levou multa leve')

    elif velocidade >= velocidade_maxima + 11 and velocidade <= velocidade_maxima + 20:
        print('Levou multa grave')

    elif velocidade > velocidade_maxima + 20:
        print('Levou multa gravissima')

consulta = infracoes()
print(consulta)        