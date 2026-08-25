import random

#matriz = [[0 for x in range(n)] for y in range(n)]


"""for i in range(n):
    for j in range(n):
        if j >i:
            matriz[i][j] = 1
        if i > j:
            matriz[i][j] = 1
        print(matriz[i][j], end=" ")
    print()
"""
def creat_tabuleiro(n):
    tabuleiro = random.sample(range(1,n + 1),n)
    return tabuleiro


def creat_tabu(n):
    matriz = [[0 for x in range(n)] for y in range(n)]
    return matriz

def print_tabu(tabu_list, n):
    print("Tabu List:")
    for i in range(n):
        print(tabu_list[i])

def update_tabu(tabu_list,n1,n2):
    TESTE = 7           #<--------------------------------------------------PARAMETRO 1
    tabu_list[n1][n2] = TESTE
    tabu_list[n2][n1] = tabu_list[n2][n1] + 1
    return tabu_list

def decrement_tabu(tabu_list,n):
    for i in range(n):
        for j in range(n):
            if (i<j and tabu_list[i][j] != 0):
                tabu_list[i][j] = tabu_list[i][j] - 1
    return tabu_list

def creat_neighbor(tabuleiro,n,tabu_list):
    
    available_moves = []

    for i in range(n):
        for j in range(i + 1 ,n): # pula o [0,0], [1,1], [2,2] e assim por diante
            if (i<j and tabu_list[i][j] == 0):
                available_moves.append((i,j))

    if len(available_moves) == 0:
        print("Criterio de inspiraçao ativo")
        menor1 = 10000
        posicao = [0,0]
        for i in range(n):
            for j in range(i): 
                if (tabu_list[i][j] < menor1):
                    menor1 = tabu_list[i][j]
                    posicao = (i,j)
        n1,n2 = posicao
    else: 
        n1, n2 = random.choice(available_moves)
    v1 = tabuleiro.copy()
    v1[n1],v1[n2] = v1[n2] , v1[n1]
    update_tabu(tabu_list, n1, n2)

    return v1

def fitness(tabuleiro,n):
    Dp = [0] * n
    Dn = [0] * n

    for i in range(n):
        Dp[i] = tabuleiro[i] - i
        Dn[i] = tabuleiro[i] + i

    fit = len(Dp) + len(Dn) - len(set(Dp)) - len(set(Dn))
    return fit

def n_queens(best_solution,n,tabu_list):

    #best_solution = random.sample(range(1,n + 1),n)

    print("Tabuleiro Inicial: ------------>", best_solution)

    n1 = creat_neighbor(best_solution,n,tabu_list)
    n2 = creat_neighbor(best_solution,n,tabu_list)
    n3 = creat_neighbor(best_solution,n,tabu_list)

    fit_tabuleiro = fitness(best_solution,n)
    print("Fitness Tabuleiro Inicial:", fit_tabuleiro)
    fit_n1 = fitness(n1,n)
    fit_n2 = fitness(n2,n)
    fit_n3 = fitness(n3,n)

    melhor_fitness = min(fit_n1, fit_n2, fit_n3)

    if melhor_fitness == fit_n1:
        best_solution = n1

    elif melhor_fitness == fit_n2:
        best_solution = n2

    else:
        best_solution = n3
    
    return best_solution,fitness(best_solution,n),tabu_list

#------------- MAIN ------------


n = 6
parada = 1000
final_fitness = 100
tabu_list = creat_tabu(n)
tabuleiro = creat_tabuleiro(n)
print("PRIMEIRO TABULEIRO: ", tabuleiro)
print ("Teste")

while parada != 0 and final_fitness > 0:
    print("----------------------------------------")
    tabu_list = decrement_tabu(tabu_list,n)
    
    tabuleiro,final_fitness,tabu_list = n_queens(tabuleiro,n,tabu_list)
    print("Final Fitness:", final_fitness)
    print("Parada:", parada)
    
    print_tabu(tabu_list, n)
    parada -= 1
