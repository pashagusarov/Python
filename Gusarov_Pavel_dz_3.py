"""
1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
"""

def num_translate(num):
    numbers = {"zero": "ноль",
               "one": "один",
               "two": "два",
               "three": "три",
               "four": "четыре",
               "five": "пять",
               "six": "шесть",
               "seven": "семь",
               "eight": "восемь",
               "nine": "девять",
               "ten": "десять"}
    print(numbers.get(num))


num_translate("")


"""
2. Доработать предыдущую функцию num_translate_adv(): 
реализовать корректную работу с числительными, начинающимися с заглавной буквы. 
"""

def num_translate_adv(num):
    first_letter = num[0]
    numbers = {"zero": "ноль",
               "one": "один",
               "two": "два",
               "three": "три",
               "four": "четыре",
               "five": "пять",
               "six": "шесть",
               "seven": "семь",
               "eight": "восемь",
               "nine": "девять",
               "ten": "десять"}
    if first_letter.islower():
        print(numbers.get(num))
    elif first_letter.isupper():
        print(numbers.get(num.lower()).title())


num_translate_adv("Two")


"""
3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь, 
в котором ключи — первые буквы имен, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
"""

def thesaurus(*names):
    my_dict = {}

    for name in names:
        first_letter = name[0]
        if first_letter in my_dict:
            my_dict[first_letter].append(name)
        else:
            my_dict[first_letter] = [name]

    return my_dict


print(thesaurus("Анна", "Павел", "Виктория", "Василий", "Виктор", "Геннадий", "Петр"))


"""
5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков:
nouns = ["автомобиль", "лес", "огонь", "город", "дом", "хуй"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий", "мама", "зоря"]

       Например:
>>> get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]

Документировать код функции.
*Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
(когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?
"""

import random

NOUNS = ["автомобиль", "лес", "огонь", "город", "дом", "привет"]
ADVERBS = ["сегодня", "вчера", "завтра", "позавчера"]
ADJECTIVES = ["веселый", "яркий", "зеленый", "утопичный", "мягкий", "мама", "зоря"]


def get_jokes(n, unique=False):
    jokes = []
    used_words = []

    """
    if unique check that n is less than the minimum length of words
    """

    if unique and (n > len(NOUNS) or n > len(ADVERBS) or n > len(ADJECTIVES)):
        return

    def get_unique(words):
        word = random.choice(words)

        while word in used_words:
            word = random.choice(words)

        used_words.append(word)
        return word

    for i in range(n):
        if unique:
            noun = get_unique(NOUNS)
            adverb = get_unique(ADVERBS)
            adj = get_unique(ADJECTIVES)
        else:
            noun = random.choice(NOUNS)
            adverb = random.choice(ADVERBS)
            adj = random.choice(ADJECTIVES)

        jokes.append(noun + ' ' + adverb + ' ' + adj)

    return jokes


print(get_jokes(5))
print(get_jokes(4, unique=True))