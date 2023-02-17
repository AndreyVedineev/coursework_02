class BasicWord:
    def __init__(self, original_word, set_subwords):
        self.original_word = original_word
        self.set_subwords = set_subwords

    def __repr__(self):
        return f'Я экземпляр класса: BasicWord\n' \
               f' Слово: {self.original_word}. Набор допустимых подслов:({", ".join(self.set_subwords)})'

    def checks_entered_word(self, user_answer):
        """проверку введенного слова в списке допустимых подслов,"""
        if user_answer in self.set_subwords:
            return True
        return False

    def counts_subwords(self):
        """подсчет количества подслов (вернет int)."""
        return int(len(self.set_subwords))


# ac = "строка"
# bc = ["акр", "акт", "кот", "рак", "орк", "оса", "сок", "ток", "тор", "кора", "коса", "сота", "торс", "роса", "скат"]
# basicword = BasicWord(ac, bc)
# print(basicword.checks_entered_word('кот'))
#
# """При инициализации ** экземпляру задаются: ** исходное слово ** и набор ** допустимых слов,
# составленных из исходного."""
