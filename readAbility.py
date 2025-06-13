text = input("Text : ")

# Счётчики
cnt_letters = 0
cnt_words = 1
cnt_sentence = 0

# Считаем буквы, слова, предложения
for char in text:
    if char.isalpha(): cnt_letters += 1
    elif char == " ": cnt_words += 1
    elif char in [".", "!", "?"]: cnt_sentence += 1

# Задаём значения переменным
L = cnt_letters / cnt_words * 100
S = cnt_sentence / cnt_words * 100

formulas = int(0.0588 * L - 0.296 * S - 15.8)

if formulas < 1: print("Before Grade 1")
elif formulas >= 16: print("Grade 16+")
else: print(f"Grade {formulas}")