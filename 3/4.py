bad_word = "редиска"

text = input("Введите комментарии : ")

text_new = text.replace(bad_word, "***")
print(text_new )
