# 1 вариант
def single_root_words(root_word, *other_words):
    same_words=[]
    for i in range (len(other_words)):
        if root_word.lower() in other_words[i].lower() or other_words[i].lower() in root_word.lower():
            same_words.append(other_words[i])

    return same_words

result1 = single_root_words('клон', 'склон', 'поклонение', 'клоп', 'наклонность')
result2 = single_root_words('Солнцеворот', 'солнце', 'Ворот', 'Рот', 'ворота')
print(result1)
print(result2)

# 2 вариант
def single_root_words(root_word, *other_words):
    same_words=[]
    for i in range (len(other_words)):
        count1 = other_words[i].upper().count(root_word.upper())
        count2 = root_word.upper().count(other_words[i].upper())
        if count1 + count2 >= 1:
            same_words.append(other_words[i])

    return same_words

result1 = single_root_words('клон', 'склон', 'поклонение', 'клоп', 'наклонность')
result2 = single_root_words('Солнцеворот', 'солнце', 'Ворот', 'ворота')
print(result1)
print(result2)