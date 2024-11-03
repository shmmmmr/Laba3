# TODO  Напишите функцию count_letters
def count_letters(text):
    dict = {}
    text=text.lower()
    DEFAULT_COUNT = 0
    for i in text:
        if i.isalpha():
            dict[i] = dict.get(i, DEFAULT_COUNT) + 1
    return dict

# TODO Напишите функцию calculate_frequency
def calculate_frequency(dict):
    total_letters = sum(dict.values())
    frequency_dict = {}
    for letter, count in dict.items():
        frequency_dict[letter] = (count / total_letters)
    return frequency_dict

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""


# TODO Распечатайте в столбик букву и её частоту в тексте
letter_count = count_letters(main_str)
freq = calculate_frequency(letter_count)
for letter, freq in freq.items():
    print(f"{letter}: {'%.2f'%freq}")