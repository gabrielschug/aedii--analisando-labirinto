from collections import deque
import heapq

#===> 1. CRIANDO LABIRINTO <==============================================================

labirinto = [
  "I.........", 
  ".########.", 
  "....#.....", 
  ".##.#.###.", 
  "....#.....", 
  ".####.###.", 
  "......#...", 
  ".#########", 
  "..........", 
  "########.F",
]

def achar (lab, simbolo):
  for i, linha in enumerate(lab):
    if simbolo in linha:
      return (i, linha.index(simbolo))

inicio = achar(labirinto, "I")
saida = achar(labirinto, "F")

DIRECOES = [(-1, 0), (0, 1), (1, 0), (0, -1)] # ↑ → ↓ ←
def livre(lab, i, j):
  dentro = 0 <= i < len(lab) and 0 <= j < len(lab[0])
  return dentro and lab[i][j] != '#'

def montar_grafo(lab):
  grafo = {}
  for i in range(len(lab)):
    for j in range(len(lab[0])):
      if not livre(lab, i, j):
        continue  
      grafo[(i, j)] = []
      for di, dj in DIRECOES:
        if livre(lab, i + di, j + dj):
          grafo[(i, j)].append((i + di, j + dj))
  return grafo

grafo = montar_grafo(labirinto)

def desenhar(lab, caminho):
  grade = [list(linha) for linha in lab]
  for i, j in caminho:
    if grade[i][j] == '.':
      grade[i][j] = '*'
  for linha in grade:
    print(''.join(linha))


#===> 2. IMPLEMENTANDO DFS, BFS E BUSCA GULOSA <==========================================

def busca_profunda(grafo, inicio, saida):
  visitados = set()
  antecessor = {inicio: None}

  def dfs(atual):
    visitados.add(atual)
    if atual == saida:
      return True
    for vizinho in grafo[atual]:
      if vizinho not in visitados:
        antecessor[vizinho] = atual
        if dfs(vizinho):
          return True
    return False

  if inicio not in grafo or saida not in grafo or not dfs(inicio):
    return [], visitados

  caminho = []
  atual = saida
  while atual is not None:
    caminho.append(atual)
    atual = antecessor[atual]
  caminho.reverse()
  return caminho, visitados

def busca_camadas(grafo, inicio, saida): 
  if inicio not in grafo or saida not in grafo:
    return [], set()

  visitados = {inicio}
  fila = deque([inicio])
  antecessor = {inicio: None}
  while fila:
    v = fila.popleft()
    if v == saida:
      caminho = []
      atual = v
      while atual is not None:
        caminho.append(atual)
        atual = antecessor[atual]
      caminho.reverse()  
      return caminho, visitados
    for w in grafo[v]:
      if w not in visitados:
        visitados.add(w)
        antecessor[w] = v
        fila.append(w)
  return [], visitados

def busca_gulosa(grafo, inicio, saida):
  if inicio not in grafo or saida not in grafo:
    return [], set()

  def heuristica(posicao):
    return abs(posicao[0] - saida[0]) + abs(posicao[1] - saida[1])

  fronteira = [(heuristica(inicio), inicio)]
  visitados = set()
  antecessor = {inicio: None}

  while fronteira:
    _, atual = heapq.heappop(fronteira)
    if atual in visitados:
        continue
    visitados.add(atual)

    if atual == saida:
        caminho = []
        while atual is not None:
          caminho.append(atual)
          atual = antecessor[atual]
        caminho.reverse()
        return caminho, visitados

    for vizinho in grafo[atual]:
        if vizinho not in visitados and vizinho not in antecessor:
          antecessor[vizinho] = atual
          heapq.heappush(fronteira, (heuristica(vizinho), vizinho))

  return [], visitados


#===> 3. COMPARANDO CAMINHOS & CASAS VISITADAS <==========================================

# BUSCA POR CAMADAS
caminho_bfs, visitados_bfs = busca_camadas(grafo, inicio, saida)
print("=== RESULTADO DA BFS ===")
print(f"Caminho encontrado ({len(caminho_bfs)} passos): {caminho_bfs}")
print(f"Total de casas visitadas: {len(visitados_bfs)}")
print("Desenho do Labirinto com o caminho (*):")
desenhar(labirinto, caminho_bfs)


# BUSCA POR PROFUNDIDADE
caminho_dfs, visitados_dfs = busca_profunda(grafo, inicio, saida)
print("=== RESULTADO DA DFS ===")
print(f"Caminho encontrado ({len(caminho_dfs)} passos): {caminho_dfs}")
print(f"Total de casas visitadas: {len(visitados_dfs)}")
print("Desenho do Labirinto com o caminho (*):")
desenhar(labirinto, caminho_dfs)

# BUSCA GULOSA
caminho_gulosa, visitados_gulosa = busca_gulosa(grafo, inicio, saida)
print("=== RESULTADO DA BUSCA GULOSA ===")
print(f"Caminho encontrado ({len(caminho_gulosa)} passos): {caminho_gulosa}")
print(f"Total de casas visitadas: {len(visitados_gulosa)}")
print("Desenho do Labirinto com o caminho (*):")
desenhar(labirinto, caminho_gulosa)