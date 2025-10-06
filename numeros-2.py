import numpy
#print(arreglo)
Lista=[1,2,3]
my_array= numpy.array(Lista)
print(f"lista {Lista}")
print(f"arreglo {my_array}")
b=Lista + my_array
print(f"combinar {b}")
array_lista = my_array.tolist()
union = array_lista + Lista
print(f"arreglo to list {array_lista}")
print(f"union de las listas {union}")