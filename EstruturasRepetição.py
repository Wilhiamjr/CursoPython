#São maneiras de interar dentro de um array ou alguma estrutura interavel

""" Exemplo for """

texto = input('Digite um texto');
vogais = 'AEIOU';

for letra in texto:
    if letra.upper() in vogais:
        print(letra);

""" For / else """

for letra in texto:
    if letra.upper() in vogais:
        print(letra)
else:
        print('Não existe vogal nesse texto')

""" Função Range """

#Range ex: range('Inicio','Fim','Step')

print(list(range(0,10,2)));


#For com range 
for list in range(11):
     print(list)


#while
     opcao = -1;
     opcao = int(input('Informe uma opção '))
     while opcao != 0:
          if opcao == 1:
               print('Opção 1')
               break
          elif opcao == 2:
                print('Opção 2')
                break
     else:
      print('nenhuma opção selecionada')
      break

               