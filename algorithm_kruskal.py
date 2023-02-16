def FindMinimumSpanningForest(matrix):
    arr = []
    result = []
    relation = [i for i in range(1, len(matrix) + 1)]
    for i in range(len(matrix)):
        for j in range(i+1, len(matrix)):
            if matrix[i][j] != 0:
                arr.append([[i, j], matrix[i][j]])
    arr.sort(key=lambda item: item[1])
    while (len(result) != len(matrix) - 1):
        if relation[arr[0][0][0]] != relation[arr[0][0][1]]:
            for i in range(len(relation)):
                if relation[i] == relation[arr[0][0][1]]:
                    relation[i] = relation[arr[0][0][0]]
            result.append(arr.pop(0))
        else:
            del arr[0]
    print("Минимальное остовное дерево")
    for element in result:
        print(element[0][0] + 1, "-", element[0][1] + 1, " : ", element[1])
