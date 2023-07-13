# Задача 2.2. 

# Напишите функцию, которая возвращает номер квартал по номеру месяца
# Например: 
# месяц 2 (февраль) является частью первого квартала; 
# месяц 6 (июнь) является частью второго квартала; 
# месяц 11 (ноябрь) является частью четвертого квартала.

number = int(input('Введите номер месяца: '))

def quarter_of(month): 

    nomber_month = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
    nomber_quarter = ['первого', 'второго', 'третьего', 'четвертого']

    if 1 <= month <= 12:
        quarter = (month+2) // 3 
        quarter_str = 'Месяц ' + str(month) + ' (' + str(nomber_month[month - 1]) + ') является частью ' + str(nomber_quarter[quarter-1])  + ' квартала'
    else:
       quarter_str = 'Такого месяца нет!'
    return  quarter_str   
  
print(quarter_of(number))     