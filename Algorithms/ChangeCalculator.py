""" 
Change Calculator
Calcular la vuelta

@familia 
voraz
dinamica

@descripcion
Calcula calcula la vuelta despues de pagar en monedas dadas
Este algoritmo tiene dos partes ya que en ocasiones se calcula mediante voraz y otras mediante dinamica


"""

from operator import itemgetter
 

coins = [1,2,4,8]
amount = 61
back = []

coins.sort(reverse=True)

#voraz
for coin in coins:
    if amount>=0:
        back.append(amount//coin)
        amount %= coin
        print(back)
        print(amount)






# Another voraz implements 
coins = [('1cent',1),('2cent',2),('4cen',4),('8cent',8)]
amount = 61
back = []

coins.sort(key=itemgetter(1),reverse=True)

# voraz
for text,coin in coins:
    if amount>=0:
        ncoins = amount//coin
        amount %= coin

        back.append(ncoins)

        print('{} coins of {}'.format(ncoins,text))
        print('Remainig Amount ',amount)



#dinamica

coins = [10,6,1]
amount = 24
backs = [[0]*len(coins) for c in coins] #fill matrix with 0s

print(backs)

for i in range(len(coins)): 
    loop_amount = amount
    for j in range(i,len(coins)):
        if loop_amount>0:
            coin = coins[j]
            backs[i][j] = loop_amount//coin
            loop_amount %= coin

   
   
print(backs)

# just print result
# for b in backs:
    #print(f'{coins[1]} coins of {coins[0]}')