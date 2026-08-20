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
    tabuleiro = [0] * n
    return tabuleiro


def creat_tabu(n):
    matriz = [[0 for x in range(n)] for y in range(n)]
    return matriz

def print_tabu(tabu_list, n):
    print("Tabu List:")
    for i in range(n):
        print(tabu_list[i])

def update_tabu(tabu_list,n1,n2):
    TESTE = 4           #<--------------------------------------------------PARAMETRO 1
    tabu_list[n1][n2] = 6
    tabu_list[n2][n1] = tabu_list[n2][n1] + 1
    return tabu_list

def decrement_tabu(tabu_list,n):
    for i in range(n):
        for j in range(n):
            if (i<j and tabu_list[i][j] != 0):
                tabu_list[i][j] = tabu_list[i][j] - 1
    return tabu_list

def creat_neighbor(tabuleiro,n,tabu_list):
    
    while True:
        n1,n2 = random.sample(range(n), 2)

        if (tabu_list[n1][n2] == 0):

            v1 = tabuleiro.copy()

            aux = v1[n1]
            v1[n1] = v1[n2]
            v1[n2] = aux
            update_tabu(tabu_list,n1,n2)
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

    
    best_solution = random.sample(range(1,n + 1),n)

    print("Tabuleiro Inicial: ------------>", best_solution)

    n1 = creat_neighbor(best_solution,n,tabu_list)
    n2 = creat_neighbor(best_solution,n,tabu_list)
    n3 = creat_neighbor(best_solution,n,tabu_list)

    fit_tabuleiro = fitness(best_solution,n)
    print("Fitness Tabuleiro Inicial:", fit_tabuleiro)
    fit_n1 = fitness(n1,n)
    fit_n2 = fitness(n2,n)
    fit_n3 = fitness(n3,n)

    if (fit_n1 < fit_tabuleiro):
        best_solution = n1
        print("Tabuleiro n1:", best_solution)
    elif (fit_n2 < fit_tabuleiro):
        best_solution = n2
        print("Tabuleiro n2:", best_solution)
    elif (fit_n3 < fit_tabuleiro):
        best_solution = n3
        print("Tabuleiro n3:", best_solution)
    elif (fit_n1 == fit_tabuleiro):
        best_solution = n1
        print("Tabuleiro n1:", best_solution)
    elif (fit_n2 == fit_tabuleiro):
        best_solution = n2
        print("Tabuleiro n2:", best_solution)
    elif (fit_n3 == fit_tabuleiro):
        best_solution = n3
        print("Tabuleiro n3:", best_solution)


    return best_solution,fitness(best_solution,n),tabu_list

#------------- MAIN ------------


n = 6
parada = 100
final_fitness = 100
tabu_list = creat_tabu(n)
tabuleiro = creat_tabuleiro(n)
print ("oiu")

while parada != 0 and final_fitness >= 0:
    print("----------------------------------------")
    tabu_list = decrement_tabu(tabu_list,n)
    
    tabuleiro,final_fitness,tabu_list = n_queens(tabuleiro,n,tabu_list)
    print("Final Fitness:", final_fitness)
    print("Parada:", parada)
    
    print_tabu(tabu_list, n)
    parada -= 1
