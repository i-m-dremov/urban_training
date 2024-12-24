#Задача "Найдёт везде"

class WordsFinder:

    def __init__(self, *name):
        self.file_names = (name)

    def get_all_words(self):
        all_words = {}
        punctuation_ = ',''.''=''!''?'';'':''-'
        for file in self.file_names:
            with open(file, encoding = 'utf-8') as all_files:
                all_files = all_files.read().lower().translate(str.maketrans('', '', punctuation_)).split()
                all_words.update({file: all_files})
        return all_words

    def find(self, word):
        word_index = {}
        self.word = word
        for name, words in self.get_all_words().items():
            word_index.update({name: words.index(self.word.lower())+1})
        return word_index

    def count(self, word):
        word_count = {}
        self.word = word
        for name, words in self.get_all_words().items():
            word_count.update({name: words.count(self.word.lower())})
        return word_count

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова {'test_file.txt': ["it's", 'a', 'text', 'for', 'task',
                                #'найти', 'везде', 'используйте', 'его', 'для',
                                #'самопроверки', 'успехов', 'в', 'решении', 'задачи', 'text', 'text', 'text']}
print(finder2.find('TEXT')) # 3 слово по счёту {'test_file.txt': 3}
print(finder2.count('teXT')) # 4 слова teXT в тексте всего {'test_file.txt': 4}

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))



