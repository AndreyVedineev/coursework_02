
from player import Player
from utils import load_random_word

PATH = "https://www.jsonkeeper.com/b/7SGM"  # путь к списку слов

if __name__ == '__main__':
    name_user = input('Введите имя игрока_:')
    player = Player(name_user)
    print(f'Привет, {player.name_user}')

    basicword = load_random_word(PATH)

    original_word = basicword.original_word.upper()

    print(f'Составьте {len(basicword.set_subwords)} слов из слова {original_word}.')
    print('Слова должны быть не короче 3 букв.')
    print('Чтобы закончить игру, угадайте все слова или напишите "stop".')
    print('Поехали, ваше первое слово?')
    a = 0
    while a < len(basicword.set_subwords) :
        user_subword = input("Слово_:")
        if len(user_subword) < 3:
            print('Слишком короткое слово.')
            continue
        if not basicword.checks_entered_word(user_subword):
            print('Неверно')
            continue
        if user_subword in player.words_used:
            print('Уже использовано')
            continue




