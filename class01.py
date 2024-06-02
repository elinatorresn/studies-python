faturamento = 1200 #tipo: int -> numero inteiro
custo = 750.45 #tipo: float -> numero com casa decimal

novas_vendas = 100
faturamento = faturamento + novas_vendas

imposto = faturamento * 0.1

lucro = faturamento - custo - imposto
margem_lucro = lucro / faturamento

print("O faturamento foi de", round(faturamento, 2))
print("O custo foi de", round(custo, 2)) 
print("O imposto foi de", round(imposto, 2))
print("O lucro foi de", round(lucro, 2))
print("A margem de lucro foi de", round(margem_lucro, 2))

mensagem = "O faturamento foi grandão" #tipo: string -> texto
email = "teste@teste.com" #tipo: string -> texto

teve_lucro = True #tipo: boolean -> sim ou não

#Mod -> % Significa o resto da divisão

print(10 % 3) #Resto da divisão por 10

tempo_contrato = 170
tempo_anos = 170 / 12
tempo_meses = 170 % 12
print("Tempo do contrato em anos:", int(tempo_anos))
print("Tempo do contrato em meses:", tempo_meses)

print("Tempo total do contrato:", int(tempo_anos), "anos e", tempo_meses, "meses")