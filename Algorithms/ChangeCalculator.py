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

def print_change(change,coins):
    i=0
    for c in change:
        if c>0:
            print(f'{c} coins of {coins[i]}')
        i+=1

coins = [1,2,4,8]
amount = 61
back = []

coins.sort(reverse=True)

#voraz
for coin in coins:
    if amount>=0:
        back.append(amount//coin)
        amount %= coin
        

print_change(back,coins)


print('-'*50,'\n')


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


print('-'*50,'\n')


#dynamic
# non-classical dynamic implementation without matrix

coins = [10,6,1]
amount = 24
best_back = [0]*len(coins) #fill matrix with 0s


for i in range(len(coins)): 
    loop_amount = amount
    loop_back = [0]*len(coins)
    for j in range(i,len(coins)):
        if loop_amount>0:
            coin = coins[j]
            loop_back[j] = loop_amount//coin
            loop_amount %= coin

    
    if sum(loop_back)<sum(best_back) or sum(best_back)==0:
        best_back = loop_back
   
# just print result
print_change(best_back,coins)



print('-'*50,'\n')

#recursive

coins = [10,6,1]
amount = 24
best_back = [0]*len(coins) #fill matrix with 0s


def change(ind,coins,amount,best_back):
    print(best_back)
    if ind<len(coins):
        loop_amount = amount
        loop_back = [0]*len(coins)
        for j in range(ind,len(coins)):
            if loop_amount>0:
                coin = coins[j]
                loop_back[j] = loop_amount//coin
                loop_amount %= coin

        if sum(loop_back)<sum(best_back) or sum(best_back)==0:
            best_back = loop_back

        return change(ind+1,coins, amount,best_back)
    else:
        return best_back

best_back = change(0,coins, amount,best_back)
# just print result
print_change(best_back,coins)
