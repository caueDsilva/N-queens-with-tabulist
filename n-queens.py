import random
import time
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
    TESTE = 22           #<--------------------------------------------------PARAMETRO 1
    tabu_list[n1][n2] = TESTE
    tabu_list[n2][n1] = tabu_list[n2][n1] + 1
    return tabu_list

def decrement_tabu(tabu_list,n):
    for i in range(n):
        for j in range(n):
            if (i<j and tabu_list[i][j] != 0):
                tabu_list[i][j] = tabu_list[i][j] - 1
    return tabu_list

def creat_neighbor(n,tabu_list):
    
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

    #v1 = tabuleiro.copy()
    #v1[n1],v1[n2] = v1[n2] , v1[n1]
    #update_tabu(tabu_list, n1, n2)

    return n1,n2

def fitness(tabuleiro,n):
    Dp = [0] * n
    Dn = [0] * n

    for i in range(n):
        Dp[i] = tabuleiro[i] - i
        Dn[i] = tabuleiro[i] + i

    fit = len(Dp) + len(Dn) - len(set(Dp)) - len(set(Dn))
    return fit

# x = quantidade de vizinho q vai criar
def n_queens(best_solution,n,tabu_list,x):


    print("Tabuleiro Inicial: ------------>", best_solution)
    fit_tabuleiro = fitness(best_solution,n)

    print("Fitness Tabuleiro Inicial:", fit_tabuleiro)
    melhor_fitness = float("inf")
    best_position = None
    melhor_tabuleiro = None

    neighbor = []
    for _ in range(x):
        movimento = creat_neighbor(n, tabu_list)
        neighbor.append(movimento)

    for p1,p2 in neighbor:
        vizinho = best_solution.copy()

        vizinho[p1], vizinho[p2] = vizinho[p2], vizinho[p1]

        fit_vizinho = fitness(vizinho, n)

        if fit_vizinho < melhor_fitness:

            melhor_fitness = fit_vizinho
            best_position = (p1, p2)
            melhor_tabuleiro = vizinho
            

    p1,p2 = best_position
    update_tabu(tabu_list,p1,p2)

    return melhor_tabuleiro,melhor_fitness,tabu_list

#------------- MAIN ------------


n = 20
x = 8 #----------------------------> numero de vizinhos gerados
parada = 1000
final_fitness = 100 # max = 0 / min = 100
tabu_list = creat_tabu(n)
tabuleiro = creat_tabuleiro(n)
print("PRIMEIRO TABULEIRO: ", tabuleiro)
print ("Teste")

inicio = time.perf_counter()

while parada != 0 and final_fitness > 0:
    print("----------------------------------------")
    tabu_list = decrement_tabu(tabu_list,n)
    
    tabuleiro,final_fitness,tabu_list = n_queens(tabuleiro,n,tabu_list,x)
    print("Final Fitness:", final_fitness)
    print("Parada:", parada)
    
    print_tabu(tabu_list, n)
    parada -= 1

fim = time.perf_counter()
temp = fim - inicio

print("----------------------------------------")
print("Final Fitness:", final_fitness)
print (f"Tempo de execuçao: {temp:.6f} segundos")
print("----------------------------------------")
