import math

print("Digite o tamanho da área a ser pintada (em metros quadrados): ")
quantidadeMetrosQuadrados = float(input())
QuantidadelitrosDeTinta = quantidadeMetrosQuadrados/3
quantidadeLatas = math.ceil(QuantidadelitrosDeTinta/18)
preco = 80*quantidadeLatas
print("Quantidades de latas necessárias =",quantidadeLatas,". Preço total =",preco)