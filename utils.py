import random
import requests


from player import Player


from basicword import BasicWord


def load_random_word(path):
    """
    получает список слов, выберет случайное слово, создает экземпляр класса `BasicWord,
    :param path:с внешнего ресурса https://www.jsonkeeper.com/b/7SGM.
    :return:basicword
    """
    response = requests.get(path)
    data_json = response.json()
    random_index = random.randint(0, len(data_json) - 1)
    original_word = data_json[random_index]['word']
    set_subwords = data_json[random_index]['subwords']
    basicword = BasicWord(original_word, set_subwords)

    return basicword


def statistics():
    pass



