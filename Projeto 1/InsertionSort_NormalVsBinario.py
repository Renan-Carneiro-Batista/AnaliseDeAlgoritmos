import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import time
 
def buscaBinaria(array, key, start, end):
    if end - start <= 1:
        if key < array[start]:
            return start - 1
        else:
            return start
 
    mid = (start + end)//2
    if array[mid] < key:
        return buscaBinaria(array, key, mid, end)
    elif array[mid] > key:
        return buscaBinaria(array, key, start, mid)
    else:
        return mid     

def insertionSortBinario(array):
    TempoInicial = time.time()

    for i in range(1, len(array)):
        temp = array[i]
        pos = buscaBinaria(array, temp, 0, i) + 1
 
        for k in range(i, pos, -1):
            array[k] = array[k - 1]
 
        array[pos] = temp
    
    TempoFinal = time.time()
    TempoTotal = TempoFinal - TempoInicial
    
    row[2] = TempoTotal
    
    print("\n--== Insertion Sort Binário ==--")
    print("Tempo de execução:", TempoTotal, "segundos.")
    
    return array
        
def insertionSort(array):
    TempoInicial = time.time()
    
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
    
    TempoFinal = time.time()
    TempoTotal = TempoFinal - TempoInicial
    
    row[1] = TempoTotal
    
    print("\n--== Insertion Sort Normal ==--")
    print("Tempo de execução:", TempoTotal, "segundos.")
    
    return array

tamanhoArray = np.random.randint(10, 10000, size=(10))
comp_df = pd.DataFrame()
  
for i in range(len(tamanhoArray)):
    array = np.random.randint(-2*tamanhoArray[i], 2*tamanhoArray[i], size=(tamanhoArray[i]))
    
    row = np.empty(3)
    row[0] = len(array)
    
    print("\nVetor Desordenado: ", array)
    print("Vetor Ordenado: ", insertionSort(array))
    print("\n")

    print("Vetor Ordenado: ", insertionSortBinario(array))
    print("\n") 
    
    comp_df = pd.concat([comp_df, pd.DataFrame(row).T])
    del(row)
    
comp_df = comp_df.rename({0: 'Tamanho da Entrada', 1: 'Insertion Sort Normal', 2: 'Insertion Sort Binário'}, axis=1)
comp_df = comp_df.reset_index(drop=True)

print(comp_df)

comp_df = comp_df.sort_values(by=['Tamanho da Entrada'])
comp_df = comp_df.reset_index(drop=True)

comp_df.plot(x = 'Tamanho da Entrada')
plt.xlabel('Tamanho da Entrada')
plt.ylabel('Tempo de Execução (em segundos)')
plt.show()