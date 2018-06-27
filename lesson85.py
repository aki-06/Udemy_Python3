# 抽象クラス
import abc

class Person(metaclass=abc.ABCMeta):
    def __init__(self, age=1):
        self.age = age

    @abc.abstractmethod
    def drive(self):
        """
        継承したクラスは必ず実装しなくてはならない
        必要がなければ多用しない
        """
        pass


class Baby(Person):
    def __init__(self, age=1):
        if age < 18:
            super().__init__(age)
        else:
            ValueError

    def drive(self):
        raise Exception('no drive')


class Adult(Person):
    def __init__(self, age=18):
        if age >= 18:
            super().__init__(age)
        else:
            ValueError

    # def drive(self):
    #     print('ok')

baby = Baby()
# baby.drive()
adult = Adult()
adult.drive()

class Car(object):
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print('run')

    def ride(self, person):
        person.drive()

car = Car()
car.ride(adult)