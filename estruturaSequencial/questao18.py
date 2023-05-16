import math

print("Digite o tamanho do arquivo (em MB): ")
tamanhoEmMB = float(input())
print("Digite a velocidade de download (em Mbps): ")
velocidadeDownloadEmMbps = float(input())
tempoDeDownloadEmSegundos = tamanhoEmMB/velocidadeDownloadEmMbps
tempoDeDownloadEmMinutos = tempoDeDownloadEmSegundos/60
print(tamanhoEmMB,"MB serão baixados em aproximadamente",math.ceil(tempoDeDownloadEmMinutos),"minutos") 
