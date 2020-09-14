import string

# Из файла создается словарь с комбинациями букв заданной длины и их количеством в тексте. Словарь отсортирован по убыванию
def letters_combinations(file, combo_letter_amount):
    handle = open(file, encoding='utf-8')
    data = handle.read()
    data = data.translate(str.maketrans("", "", string.punctuation))
    data = data.translate(str.maketrans("", "", string.digits))
    data = data.lower()
    letter_dictionary = {}
    buffer = ""
    for letter in data:
        if (letter == " ") or (letter == "\n"):
            continue
        buffer += letter
        if len(buffer) == combo_letter_amount:
            letter_dictionary[buffer] = 1 if buffer not in letter_dictionary else letter_dictionary[buffer] + 1
            buffer = ""
    letter_dictionary = {k: v for k, v in
                             sorted(letter_dictionary.items(), key=lambda item: item[1], reverse=True)
                             }
    handle.close()
    return letter_dictionary


# Из двух словарей создается один, в котором ключи - пересечение множеств ключей словаря, а значения - разность значений
def intersected_dictionary_creator(first_dict, second_dict, is_absolute_values):
    first_key_set = set(first_dict.keys())
    second_key_set = set(second_dict.keys())
    intersection_key_set = first_key_set.intersection(second_key_set)
    letter_dictionary = {}
    if is_absolute_values:
        for key in intersection_key_set:
            letter_dictionary[key] = abs(first_dict[key] - second_dict[key])
        letter_dictionary = {k: value for k, value in
                             sorted(letter_dictionary.items(), key=lambda item: item[1], reverse=True)}
    else:
        for key in intersection_key_set:
            letter_dictionary[key] = first_dict[key] - second_dict[key]
        letter_dictionary = {k: value for k, value in
                             sorted(letter_dictionary.items(), key=lambda item: item[1], reverse=True)}
    return letter_dictionary

#  Создается словарь из комбинаций заданной длины из файла, для которого требуется определить язык. Затем множество его
# ключей сравнивается по метрике Жаккара с множествами ключей из русского и болгарского "словарей".
def belonging_determinator(file, ru_dict, bg_dict, combo_letter_amount):
    file_dictionary = letters_combinations(file, combo_letter_amount)
    ru_comparing_dictionary = intersected_dictionary_creator(ru_dict, file_dictionary, True)
    ru_intersection_size = len(set(ru_comparing_dictionary.keys()))
    ru_union_set = set(file_dictionary.keys()).union(set(ru_dict.keys()))
    ru_union_size = len(ru_union_set)
    ru_jaccard = ru_intersection_size / ru_union_size


    bg_comparing_dictionary = intersected_dictionary_creator(bg_dict, letters_combinations(file, combo_letter_amount), True)
    bg_intersection_size = len(set(bg_comparing_dictionary.keys()))
    bg_union_set = set(file_dictionary.keys()).union(set(bg_dict.keys()))
    bg_union_size = len(bg_union_set)
    bg_jaccard = bg_intersection_size / bg_union_size


    if ru_jaccard > bg_jaccard:
        print("Most likely it is Russian with probability(ru): " + str(ru_jaccard) + " (bg): " + str(bg_jaccard))
    elif ru_jaccard < bg_jaccard:
        print("Most likely it is Bulgarian with probability(ru): " + str(ru_jaccard) + " (bg): " + str(bg_jaccard))
    else:
        print("Same opportunity it is Russian or Bulgarian with probability(ru): " + str(ru_jaccard) + " (bg): " + str(bg_jaccard))


if __name__ == '__main__':
    two_letters_ru = letters_combinations("OpenSubtitles.bg-ru.ru.txt", 2)
    three_letters_ru = letters_combinations("OpenSubtitles.bg-ru.ru.txt", 3)
    print("Most common 2-letter combinations RU: " + str(two_letters_ru))
    print("Most common 3-letter combinations RU: " + str(three_letters_ru))
    # four_letters_ru = letters_combinations("D:\\OpenSubtitles.bg-ru.ru.txt", 4)

    two_letters_bg = letters_combinations("OpenSubtitles.bg-ru.bg.txt", 2)
    three_letters_bg = letters_combinations("OpenSubtitles.bg-ru.bg.txt", 3)
    print("Most common 2-letter combinations BG: " + str(two_letters_bg))
    print("Most common 3-letter combinations BG: " + str(three_letters_bg))

    max_defferences_two_letter_combo = intersected_dictionary_creator(two_letters_ru, two_letters_bg, True)
    max_defferences_three_letter_combo = intersected_dictionary_creator(three_letters_ru, three_letters_bg, True)
    print("Most different 2-letter combinations: " + str(max_defferences_two_letter_combo))
    print("Most different 3-letter combinations: " + str(max_defferences_three_letter_combo))
    # four_letters_bg = letters_combinations("D:\\OpenSubtitles.bg-ru.bg.txt", 4)

    print("Testing files:")
    belonging_determinator("BG_text_1.txt", two_letters_ru, two_letters_bg, 2)
    belonging_determinator("BG_text_1.txt", three_letters_ru, three_letters_bg, 3)

    belonging_determinator("BG_text_2.txt", two_letters_ru, two_letters_bg, 2)
    belonging_determinator("BG_text_2.txt", three_letters_ru, three_letters_bg, 3)

    belonging_determinator("RU_text_1.txt", two_letters_ru, two_letters_bg, 2)
    belonging_determinator("RU_text_1.txt", three_letters_ru, three_letters_bg, 3)

    belonging_determinator("RU_text_2.txt", two_letters_ru, two_letters_bg, 2)
    belonging_determinator("RU_text_2.txt", three_letters_ru, three_letters_bg, 3)