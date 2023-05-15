import numpy as num

if __name__ == '__main__':
    #vetor = num.array([[1,2,3],[4,5,6],[7,8,9]])
    #print(vetor[-1][-3])
    #lista3 = num.arange(1,16).reshape(3,5)
    #print(lista3[2,-2]) 
    #print("Dimensões",vetor.ndim)
    lista = num.arange(1,11) * 2
    print(lista[3:7:2])