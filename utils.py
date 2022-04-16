import json


def candidates():
    '''
    Из файла json возвращает список словарей.
    '''

    with open('candidates.json', 'r', encoding='utf8') as file:
        candidat = json.load(file)
        return candidat
