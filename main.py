original_text = input("Введите сообщение: ")
lenght = len(original_text)
print(f"Количество символов в строке:{lenght}")
print(f"Второй символ строки: {original_text[1]}")
print(f"Последний символ строки: {original_text[-1]}")
print(f"Последние три символа строки: {original_text[-3:]}")
print(f"Первые три символа строки: {original_text[:3]}")
print(f"Раскраска: \u001b[31m \u001b[46m {original_text} \u001b[0m")
color_start = int(input("С какого номера начать окраску? "))
color_end = int(input("На каком номере закончить окраску? "))
color_name = input("Какой цвет выбрать? ")
if color_name == "Синий":
    colorized_text = f"{original_text[:color_start]} \u001b[34m {original_text[color_start:color_end]} \u001b[0m {original_text[color_end:]}"
elif color_name == "Красный":
    colorized_text = f"{original_text[:color_start]} \u001b[31m {original_text[color_start:color_end]} \u001b[0m {original_text[color_end:]}"
elif color_name == "Зелёный":
    colorized_text = f"{original_text[:color_start]} \u001b[32m {original_text[color_start:color_end]} \u001b[0m {original_text[color_end:]}"
elif color_name == "Жёлтый":
    colorized_text = f"{original_text[:color_start]} \u001b[33m {original_text[color_start:color_end]} \u001b[0m {original_text[color_end:]}"
else:
    print("Я вас не понял, сделаю красный цвет.")
    colorized_text = f"{original_text[:color_start]} \u001b[31m {original_text[color_start:color_end]} \u001b[0m {original_text[color_end:]}"
print(f"Раскрашенный текст: {colorized_text}")
old_char = input("Введите символ, который вы хотите заменить: ")
new_char = input("Введите символ, на который вы хотите заменить:  ")
modified_text = original_text.replace(old_char, new_char)
print(f"Текст после замены: {modified_text}")
print(f"Срез по чётным символам: {original_text[::2]}")
print(f"Срез по нечётным символам: {original_text[1::2]}")
reversed_text = original_text[::-1]
print(f"Текст с изменнёным порядком символов: {reversed_text}")
middle_index = lenght // 2
swapped_text = original_text[middle_index:] + original_text[:middle_index]
print(f"Текст с заменой местами левой и правой части {swapped_text}")
