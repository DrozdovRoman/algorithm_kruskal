import os
from pathlib import Path


def read_matrix(path, sizeof):
    result = []
    with open(path, "r") as textFile:
        for element in textFile:
            if len(element) > sizeof:
                element = [int(i) if i.isdigit()
                           else 0 for i in element[sizeof]]
            elif len(element) < sizeof:
                element = [int(element[i]) if i.isdigit() and i < len(element)
                           else 0 for i in range(sizeof)]
            result.append(element)
    print(result)


def file_exist(path, format):
    if os.path.exists(path) and Path(path).suffix == format:
        return True
    else:
        return False
