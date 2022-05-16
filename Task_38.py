# 38.	Напишите программу, удаляющую из текста все слова, содержащие "абв".

text = 'ываабв лповап абвцукв алоабвабв ываываыв'

text_word = text.split()
find = 'абв'
new_text = []

for i in text_word:
    if find not in i:
        new_text.append(i)
text_2 = ' '.join(new_text)
print('Исходный список', text)
print()
print('Отредактированный список', text_2)