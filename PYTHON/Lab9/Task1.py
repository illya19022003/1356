class Alphabet:
    def __init__(self):
        self._lang = 'Ua'
        self._letters = ['а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'є', 'ж', 'з', 'и', 'і', 'ї', 'й', 'к', 'л', 'м', 'н', 'о',
                         'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ю', 'я']

    def print_alphabet(self):
        alphabet = ''
        for i in self._letters:
            alphabet += i + ' '
        print(alphabet)

    def letters_num(self):
        print(len(self._letters))

    def is_ua_lang(self, text):
        text = text.replace(' ', '')
        text = text.lower()
        for i in text:
            if ''.join(self._letters).find(i) == -1:
                return False
        return True


class EngAlphabet(Alphabet):
    def __init__(self):
        self._lang = 'En'
        self._letters = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
        self._en_letters_num = len(self._letters.replace(' ', ''))

    def is_en_lang(self, text):
        text = text.replace(' ', '')
        text = text.lower()
        for i in text:
            if self._letters.find(i) == -1:
                return False
        return True

    def letters_num(self):
        print(self._en_letters_num)

    def _expample(self):
        print('hello my name is Vlad')


ukr = Alphabet()
ukr.print_alphabet()
ukr.letters_num()
text = 'привет'
print(ukr.is_ua_lang(text))

eng = EngAlphabet()
eng.print_alphabet()
print(eng.is_en_lang('J'))
print(eng.is_en_lang('Щ'))
eng.letters_num()
eng._expample()
