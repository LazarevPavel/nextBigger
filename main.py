
#Задача:
# На вход подается число. Необходимо найти следующее по величине число, состоящее из тех же цифр, что и число на входе.
# Если следующее число найти невозможно, результат должен быть -1.


def nextBigger(number):
    number = [int(digit) for digit in str(number)]

    for index in range(len(number)-1, -1, -1):
        if index != 0:
            if number[index] > number[index-1]:
                digit = number[index-1]

                flag = False
                while flag != True:
                    digit += 1
                    if digit == 10:
                        return -1
                    if digit in number[index:]:
                        for target_index in range(index, len(number)):
                                if number[target_index] == digit:
                                    number[index-1], number[target_index] = number[target_index], number[index-1]
                                    flag = True
                                    break

                result = number[:index]
                result.extend(sorted(number[index:]))
                return ''.join([str(digit) for digit in result])
    return -1


# Проверяем работу
# удобно в качестве примера использовать 1234
in_number = int(input())

while in_number != -1:
    in_number = nextBigger(in_number)
    print(in_number)


