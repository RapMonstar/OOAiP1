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
        print('Однозначное число')


class twoDigitNnumber(object):
    @staticmethod
    def check(number):
        print('Двузначное число')


class aLotOfNumbers(object):
    @staticmethod
    def check(number):
        print('Число с большим количеством знаков')


class Number(object):
    @classmethod
    def open(cls, number):
        if len(str(number)) == 1:
            checker = singleDigitNumber
        elif len(str(number)) == 2:
            checker = twoDigitNnumber
        elif len(str(number)) >= 3:
            checker = aLotOfNumbers

        #print(checker)
        #print(checker.check(a))
        return cls(checker.check(number), number)

    def __init__(self, checker, number):
        self._checker = checker
        self._number = number

Number.open(10000000000000000)
