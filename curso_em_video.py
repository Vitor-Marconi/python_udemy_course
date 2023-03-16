# -*- coding: utf-8 -*-
"""Curso_em_video.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Z1s4-DVDU1Je6FH0uWMspwifjLPcGi2u

#CURSO EM VIDEO
#Variáveis
"""

# O python é uma liguagem dinamica, ou seja, você não amarra uma variável, porem ele consegue interpretar varias variaveis ele pode ser classificado como uma variavel fortemente tipada e dinamicamente tipada

#Int
a = 5
b = 4 
print(a+b)

#String
a = 'Hey bro what do you think ?'
print (a)

#float
b = 5.2

"""#Operadores Aritméticos """

print(2 + 3)
print(4 - 7)
print(2 * 5.3) #Resultado tipo float 
print(9.4 / 3)
print(9.4 // 3) #Retorna um float inteiro 
print(2 ** 8) #Potencia 
print(10 % 3) #Modulo é o resto da divisão 

a = 12
b = a 
print(a + b)

# Operadores aritimeticos são binarios, ou seja, que precisa de dois operandos para que ela aconteça 
# O simbulo de (+ - %) recebe o nome de infixo

# Caso de UM OPERANDO UNARIO operando prefixado para adicionar ou subtrair (depende do infixo) alguma unidade a variável (Dois infixos seguidos antes do operador) EX:
#x = 7
#y = 5
#print (x + y)
#++y
#--x

"""#Desafio"""

# Minhas variáveis 
# Qual é o percentual de compromentimento que  tem das despesas em cima do salário ?
salario = 3450.45
despesas = 2456.2

#Resposta 
compromentimento_do_salario = despesas / salario * 100
compromentimento_do_salario

"""#Operadores Relacionais """

3 > 4

5 >= 8

7 < 8

3 <= 1

3 != 2 # O signficado do infixo é diferente

3 == 3

2 == '3' # Falso porque um é inteiro é o outro é um texto ou string(em ingles)

"""#OPERADORES DE ATRIBUIÇÃO 




"""

a = 3 
a = a + 7
print(a)

#a = 5 (subistituindo o valor)
a += 5 #(acresentando o valor) # a = a + 5 
print(a)

a -= 3
print(a)

a *= 2
print(a)

a /= 4
print(a)

a %= 4
print(a)

a **= 8
print(a)

a //= 256
print(a)

"""#Operadores Lógicos """

True or False
7 != 3 and 2 > 3

# Tabela verdade do AND

True and True

True and False

False and True

False and False

# tabela verdade do OR
True or True

True or False

False or True

False or False

False or False or True or False

# Tabela verdade do XOR
True != True

True != False

False != True

False != False

# Operador de Negação (unário)
not True

not False

not False

not 0

not 1

not -1

not not -1

# Um pouco da realidade 
saldo = 1000
salario = 4000
despesas = 2967
meta = saldo > 0 and salario - despesas >= 0.2 * salario

meta

saldo = 1000
salario = 4000
despesas = 3967
meta = saldo > 0 and salario - despesas >= 0.2 * salario
meta

# Operador Bit-a-Bit n pode ser usados com operadores lógicos

saldo = 1000
salario = 4000
despesas = 3967

saldo_positivo = saldo > 0
despesas_controladas = salario - despesas >= 0.2 * salario
meta = saldo_positivo and despesas_controladas
meta

# Desfio Operadores Lógicos 
trabalho_terça = True 
trabaho_quinta = False 

"""
- Confirmando os 2: TV 50' + Sorvete
- Confrimando apenas 1: TV 32' + Sorvete
- Nenhum confirmado: Fica em casa
"""

tv_50 = trabalho_terça and trabaho_quinta
sorvete = trabalho_terça or trabaho_quinta
tv_32 = trabalho_terça != trabaho_quinta
mais_saudavel = not sorvete

print("Tv50={} Tv32={} Sorvete={} Saudável={}"
     .format(tv_50, tv_32, sorvete, mais_saudavel))

trabalho_terça = False
trabaho_quinta = False 

"""
- Confirmando os 2: TV 50' + Sorvete
- Confrimando apenas 1: TV 32' + Sorvete
- Nenhum confirmado: Fica em casa
"""

tv_50 = trabalho_terça and trabaho_quinta
sorvete = trabalho_terça or trabaho_quinta
tv_32 = trabalho_terça != trabaho_quinta
mais_saudavel = not sorvete

print("Tv50={} Tv32={} Sorvete={} Saudável={}"
     .format(tv_50, tv_32, sorvete, mais_saudavel))

trabalho_terça =  False
trabaho_quinta = True 

"""
- Confirmando os 2: TV 50' + Sorvete
- Confrimando apenas 1: TV 32' + Sorvete
- Nenhum confirmado: Fica em casa
"""

tv_50 = trabalho_terça and trabaho_quinta
sorvete = trabalho_terça or trabaho_quinta
tv_32 = trabalho_terça != trabaho_quinta
mais_saudavel = not sorvete

print("Tv50={} Tv32={} Sorvete={} Saudável={}"
     .format(tv_50, tv_32, sorvete, mais_saudavel))

trabalho_terça = True 
trabaho_quinta = False 

"""
- Confirmando os 2: TV 50' + Sorvete
- Confrimando apenas 1: TV 32' + Sorvete
- Nenhum confirmado: Fica em casa
"""

tv_50 = trabalho_terça and trabaho_quinta
sorvete = trabalho_terça or trabaho_quinta
tv_32 = trabalho_terça != trabaho_quinta
mais_saudavel = not sorvete

print("Tv50={} Tv32={} Sorvete={} Saudável={}"
     .format(tv_50, tv_32, sorvete, mais_saudavel))
# Método .format
#"{}, {} = {}".format(1, False, 'resultado')

"""# Operadores Unários"""

a =3

# a += 1
# a

# a ++

++a

-a

a = -a

a

"""#Operadores Ternários"""

esta_chuvendo = True
print('Hoje estou com as roupas' + ('secas', 'molhadas')[esta_chuvendo])

esta_chuvendo = False
print('Hoje estou com as roupas ' + ('molhadas.' if esta_chuvendo else 'secas.'))



"""# Mais operadores (membro/identidade)

"""

#Operador de Membro
lista = [1, 2, 3, 'Ana', 'Carla']

2 in lista

'Ana' not in lista

#Operador de Identidade 
x = 3
y = x
z = 3

x is y

y is z

x is not z

Lista_a = [1, 2, 3]
Lista_b = Lista_a
Lista_c = [1, 2, 3]

Lista_a is Lista_b

Lista_b is Lista_c

Lista_a is not Lista_c

"""# Builtins

"""

#type()

# De onde vem a função type() 
# R = Do Builtins que e um Modulo que gera varias funcionalidades 
type(1)

__builtins__.type('Fala galera')

__builtins__.print( 10 / 3)

__builtins__.help(__builtin__.dir)

#dir()

#dir(__builtins__)

nome = 'João da silva'

type(nome)

__builtins__.len(nome)

"""#Conversão de Tipos 

"""

2 + 3

'2' + '3'

# 2 + '3'
#print(2 + '3')
 
a = 2
b = '3'

print(type(a))
print(type(b))

print(a + int(b))

print(str(a) + b)

"""#Coerção automática

"""

10/2

type(10/2)

10/3

10//3

type(10//3)

10//3.3

10 /2.5

2 + True # Assume o (True como se fosse int 1)

2 + False # Assume o (True como se fosse int 0)

type(1 + 2)

type( 1 + 2.5)

"""#Tipos Numéricos  """

#dir(int)

#dir(float)

a = 5
b = 2.5

a/b

b.is_integer()

5.0.is_integer()

#dir(int)

int.__add__(2, 3)

(-2).__abs__()

# 1.1 + 2.2

from decimal import Decimal, getcontext

Decimal(1)/Decimal(7)

getcontext().prec = 4
Decimal(1) / Decimal(7)

Decimal.max(Decimal(1), Decimal(7))

"""

>Numeros#1



"""

#dir(int)

#dir(float)

a = 5
b = 2.5
a / b

a + b

type(a)

type(b)

type(a-b)

b.is_integer()

5.0.is_integer()

int.__add__(2,3)

2 + 3

(-2).__abs__()

abs(-2)

(-3.6).__abs__()
dir(float)
abs(-3.6)

#1.1 +2.2
#importando o decimal
from decimal import Decimal, getcontext

#dir(Decimal)

Decimal(1) / Decimal(7)

# precisão de casas "getcontext().prec" 
getcontext().prec = 4
Decimal(1) / Decimal(7)

Decimal.max(Decimal(1), Decimal(7))

1.1 + 2.2

Decimal(1.1) + Decimal(2.2)

"""# STRING

"""

# String é um objeto imutavel

nome = "Saulo Pedro"
nome

nome[0]

#nome[0] = 'P'
#Erro, n pode mudar a string propriamente dita

#"marca d' agua'
# \  = scape
"marca d' agua" == 'marca d\'agua'

"Teste \"funciona!"

texto = 'texto entre apostrófo pode ter "aspas" '
texto

doc1 = """ Texto de multiplas
 ...linhas"""
doc1

print('Texto com multiplas\n\t... linhas')
print(doc)

doc2 = ''' Texto...
linha'''
doc2

nome = 'Vitor Marconi'

nome[0]

nome[6]

nome[-7]

nome[5:] # Começando a string a partir do 5

nome[:5] # Oh index 5 n entra

nome[-7:] # Começando a partir do -7

#inicio ao fim
nome[2:5]

numeros = '12345678'

# Todos 
numeros [::]

#Numeros com step de 2 em 2
numeros [::2]

#Numeros começando do index 1 o resultado são os pares 
numeros[1::2]

numeros[::-1]

numeros[::-2]

nome [::-1]

"""--------------------------------------------------------------------------------"""

frase = 'Aprendendo python'

# Operador membro
'aprendendo' in frase
# False, pois a letra "A" está minuscula

"aprendendo" not in frase

#tamanho da frase
len(frase)

# Transformando a frase para letra minuscula 
frase.lower()

# Trasformando a frase para letra Maiuscula
frase.upper()

# Quebrando a frase com espaços em branco
frase.split()

# Quebrando e especificando 
frase.split('e')

#dir(str)
#help(str.center)

# Magic Methodos
# www.python-course/python3_magic_methodos.php

"""-------------------------------

# Listas

------------------------------------Lista#1-------------------------------------
"""

# Criando uma Lista
list = [] #vazia
type(list) # tipo 
#help(list)

# Em Python a lista é uma sequencia mutavel
# Aceita tipos heterogenios 
len(list) # tamanho

# Adicionando elementos na lista
list.append(1) 
list.append(5)
list

len(list)

# Nova Lista com dados heterogenios (não é o ideial)
lista = [1, 5, 'Ana', 'Bia']
lista

lista.remove(5) # Remove o iten escolido 
lista

lista.reverse() # Reverte a lista
lista

"""----------------------------Lista#2---------------------------------------------"""

# A lista é uma estrutura indexada
lista = [ 1, 5, 'Rebeca', 'Guilherme', 3.1415]
lista.index('Guilherme') # 'Guilherme' esta no indice 3

#lista.index(42) Vai dar erro pois n tem niguem nesse index

lista[2] # 'Rebeca' esta no index 2

1 in lista # Sim 1 percente a lista

'Pedro' not in lista

lista[0]

lista[4]

lista[-5]

"""----------------------------------------Lista#3---------------------------------"""

lista = ['Ana', 'Lia', 'Rui', 'Paulo', 'Vitor']
lista [1:3] # Começa do indice 1 ao 2, pois n iclui o 3
lista [1:-1]
lista [1:]
lista [:-1]
lista [::2]
lista [::-1]
del lista[2]
lista
del lista [:1]
lista

"""# TUPLA

Tupla é uma sequencia imutavel
"""

tupla = tuple()

tupla = ()

type(tupla)

#dir(tupla)

tupla = ('um') # igual a uma string
tupla = ('um',) # tipo tupla

type(tupla)

tupla[0]

#tupla [0] = 'novo' /// Não suporta atribuição de item

cores = ('amarelo', 'azul', 'vermelho', 'branco')
cores[0]
cores[1:]
cores[-1]

cores.index('amarelo')

cores.count('azul') # Quantos elementos desses possui na tulpa

len(cores)



"""#Dicionário"""

# Usamos {} para dicionário
pessoa = { 'nome' : 'Prof(a). Ana', 'idade' : 38, 'curso' : ['inglês', 'espanhol']}

type(pessoa)

pessoa

pessoa['nome']

pessoa ['idade']

pessoa ['curso']

pessoa ['curso'][1]

#pessoas[tags]

pessoa.keys() # Chaves do curso

pessoa.values() # Valores do dict

pessoa.items() # Pega todo o range

pessoa.get('idade')

pessoa.get('tags') # Não retorna nada

pessoa.get('tags', []) # Para conferir se não existe no dict

"""-----------------------------DICT#2----------------------------------------"""

pessoas = {'nome' : 'Prof Alberto', 'idade' : 43, 'cursos' : ['react', 'python']}
pessoas['idade'] = 44 # Alterando a idade
pessoas
pessoas['cursos'].append('Angular') # Adiciona um item ao dict
pessoas.pop('idade') # Excluindo o item
pessoas
pessoas.update({'idade':40, "sexo" : 'M'}) # Atualiza de add intens
pessoas
del pessoas['cursos'] # Deleta algum item
pessoas
pessoas.clear() # Limpa a o dict
pessoas

"""# Conjunto"""

# Não é indexado
# Não aceita repetição

a = {1, 2, 3}
type(a)

a = set('cod3r') # Executa cada uma das letras

print(a)

a = set('coddddddddd3') # Não repete as letras pois não aceita repetição
print(a)

print('3' in a, 4 not in a)

{1, 2, 3} == {3, 2, 1, 3}

# Operações
c1 = {1,2}
c2 = {2,3}

c1.union(c2)

c1.intersection(c2)

c1.update(c2)

c1

c2 <= c1

"""# Intepolação"""
