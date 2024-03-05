""" Metodos uteis para manipular strings em python """

exemplo = 'PHytOn'
#LowerCase
print(exemplo.lower());

#UpperCase
print(exemplo.upper());

#Title
print(exemplo.title());

""" Eliminar espaços em brancos das strings  """

exemplo = "      Phyton       "

#Strip Remove todos os espaços em branco
print(exemplo.strip());

#lstrip Remove todos os espaços em branco do lado esquerdo 
print(exemplo.lstrip());

#rstrip remove todos os espaços em branco do lado direito 
print(exemplo.rstrip());

""" Junções e Centralizações """

exemplo = "Python"

#Centralização
print(exemplo.center(10,"#"))

#Junção 
print(".".join(exemplo))

""" Interpolação de variáveis  """

# Existe varias formas de interpolar mais a que eu achei mais adequada e mais utilizada é a seguinte
nome =  "Wilhiam"
Sobrenome = "Junior"
idade = 28.0

print(f"Seu nome é {nome} e seu sobre nome é {Sobrenome} sua idade é {idade: 0.0f}")

""" Fatiamento de string """

nome = 'Wilhiam Junior';

print(nome[0]);
print(nome[0:10]);
print(nome[0:10:2]);
print(nome[::-1]);
