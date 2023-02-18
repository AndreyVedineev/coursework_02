class Player:
    def __init__(self, name_user, words_used=[]):
        self.name_user = name_user  # имя пользователя
        self.words_used = words_used  # использованные слова пользователя - list()

    def __repr__(self):
        return f'Пользователь: {self.name_user},\n' \
               f'Использованные слова: ({", ".join(self.words_used)})'

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

#
# word = ["пони", "тон", "ион", "опт", "пот", "топ", "пион", "тип"]
# pl_1 = Player("Vasay", word)
# print(pl_1)
# print(pl_1.get_number_words_used())
#
# print(pl_1)
# print(pl_1.check_word_before("тип"))