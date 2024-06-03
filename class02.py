faturamento = 1200
custo = 700
lucro = faturamento - custo
margem_lucro = lucro / faturamento

# print("Faturamento da empresa: {faturamento}, Custo {custo}, Lucro {lucro}".format(faturamento, custo, lucro))

print(f"Faturamento da empresa: {faturamento}, Custo {custo}, Lucro {lucro}") #Usar o f no inicio do texto para mesclar string e variavel no print


email_cliente = "meuemailaleatorio@email.com"

email_cliente = email_cliente.upper() #transformar variavel para maiuscula
print(email_cliente)

email_cliente = email_cliente.lower() #transformar variavel para minuscula
print(email_cliente)


print(email_cliente.find("@")) #encontrar a posicao do @

print(len(email_cliente)) #verificar o tamanho do texto

print(email_cliente[4]) #pegar um caractere especifico se existir

print(email_cliente[-4]) #pegar um caractere especifico de tras pra frente

print(email_cliente[:8]) #pegar até o index 4

print(email_cliente[17:23]) #pegar do index 17 até o index 23

novo_email = email_cliente.replace("email.com", "gmail.com") #trocar um pedaço do texto de acordo com o anterior
print(novo_email)


nome = "ELINA torres"
print(nome.capitalize()) #deixa a primeira letra maiuscula
print(nome.title()) #deixa a primeira letra de cada palavra maiuscula

#pegar o servidor do email
posicao_arroba = email_cliente.find("@") + 1
servidor = email_cliente[posicao_arroba:]
print(servidor)

#pegar o primeiro nome 
posicao_espaco = nome.find(" ")
primeiro_nome = nome[:posicao_espaco].title()
print(primeiro_nome)

#pegar o sobrenome
segundo_nome = nome[posicao_espaco+1:].title()
print(segundo_nome)


# Casos especiais

print(f"Faturamento da empresa: R${faturamento:.2f}, Custo R${custo:.2f}, Lucro R${lucro:.2f}, Margem: {margem_lucro:.0%}") #Usar o : apos a variavel pra formatar