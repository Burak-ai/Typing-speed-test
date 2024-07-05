import random
import time
import nltk
from nltk.corpus import words

# Download the nltk words corpus if not already downloaded
nltk.download('words')
word_list = words.words()

def generate_random_phrase():
    random_words = random.sample(word_list, 10)
    return ' '.join(random_words)

string = generate_random_phrase()
word_count = len(string.split())

def createbox():
    print()
    print('Enter the phrase as fast as possible and with accuracy')
    print()

while True:
    t0 = time.time()
    createbox()
    print(string, '\n')
    inputText = input()
    t1 = time.time()
    
    lengthOfInput = len(inputText.split())
    accuracy = len(set(inputText.split()) & set(string.split()))
    accuracy = (accuracy / word_count)
    timeTaken = (t1 - t0)
    wordsperminute = (lengthOfInput / timeTaken) * 60

    
    print('Total words \t :', lengthOfInput)
    print('Time used \t :', round(timeTaken, 2), 'seconds')
    print('Your accuracy \t :', round(accuracy, 3) * 100, '%')
    print('Speed is \t :', round(wordsperminute, 2), 'words per minute')
    
    print("Do you want to retry (yes or no)? ", end='')
    retry = input().strip().lower()
    if retry == 'yes':
        string = generate_random_phrase()
        word_count = len(string.split())
        continue
    else:
        print('Thank you, bye bye.')
        time.sleep(1.5)
        break
