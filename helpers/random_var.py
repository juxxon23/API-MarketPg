import random

class RandomVar:

    def do(file_name, categoria, arr):
        var = file_name[categoria][random.randint(-1, 4)]
        if var in arr:
            var = RandomVar.do(file_name, categoria, arr)
            arr = var
        else:
            arr = var
        return arr
