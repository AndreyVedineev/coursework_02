from utils import create_random_word, statistics, creates_player, load_file

PATH = "https://www.jsonkeeper.com/b/7SGM"  # путь к списку слов
count = 0  # счетчик угаданных слов


def check(subword):
    """
    Проверка длины введенного слова - не менее 3 символов, нет такого слова или слово уже угадано.
    :param subword:
    :return: boolean
    """
    if len(subword) < 3:
        print('Слишком короткое слово.')
        return True
    if not basicword.checks_entered_word(subword):
        print('Нет такого слова')
        return True
    if subword in player.words_used:
        print('Уже использовано')
        return True
    else:
        return False


if __name__ == '__main__':
    while True:
        name_user = input('Введите имя игрока_:')
        if name_user is not "":
            break
        else:
            print("Вы не указали имя! Повторите!")

    player = creates_player(name_user)
    print(f'Привет, {player.name_user}')

    basicword = create_random_word(load_file(PATH))

    print(f'Составьте {len(basicword.set_subwords)} слов из слова {basicword.original_word.upper()}.')
    print('Слова должны быть не короче 3 букв.\n'
          'Чтобы закончить игру, угадайте все слова или напишите "stop".\n'
          'Поехали, ваше первое слово?')

    while count <= len(basicword.set_subwords) - 1:

        user_subword = input("Слово_:").lower().strip()

        if user_subword in ["stop", "стоп"]:
            break

        if check(user_subword):
            continue

        print('Верно')
        player.words_used.append(user_subword)
        count += 1

    statistics(player)
