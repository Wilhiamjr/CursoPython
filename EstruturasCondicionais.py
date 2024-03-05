""" Estrutura de condicional não possiu caracteres para abertura e fechamento dos blocos,
utiliza-se a identação para definir o inicio e fim . """
#Blocos de identação
saldo=0;
def sacar(valor)->None:
    if valor >= saldo:
        print('Não possui saldo')

sacar(1);

#Estrutura condicionais
if saldo > 1:
    print('Possui saldo')
if saldo < 1 :
    print('Não possui saldo')

if saldo > 1:
    print('Tem saldo')
else:
    print('Não tem saldo')

opcao = int(input('Digite [1] para ver saldo ou [2] para ver extrato'))

if opcao == 1:
    print('Seu saldo é ', saldo);
elif opcao == 2:
    print('Seu extrato é', saldo);
else:
    print('Opção inválida');