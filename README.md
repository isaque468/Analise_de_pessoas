# 📊 Análise de Dados de Pessoas

> **Exercício prático de Python** desenvolvido para consolidar conceitos de estruturas de repetição, condicionais e manipulação de dados.

## 🎯 Objetivo
Criar um programa que coleta informações de 4 pessoas e gera estatísticas sobre:
- Média de idade do grupo
- Homem mais velho
- Quantidade de mulheres com menos de 20 anos

## 🛠️ Tecnologias Utilizadas
- **Python 3.x**
- Estruturas de repetição (for)
- Condicionais (if/elif)
- Manipulação de strings
- Entrada e saída de dados

## 📱 Contexto de Desenvolvimento
Este código foi desenvolvido **inteiramente pelo celular**, demonstrando adaptabilidade e dedicação ao aprendizado de programação em qualquer ambiente.

## 🔧 Funcionalidades
- ✅ Coleta dados de nome, idade e sexo
- ✅ Calcula média de idade automaticamente
- ✅ Identifica o homem mais velho do grupo
- ✅ Conta mulheres menores de 20 anos
- ✅ Validação de entrada para sexo (M/F)
- ✅ Formatação limpa dos resultados

## 💻 Como Executar
```bash
# Execute o programa
python analise_pessoas.py
```

## 📋 Exemplo de Uso
```
-----------1° Pessoa ------------
Nome: João
Idade: 25
Sexo [M/F]: M

-----------2° Pessoa ------------
Nome: Maria
Idade: 18
Sexo [M/F]: F

[...continua para 4 pessoas...]

# Saída:
A média da idade do grupo é de 22.5 anos
O homem mais velho tem 25 anos e se chama João
Ao todo são 1 mulheres com menos de 20 anos
```

## 🧠 Conceitos Aplicados
- **Estruturas de Repetição**: Loop `for` para iterar sobre as 4 pessoas
- **Condicionais**: Lógica para identificar homens, mulheres e idades
- **Acumuladores**: Variáveis para somar idades e contar mulheres
- **Manipulação de Strings**: Tratamento de entrada com `.strip()` e validação
- **Formatação**: Uso de `.format()` para saída organizada

## 🎯 Lógica Implementada
1. **Coleta de Dados**: Loop que solicita informações de cada pessoa
2. **Rastreamento do Homem Mais Velho**: Comparação de idades entre homens
3. **Contagem de Mulheres Jovens**: Incremento para mulheres < 20 anos
4. **Cálculo de Média**: Soma total dividida pelo número de pessoas

## 🚀 Possíveis Melhorias Futuras
- [ ] Adicionar validação de entrada mais robusta
- [ ] Implementar tratamento de erros (try/except)
- [ ] Criar interface gráfica
- [ ] Salvar resultados em arquivo
- [ ] Expandir para N pessoas (não limitado a 4)

## 👨‍💻 Aprendizado
Este exercício consolidou meu entendimento sobre:
- Lógica de programação básica
- Estruturas de controle em Python
- Manipulação de dados de entrada
- Organização de código legível

---

**Desenvolvido por Isaque Silva **  
*Parte da minha jornada de aprendizado em Python*
