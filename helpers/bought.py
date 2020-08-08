from .random_var import RandomVar
import json


class Bought:
    
    def save(self, file_name, categoria, cantidad):
        data_selected = []
        data = {}
        for i in range(0, cantidad):
            data_selected.append(RandomVar.do(file_name, categoria, data_selected))
        data[categoria] = data_selected
        with open("data/bought.json", "w") as data_out:
            json.dump(data, data_out, indent=2)
        return 'saved'
