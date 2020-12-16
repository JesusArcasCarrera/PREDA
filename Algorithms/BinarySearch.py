""" 
Binary search
Busqueda binaria

@familia 
divide y venceras

@descripcion
solo busca si un elemento esta o no arbol binario

"""
def binary_search(vector,target, positions = None):
    if positions is None:
         positions = (0, len(vector))
       
    
    i , j = positions

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



""" Another """
def busqueda_binaria(i,j,vector,target):
    
    if i==j:
        if vector[i]==target:
            return True
        else:
            return False
    else:
        m=(i+j)//2
        if vector[m]<=target:
            return busqueda_binaria(i,m,vector,target)
        else:
            return busqueda_binaria(m+1,j,vector,target)


#TODO 
if __name__ == "__main__":
    v = [1,2,3,4,6,7,8,9,15]
    print(binary_search(v,9))
    print(binary_search(v,5))