# 135 = 5*27 = 5*20 + 5*7 = (multiplo_centena + multiplo_unidade)*divisor
# 135 = 100+35 = 20*5 + 7*5 = (20+7)5 = (4*5 + 7*1)5

# *100
centena = int(input('Digite a centena em uma unidade: '))
centena = centena*100
print(centena)
# *10
dezena_aux = int(input('Digite a dezena em uma unidade: '))
dezena = dezena_aux*10
print(dezena)
# *1
unidade = int(input('Digite a unidade: '))
print(unidade)
# c100 + d10 + u1
inteiro = int(centena + dezena + unidade)
print('Inteiro = {}'.format(inteiro))
# (dezena + unidade)multiplo = dezena*multiplo + unidade*multiplo => (dezena + unidade) / multiplo 
divisor = int(input('Digite o divisor dos algarísmos: '))
multiplo_dezena = int(dezena / divisor)
multiplo_unidade = int(unidade / divisor)
print('Multiplo da dezena: {}'.format(multiplo_dezena))
print('Multiplo da unidade: {}'.format(multiplo_unidade))
# centena + (multiplo_dezena * divisor) + (multiplo_unidade + divisor) = inteiro
print('{} + {}*{} + {}*{} = {}'
    .format(centena, multiplo_dezena, divisor, multiplo_unidade, divisor, inteiro))

multiplo_centena = int(centena/divisor)
print('Múltiplo da centena: {}'.format(multiplo_centena))
multiplo_soma_dezenaEunidade = int((dezena + unidade) / divisor) 
print('Múltiplo da soma da dezena com a unidade: {}'.format(multiplo_soma_dezenaEunidade))

multiplo = int(multiplo_centena+multiplo_soma_dezenaEunidade)
print('Soma do múltiplo da centena {} e o múltiplo da soma da dezena com a unidade {}: {}'
    .format(multiplo_centena, multiplo_soma_dezenaEunidade, multiplo))

print('{}*{} = {} <=> {}*{} + {}*{}'
    .format(multiplo, divisor, inteiro, multiplo_centena, divisor, multiplo_soma_dezenaEunidade, divisor))