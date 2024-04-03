T = int(input())

for i in range(T):
    N, K = map(int, input().split())
    total_garrafas = N  # Começa com o número de garrafas compradas
    while N >= K:
        trocas = N // K  # Calcula quantas trocas completas são possíveis
        total_garrafas += trocas  # Adiciona as garrafas obtidas nas trocas
        N = trocas + (N % K)  # Atualiza o número de garrafas para a próxima iteração
        

    print(total_garrafas)