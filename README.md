# Resolução do Labirinto com Buscas em Grafos (AED II)

Projeto desenvolvido para a disciplina de Algoritmos e Estruturas de Dados II (UniSENAC Pelotas) ministrada pelo Prof. Pablo De Chiaro.

## 📌 Descrição do Labirinto

Foi modelado um labirinto $10 \times 10$ no formato de grade (matriz de caracteres), onde cada casa livre é tratada como um vértice de um grafo não-dirigido e sem pesos.

O mapa conta com uma **barreira central de paredes** e duas opções de trajetos a partir do início `I` (0,0) até a saída `F` (9,9):
<img width="1573" height="587" alt="image" src="https://github.com/user-attachments/assets/ccfdb96f-a224-4b5d-8874-679d2776d15c" />


## 📊 Tabela Comparativa dos Algoritmos

| Algoritmo | Estrutura de Dados | Passos no Caminho | Casas Visitadas | Garante Menor Caminho? |
| :--- | :--- | :--- | :--- | :--- |
| **BFS (Largura)** | Fila (`collections.deque` - FIFO) | **19 passos** | **59 casas** | **Sim** |
| **DFS (Profundidade)** | Pilha (Recursão / LIFO) | **37 passos** | **58 casas** | **Não** |
| **Gulosa (Greedy)** | Fila de Prioridade (`heapq`) | **37 passos** | **46 casas** | **Não** |

## 🧠 Análise dos Resultados e Defesa Oral

1. **Por que a BFS encontrou o menor caminho e a DFS não?**
   * A **BFS (Breadth-First Search)** explora o grafo em "camadas concêntricas" de distância (raio de expansão). Por desempilhar sempre por ordem de chegada (FIFO), ela varre todas as possibilidades de 1 passo, depois 2 passos, até atingir o objetivo. Isso garante matematicamente a menor rota (19 passos).
   * A **DFS (Depth-First Search)** engata em uma única ramificação e avança o mais fundo possível até bater em uma parede. Como a primeira ramificação percorrida foi a do topo, ela encontrou um caminho válido até a saída e encerrou a busca, entregando uma rota mais longa (23 passos).

2. **Em que ponto a Busca Gulosa foi induzida ao caminho inadequado?**
   * A **Busca Gulosa** utiliza a distância de Manhattan ($h = |x_1 - x_2| + |y_1 - y_2|$) como heurística. No nó inicial `(0,0)`, os vizinhos na linha 0 apresentavam valores de $h$ decrescentes em relação à saída `(9,9)`. A "bússola" da heurística atraiu o algoritmo para a direita, fazendo-o cair na armadilha da barreira central e forçando-o a fazer o trajeto longo de 23 passos.
