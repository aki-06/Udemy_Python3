# プロパティを使った属性の設定
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
    def __init__(self, model='Model A',
                 enable_auto_run=False,
                 passwd='123'):
        # 親クラスの__init__を呼び出す
        super().__init__(model)
        # 外部からいじって欲しくないことを明示する「_」
        # self._enable_auto_run = enable_auto_run
        self.__enable_auto_run = enable_auto_run
        self.passwd = passwd

    @property
    def enable_auto_run(self):
        return self._enable_auto_run

    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
        if self.passwd == '456':
            self._enable_auto_run = is_enable
        else:
            raise ValueError

    def auto_run(self):
        # クラス内からは__enable_auto_runにアクセスできる
        print(self.__enable_auto_run)
        print('auto run')

tesla_car = TeslaCar('model S', passwd='123')
tesla_car.auto_run()
# tesla_car.enable_auto_run = True
# print(tesla_car.__enable_auto_run)

