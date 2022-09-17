# Реализовать программный продукт выполняющий проверку введёного пользователем числа - что введено:
# однозначное число, двузначное число или число с большим количеством знаков?
# При разработке использовать поведенческий паттерн Стратегия
#
#class NumberChecker(object):
#    @staticmethod
#    def check(number):
#        raise NotImplementedError()
#

class singleDigitNumber(object):
    @staticmethod
    def check(number):
        if len(str(number)) == 1:
            print('Однозначное число')
        else:
            print('Нет')


class twoDigitNnumber(object):
    @staticmethod
    def check(number):
        if len(str(number)) == 2:
            print('Двузначное число')
        else:
            print('Нет')


class aLotOfNumbers(object):
    @staticmethod
    def check(number):
        if len(str(number)) >= 3:
            print('Число с большим количеством знаков')
        else:
            print('Нет')



class Number(object):
    @classmethod
    def open(cls, number):
        print("Check ls\n1. Однозначное число \n2. Двузначное число \n3. Число с большим количеством знаков")
        menu = int(input())

        if menu == 1:
            checker = singleDigitNumber
        elif menu == 2:
            checker = twoDigitNnumber
        elif menu == 3:
            checker = aLotOfNumbers

        #if len(str(number)) == 1:
        #    checker = singleDigitNumber
        #elif len(str(number)) == 2:
        #    checker = twoDigitNnumber
        #elif len(str(number)) >= 3:
        #    checker = aLotOfNumbers

        #print(checker)
        #print(checker.check(a))
        return cls(checker.check(number), number)

    def __init__(self, checker, number):
        self._checker = checker
        self._number = number

Number.open('1')