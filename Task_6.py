#Дано число обозначающее день недели.Вывести его название и указать является ли он выходным.
dayName = 'ПН', 'ВТ', 'СР', 'ЧТ', 'ПТ', 'СБ', 'ВС'
day = int (input('Введите число обозначающее день недели '))
if (7 >= day >= 1):
    print (day, 'это', dayName[day-1])
else:
    print ('В неделе 7 дней. Введите число от 1 до 7')