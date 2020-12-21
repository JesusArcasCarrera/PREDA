""" 
Cuadratic Sort

Aun más basico e ineficiente que burbuja. JAMAS usar este algoritmo 
"""

def cuadratic_sort(elements):
    for i in range(len(elements)):
        for j in range(i, len(elements)):
            if elements[i]>elements[j]:
                elements[i],elements[j] = elements[j],elements[i]
    return elements
