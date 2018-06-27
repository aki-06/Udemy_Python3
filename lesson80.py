# クラスの継承
class Car(object):
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print('run')


class ToyotaCar(Car):
    def run(self):
        """
        メソッドのオーバーライド
        """
        print('fast')


class TeslaCar(Car):
    def __init__(self, model='Model A', enable_auto_run=False):
        # 親クラスの__init__を呼び出す
        super().__init__(model)
        self.enable_auto_run = enable_auto_run

    def auto_run(self):
        print('auto run')

car = Car()
car.run()

print('######################')

toyota_car = ToyotaCar('Lexus')
print(toyota_car.model)
toyota_car.run()

print('######################')
tesla_car = TeslaCar()
print(tesla_car.model)
tesla_car.run()
tesla_car.auto_run()