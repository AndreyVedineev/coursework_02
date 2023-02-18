from utils import load_random_word, statistics, creates_player

PATH = "https://www.jsonkeeper.com/b/7SGM"  # путь к списку слов

if __name__ == '__main__':

    name_user = input('Введите имя игрока_:')
    player = creates_player(name_user)
    print(f'Привет, {player.name_user}')
    basicword = load_random_word(PATH)

    print(f'Составьте {len(basicword.set_subwords)} слов из слова {basicword.original_word.upper()}.')
    print('Слова должны быть не короче 3 букв.\n'
          'Чтобы закончить игру, угадайте все слова или напишите "stop".\n'
          'Поехали, ваше первое слово?')

    count = 0

    while count <= len(basicword.set_subwords) - 1:

        user_subword = input("Слово_:").lower().strip()

        if user_subword in ["stop", "стоп"]:
            break
        if len(user_subword) < 3:
            print('Слишком короткое слово.')
            continue
        if not basicword.checks_entered_word(user_subword):
            print('Неверно')
            continue
        if user_subword in player.words_used:
            print('Уже использовано')
            continue

        print('Верно')
        player.words_used.append(user_subword)
        count += 1

    statistics(player)
