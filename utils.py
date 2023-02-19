import random

import requests

from basicword import BasicWord
from player import Player


def load_file(path):
    """ Получает список слов с внешнего ресурса https://www.jsonkeeper.com/b/7SGM.

    :param path: https://www.jsonkeeper.com/b/7SGM.
    :return: list
    """

    response = requests.get(path)
    return response.json()


def create_random_word(file):
    """
    получает список слов, выберет случайное слово, создает экземпляр класса `BasicWord,
    :param file:
    :param path:list
    :return:basicword
    """
    random_index = random.randint(0, len(file) - 1)
    original_word = file[random_index]['word']
    set_subwords = file[random_index]['subwords']

    return BasicWord(original_word, set_subwords)


def creates_player(name_user):
    """ Создает экземпляр игрока"""

    player = Player(name_user)
    return player


def statistics(player):
    print(f'Игра завершена, вы угадали {len(player.words_used)} слов!')
