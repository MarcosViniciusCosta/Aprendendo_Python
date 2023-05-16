import math

print("Digite o tamanho da área a ser pintada (em metros quadrados): ")
quantidadeMetrosQuadrados = float(input())
QuantidadelitrosDeTinta = quantidadeMetrosQuadrados/6
quantidadeLatas = math.ceil(QuantidadelitrosDeTinta/18)
quantidadeGaloes = math.ceil(QuantidadelitrosDeTinta/3.6)
precoLata = 80*quantidadeLatas
precoGalao = 80*quantidadeGaloes
print("Quantidades de latas necessárias =",quantidadeLatas,". Preço total =",precoLata)
print("Quantidades de galoes necessários =",quantidadeGaloes,". Preço total =",precoGalao)