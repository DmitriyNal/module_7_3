import string
class  WordsFinder:
    def __init__(self,*file_names):
        self.file_names = file_names

    def __str__(self):
        print(f'Имя файла : {self.file_names}')

    def get_all_words(self):
        all_words = {}
        for name_text in self.file_names:
            with open(name_text, 'r', encoding='utf-8') as file:
                words = []
                for line in file.readlines():

                    line = line.translate(str.maketrans('', '', string.punctuation)).replace('-', ' ').split()
                    words.extend(line)
                    all_words[name_text] = words
                return all_words


    def find(self, word):# найти слово в словаре
        dictionary1 ={}
        for name, words in self.get_all_words().items():
            dictionary1[name] = words.index(word.lower())+1
            return dictionary1


    def count(self, word):# #количество слов
        dictionary2 = {}
        for name, words in self.get_all_words().items():
            dictionary2[name] = words.count(word.lower())
            return dictionary2

if __name__ == '__main__':
    finder2 = WordsFinder('test_file.txt')
    finder2.__str__()  # Имя файла
    print(finder2.get_all_words())  # Все слова
    print(finder2.find('TEXT'))  # 3 слово по счёту
    print(finder2.count('teXT'))  # 4 слова teXT в тексте всего

























