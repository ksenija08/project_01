# Задача 2.2. 

# Напишите функцию, которая возвращает номер квартал по номеру месяца
# Например: 
# месяц 2 (февраль) является частью первого квартала; 
# месяц 6 (июнь) является частью второго квартала; 
# месяц 11 (ноябрь) является частью четвертого квартала.

number = int(input('Введите номер месяца: '))
nomber_month = {1:'январь', 2:'февраль', 3:'март', 4:'апрель', 5:'май', 6:'июнь', 7:'июль', 8:'август', 9:'сентябрь', 10:'октябрь', 11:'ноябрь', 12: 'декабрь'}
nomber_quarter = {1:'первого', 2:'второго', 3:'третьего', 4:'четвертого'}

def quarter_of(month):
    quarter = (month+2) // 3 
    return quarter

if 1 <= number <= 12:
    print (f"Месяц {number} ({nomber_month[number]}) является частью {nomber_quarter[quarter_of(number)]} квартала")
else:
    print('Такого месяца нет!')    