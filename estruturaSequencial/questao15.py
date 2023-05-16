print("Digite o valor ganho por hora: ")
valorPorHora = float(input())
print("Digite a quantidade de horas trabalhadas mensalmente: ")
quantidadeHoras = int(input())
remuneracaoMensal = (valorPorHora*quantidadeHoras)
descontoINSS = 0.08 * remuneracaoMensal
descontoSindicato = 0.05 * remuneracaoMensal
descontoImpostoRenda = 0.11 * remuneracaoMensal
remuneracaoLiquida = 0.76 * remuneracaoMensal
print("a) Salário bruto =",remuneracaoMensal)
print("b) Desconto do INSS =", descontoINSS)
print("c) Desconto do sindicato =", descontoSindicato)
print("d) Salário líquido =", remuneracaoLiquida)
print("\n\n")
print("e) \n")
print(" + Salário Bruto : R$", remuneracaoMensal,"\n"
,"- IR (11%) : R$", descontoImpostoRenda,"\n"
,"- INSS (8%) : R$", descontoINSS,"\n"
,"- Sindicato ( 5%) : R$",descontoSindicato,"\n"
,"= Salário Liquido : R$",remuneracaoLiquida)

