def fatorial(x):
    if(x <= 1): 
        return 1
    else: 
        return x*fatorial(x-1)
    
resultado = fatorial(10)    
print("resultado = ",resultado," do tipo ",type(resultado))
    