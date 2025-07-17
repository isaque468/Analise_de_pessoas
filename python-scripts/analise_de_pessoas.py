"""
Programa: Análise de Dados de Pessoas
Objetivo: Coletar informações de 4 pessoas e gerar estatísticas
Autor: [Seu Nome]
Data: [Data atual]
Desenvolvido pelo celular como exercício de aprendizado
"""

# Inicialização das variáveis
somaidade = 0              # Acumulador para somar todas as idades
media_idade = 0            # Armazenará a média calculada
maior_idade_do_homem = 0   # Maior idade encontrada entre os homens
nome_velho = ' '           # Nome do homem mais velho
totmulher20 = 0            # Contador de mulheres com menos de 20 anos

# Loop principal: coleta dados de 4 pessoas
for p in range(1, 5):
    print("-----------{}° Pessoa ------------".format(p))
    
    # Entrada de dados com tratamento de espaços
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip()
    
    # Acumula a idade para calcular média depois
    somaidade += idade
    
    # Lógica para identificar o homem mais velho
    # Se for a primeira pessoa E for homem, define como referência inicial
    if p == 1 and sexo in "Mm":
        maior_idade_do_homem = idade
        nome_velho = nome
    
    # Para os demais homens, compara se a idade é maior que a atual
    if sexo in "Mm" and idade > maior_idade_do_homem:
         maior_idade_do_homem = idade
         nome_velho = nome
    
    # Conta mulheres com menos de 20 anos
    if sexo in "Ff" and idade < 20:
         totmulher20 += 1

# Cálculo da média de idade
media_idade = somaidade / 4

# Exibição dos resultados
print("A média da idade do grupo é de {} anos".format(media_idade))
print("O homem mais velho tem {} anos e se chama {} ".format(maior_idade_do_homem, nome_velho))
print("Ao todo são {} mulheres com menos de 20 anos".format(totmulher20))
