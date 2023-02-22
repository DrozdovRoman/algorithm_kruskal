from prettytable import PrettyTable
from copy import deepcopy
from init_matrix import file_exist, read_matrix
from algorithm_kruskal import Graph

if __name__ == "__main__":
    path = "matrix.txt"
    format = ".txt"
    matrixSize = 9
    if file_exist(path=path, format=format):
        matrix = PrettyTable()
        matrix.field_names = ["Graph"] + [i + 1 for i in range(matrixSize)]
        rows = read_matrix(path, matrixSize)
        rowsPrint = deepcopy(rows)
        for i in range(len(rowsPrint)):
            rowsPrint[i] = [i + 1] + rowsPrint[i]
        matrix.add_rows(rowsPrint)
        print("Матрица смежности\n", matrix, sep="")
        print("Краскала")
        graph = Graph(matrixSize)
        graph.add_matrix(rows)
        graph.FindMinimumSpanningForest()
    else:
        print("File not found.")
