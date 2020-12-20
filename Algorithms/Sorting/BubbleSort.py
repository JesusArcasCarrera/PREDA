
""" 
Bubble Sort
Ordenacion burbuja

@familia

@descripcion
El algoritmo más basico de ordenacion. Con un coste n^2.

"""


def bubble_sort(elements):
    for iter_num in range(len(elements)-1,0,-1):
        for idx in range(iter_num):
            if elements[idx]>elements[idx+1]:
                elements[idx],elements[idx+1] = elements[idx+1],elements[idx]
    return elements

def another_bubble_sort(elements):
   
    n = len(elements)

    for i in range(n):

        already = True

        for j in range(n - i - 1):
            if elements[j] > elements[j + 1]:
                elements[j], elements[j + 1] = elements[j + 1], elements[j]
                already = False

        if already:
            break

    return elements

def recursive_bubble_sort(elements):
        
        for idx in range(len(elements) - 1):
            if elements[idx] > elements[idx + 1]:
                elements[idx], elements[idx + 1] = elements[idx + 1], elements[idx]
        
        last = elements.pop()
        if len(elements) > 1:
            return recursive_bubble_sort(elements).append(last)
        else:
            return last


elements = []
def recursive_bubble_sort_inplace(n):
        if n == 1:
            return
        
        for idx in range(n - 1):
            if elements[idx] > elements[idx + 1]:
                elements[idx], elements[idx + 1] = elements[idx + 1], elements[idx]
        
        recursive_bubble_sort(n-1)
       


