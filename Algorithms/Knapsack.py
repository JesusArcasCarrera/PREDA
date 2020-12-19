""" 

Knapsack Problem
Problema de la mochila

@familia
voraz
dinamica

@descripcion
Tratamos de meter n elementos con un peso weight y valor value en una mochila con capacidad capacity
Empezare resolviendo la forma simple, con una unica mochila, con planteamiento voraz y dinamico

Observar que si la suma de los pesos es menor o igual que la capacidad de la mochila, el problema es trivial
Asi que interesa resolver cuando la suma es mayor que la capacidad de la mochila 

Adicionalmente, en algunas implementaciones los objetos seran fraccionables

"""


""" 
    voraz 
    elements -> [(weight, value)]
    We need to choose a condition for select next best candidate
    We have three posibles selection functions:
        Higher value
        Lower weight
        Higher value/weight -> optimal
"""

def napsack(elements, capacity):
    index = list(range(len(elements)))
    elems = zip(elements, index)
    relation = [(r[1]/r[0],i) for r,i in elems]
    relation.sort(reverse=True)
    acumulate = 0
    position = 0
    solution = []
    #position restriction is not really necessary here
    while acumulate < capacity and position<len(relation):
        element_index = relation[position][1]
        next_element = elements[element_index]
        
        free = capacity-acumulate

        if next_element[0] < free:
            acumulate += next_element
            solution.append((element_index,1))
        else:
            acumulate = capacity
            percent = (free/next_element[0])
            solution.append((element_index,percent))

        position += 1

    return solution


