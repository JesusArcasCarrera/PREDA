""" 
Insertion Sort



@descripcion


"""

def insertion_sort(elements):
    for i in range(1, len(elements)):
        j = i-1
        nxt_element = elements[i]
		
        while (elements[j] > nxt_element) and (j >= 0):
            elements[j+1] = elements[j]
            j=j-1
        elements[j+1] = nxt_element


def recursive_insertion_sort(elements):
    pass