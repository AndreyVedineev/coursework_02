class Player:
    """ Игрок и угаданные им слова"""

    def __init__(self, name_user, words_used=[]):
        self.name_user = name_user  # имя пользователя
        self.words_used = words_used  # использованные слова пользователя - list()

    def __str__(self):
        return f'Я экземпляр класса: BasicWord\n' \
               f'Пользователь: {self.name_user},\n' \
               f'Использованные слова: ({", ".join(self.words_used)})'

    def __repr__(self):
        return f'name_user: {self.name_user},\n' \
               f'words_used: ({self.words_used})'

    def get_number_words_used(self):
        """Получение количества использованных слов (возвращает int)"""

        return int(len(self.words_used))

    def add_word_to_used_words(self, user_answer=None):
        """Добавление слова в использованные слова (ничего не возвращает)"""

        self.words_used.append(user_answer)

    def check_word_before(self, user_answer=None):
        """Проверка использования данного слова до этого (возвращает True, если слово не использовалось,
        можно добавлять!)."""

        if user_answer in self.words_used:
            return False
        return True
