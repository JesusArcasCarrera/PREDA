""" 
Counting Sort
Ordenacion por conteo


Realmente no mueve los elementos para ordenarlos, cuenta las ocurrencias de cada elemento y luego las escribe.
"""


def counting_sort(elements, inplace=True):
    occurences = {k:0 for k in range(max(elements)+1)}

    for element in elements:
        occurences[element] +=1

    #new_list = [[v]*c for (v,c) in occurences.items()]
    #flatten_list = [elem for sublist in new_list for elem in sublist ]

    lista = [elem for sublist in [[v]*c for (v,c) in occurences.items()] for elem in sublist]

    if inplace:
        for idx in range(len(elements)):
            elements[idx] = lista[idx]

        return elements
    else:
        return lista