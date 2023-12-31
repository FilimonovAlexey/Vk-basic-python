# Необходимо написать программу, которая будет считывать со стандартного ввода строку. 
# Нужно разбить строку на слова, словом будем считать последовательность символов отличных от 
# пробелов (то есть знаки пунктуации будут входить в слова). Далее нужно посчитать сколько каждое 
# слово встречалось в тексте и вывести наиболее часто слово и сколько оно встретилось. Все слова нужно 
# также приводить к нижнему регистру при подсчете. Гарантируется, что в тексте самое частое слово – единственное.

import re
from collections import Counter

# Считываем строку со стандартного ввода
input_str = input()

# Разбиваем строку на слова, приводим их к нижнему регистру
words = re.findall(r'\w+', input_str.lower())

# Подсчитываем количество вхождений каждого слова
word_counts = Counter(words)

# Находим наиболее часто встречающееся слово и его количество вхождений
most_common_word, count = word_counts.most_common(1)[0]

print(f"{most_common_word} {count}")