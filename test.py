from nltk.corpus import stopwords
import random, sys

class generate:

    def __init__(self, len):

        self.max_len = len
        self.__main__()

    def _lent(self, str):
        self.counter = 0
        for i in str:
            self.counter += 1
            return self.counter
    
    def __main__(self):

        self.word_list = []
        
        for words in open(r'C:\xampp\htdocs\python\docgen\word-list-1.txt', 'r'):
                
            if self._lent(words) >= 6:
                self.word_list.append(words.replace('\n', ''))

        self._gen()


    def _gen(self):

        self.text = []
        count = 1

        for i in range(self.max_len):

            count += 2
            words = self.word_list
            
            self.text.append((random.choice(words)))
            stopWords = set(stopwords.words('english'))
            self.text.insert(count - 2, random.choice(list(stopWords)))
                
        res = ' '.join(self.text)
        print(res)

    

generate(200)


