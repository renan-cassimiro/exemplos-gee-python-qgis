# Variaveis int (numeros inteiros)
intA = 4
intB = 2

# Operador "+" resulta em soma algebrica
print("Soma: ",intA + intB)

# Variaveis float (numeros com ponto flutuante)
numA = 4.3
numB = 2.2

# Operador "+" também resulta em soma algebrica
print("Soma: ", numA + numB)

#variaveis string (texto). Os valores ficam em aspas simples ou duplas
textoA = "4"
textoB = "2"

# Operador "+" também resulta em concatenação
print("Concatenação: ", textoA + textoB)

# Para realizar soma, é preciso converter os valores das variáveis. As funções 
#int(), float() e str() convertem os valores para seru respectivos tipos
print("Soma: ", int(textoA) + int(textoB))

#O tipo da variavel (int, string, float) é definido pelo conteudo. Ao atribuir 
#um texto para um variavel que era int, a variavel automaticamente é convertida para string

intA = "texto de exemplo"

#Função type() retorna o tipo da variável
print("Valor:", intA, "Tipo:", type(intA))