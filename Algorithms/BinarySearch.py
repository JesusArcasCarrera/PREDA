""" 
Binary search
Busqueda binaria

@familia 
divide y venceras

@descripcion
solo busca si un elemento esta o no arbol binario

"""
import argparse

def binary_search(vector,target, positions = None):
    if positions is None:
         positions = (0, len(vector))
       
    
    i , j = positions
    print(positions)
    if i != j:

        half = sum(positions)//2
        print(half)

        if target <= vector[i]:
            new_positions = (i,half)
        else:
            new_positions = (half,j)
        
        return  binary_search(vector,target,new_positions)
         
    else:
        return (vector[i]==target)

""" 
#if you don't want two return

if i != j:
.
.
.
result = binary_search(new_positions,vector,target) 

else:
    result = (vector[i]==target)

return result


    """
#TODO 
if __name__ == "__main__":
    v = [1,2,3,4,6,7,8,9,15]
    print(binary_search(v,9))
    print(binary_search(v,5))