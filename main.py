from nltk.corpus import stopwords
import random, sys, time, logging
import pathlib, os, nltk
from colorama import Fore, Back, Style
from pathlib import Path
from os import system, name
from urllib.request import urlopen
nltk.download('stopwords') 

def lent(self, str):
    counter = 0
    for i in str:
            
        counter += 1
        return counter

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

class generate:

    def __init__(self, amount):

        logging.basicConfig(
            level=logging.INFO,
            format='\r' + Fore.GREEN + '[%(asctime)s] Worker: ' + Style.RESET_ALL + '%(message)s', datefmt="%H:%M:%S"
        )

        self.max_len = 230
        self.max_amount = 1000
        self.amount = int(amount)

        if self.amount > self.max_amount:
            print('[!] Max Limit Exceeded: 1000\n(To Prevent Crashing)\n')
            exit()

        self.cdir = pathlib.Path(__file__).parent.resolve()
        self.newpath = r'%s\doc-files'%self.cdir
        if not os.path.exists(self.newpath):
            logging.info('Generating Directory')
            os.makedirs(self.newpath)
        self.dir = self.newpath


        self.__main__()
    
    

    def __main__(self):

        logging.info('Loading Wordlist')

        self.word_list = []
        dir = r'%s\word-list-1.txt'%self.cdir

        for words in open(dir, 'r'):
            if len(words) >= 6:
                self.word_list.append(words.replace('\n', ''))

        self.__mass__()


    def __title__(self):
        html = urlopen("https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english-usa-no-swears-long.txt")
        list = []
        for i in html:
            if i not in list:
                list.append(i.decode('utf-8').replace('\n', ''))
        subject = random.choice(list)

        return subject


    def __gen__(self):

        self.text = []
        count = 1

        for i in range(230):

            count += 2
            words = self.word_list
            
            self.text.append((random.choice(words)))
            stopWords = set(stopwords.words('english'))
            self.text.insert(count - 2, random.choice(list(stopWords)))
                
        sentences = ' '.join(self.text)
        return sentences


    def __save__(self):

        self._sub = self.__title__()
        content = self.__gen__()
        content1 = self.__gen__()
        
        with open(r"%s\%s.doc"%(self.dir, self._sub), "w") as f:
            f.write(content)
            f.write('\n\n')
            f.write(content1)

    def __mass__(self):

        logging.info('Generating Documents:')
        count = 0 
        
        for i in range(self.amount):
            count += 1
            self.__save__()
            print('\t           [+%s] Document: Generated'%(count))
            if count >= self.amount:
                logging.info('Documents Generated Successfully\n')

def loader():
    
    banner = ("""
███████╗    ██╗         ██╗   ██╗    ██╗  ██╗    ██╗   ██╗    ███████╗
██╔════╝    ██║         ╚██╗ ██╔╝    ╚██╗██╔╝    ██║   ██║    ██╔════╝
█████╗      ██║          ╚████╔╝      ╚███╔╝     ██║   ██║    ███████╗
██╔══╝      ██║           ╚██╔╝       ██╔██╗     ██║   ██║    ╚════██║
███████╗    ███████╗       ██║       ██╔╝ ██╗    ╚██████╔╝    ███████║
╚══════╝    ╚══════╝       ╚═╝       ╚═╝  ╚═╝     ╚═════╝     ╚══════╝
                                                                      """)
                                                                      
    try:
        for col in banner:
            print(Fore.GREEN + col, end="")
            sys.stdout.flush()
            time.sleep(0.008)
        print(Style.RESET_ALL)
        print(Fore.GREEN + 'Contact me on Telegram: @elyxus' + Style.RESET_ALL)
    except KeyboardInterrupt:
        clear()
        print(Style.RESET_ALL + '[+] Program Exited')
        exit()

if __name__ == '__main__':
    clear()
    try:
        val = input('\n[+] Amount of Doc to Gen: ')
        try:
            value = int(val)
            if isinstance(value, int):
                generate(int(val))
        except ValueError:
            print('Enter a Valid Number!')
            exit()
    except KeyboardInterrupt:
            print(Style.RESET_ALL + '[+] Program Exited')
		
