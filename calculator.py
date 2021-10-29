def calculator():
    operation = input('''
 Введите математическую операцию, которую вы хотите выполнить :
 + для сложения
 - для вычитания
 * для умножения
 / для деления, затем нажмите ввод
   ''')
    number_1 = int(input('Vvedite pervoe chislo:'))
    number_2 = int(input('Vvedite vtoroe chislo'))
    if operation == '+':
            print(number_1+number_2)
    elif operation == '-':
        print(number_1-number_2)
    elif operation == '*':
        print(number_1 * number_2)
    elif operation == '/':
        print(number_1 / number_2)
    else:
        if number_2 == 0:
              print('На ноль делить нельзя, ошибка ввода ')
calculator()

