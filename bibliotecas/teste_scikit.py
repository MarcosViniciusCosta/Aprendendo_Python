from sklearn import tree

if __name__ == "__main__":
    print("Olá, Mundo!")
    
    #0 goleiro
    #1 jogador de linha
    altura = [
        [155],
        [192],
        [188],
        [185],
        [192],
        [199],
        [176]
    ]
    
    rotulos = [
        [1],
        [0],
        [1],
        [1],
        [0],
        [0],
        [1]
    ]
    
    #declaracao árvore
    arvore = tree.DecisionTreeClassifier()
    
    #treinamento
    arvore.fit(altura, rotulos)
    
    #previsoes

    print(arvore.predict([[180]]))
    print(arvore.predict([[198]]))
    print(arvore.predict([[182]]))
    print(arvore.predict([[159]]))
    print(arvore.predict([[190]]))

