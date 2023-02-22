class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_matrix(self, matrix):
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                if matrix[i][j] != 0:
                    self.graph.append([i, j, matrix[i][j]])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def apply_union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def FindMinimumSpanningForest(self):
        result = []
        index, element = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for i in range(self.V):
            parent.append(i)
            rank.append(0)

        while element < self.V - 1:
            u, v, w = self.graph[index]
            index = index + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                element = element + 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
        sum = 0
        for u, v, weight in result:
            sum += weight
            print(f"{u} - {v}: {weight}")
        print(f"Итоговая длина: {sum}")

