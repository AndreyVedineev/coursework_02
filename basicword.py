class BasicWord:
    def __init__(self, original_word, set_subwords):
        self.original_word = original_word
        self.set_subwords = set_subwords

    def __repr__(self):
        return f'Слово: {self.original_word} набор допустимых подслов {", ".join(self.set_subwords)})'

    def checks_entered_word(self, user_answer):
        """проверку введенного слова в списке допустимых подслов (вернет bool),"""
        if user_answer in self.set_subwords:
            return True
        return False

    def counts_subwords(self):
        """подсчет количества подслов (вернет int)."""
        return int(len(self.set_subwords))


"""При инициализации ** экземпляру задаются: ** исходное слово ** и набор ** допустимых слов,
составленных из исходного."""

