import sys 

class Forca(object):
    def __init__(self, word):
        self.word = word
        letters = self.letters = list(word)
        self.letter_len = letter_len = len(word)
        self.adiv = list("_"*letter_len)
        self.str_adiv = ' '.join(self.adiv)
    def letter(self, char):
        letter = self.letters
        adiv = self.adiv
        if not char in letter:
            return None
        while letter.count(char) != 0:
                p = letter.index(char)
                adiv[p] = char
                letter[p] = "."
        self.str_adiv = ' '.join(adiv)
        return True
    def word_kick(self, word_s):
        return word_s == self.word
    def re_word(self):
        return self.str_adiv

