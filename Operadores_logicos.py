saldo_conta = 100;
saque = 2000;
limite_saque = 1000;

print("Seu saldo e de: ", saldo_conta);
if(saldo_conta < saque and saldo_conta == 0):
    print("Seu saque foi negado");
else:
    if(saldo_conta >= saque or limite_saque >= saque):
        print("Seu saque foi realizado");
    else:
        print("Seu saque foi negado")


print(not saque > limite_saque)