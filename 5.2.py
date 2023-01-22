import json

class Model:
    title = 'Создание класса Model'
    text = 'Создание словаря со всеми значениями атрибутов класса'
    autor = 'Александр'
    def save(self):
        dct = {k: str(v) for k, v in vars(Model).items()}
        with open('1.json', 'w', encoding='utf-8') as fout:
            json.dump(dct, fout)

obj = Model()
obj.save()





