text = input("Введите текст: ")

# Разбиваем текст на слова
words = text.split()

# Считаем количество вхождений каждого слова
word_count = {}
for word in words:
    if word not in word_count:
        word_count[word] = 0
    word_count[word] += 1

# Находим наиболее часто встречающееся слово
most_common_word = max(word_count, key=word_count.get)

# Находим самое длинное слово
longest_word = max(words, key=len)

# Выводим результаты
print("Наиболее часто встречающееся слово:", most_common_word)
print("Самое длинное слово:", longest_word)