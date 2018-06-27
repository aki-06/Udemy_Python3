# クラスの初期化とクラス変数
class Person(object):
    def __init__(self, name):
        """
        コンストラクタ
        オブジェクトが生成されたら最初に呼ばれる
        """
        self.name = name

    def say_something(self):
        print('I am {}. hello.'.format(self.name))
        # 自分自身のメソッドにもアクセスできる
        self.run()

    def run(self):
        print('run')

    def __del__(self):
        """
        デストラクタ
        オブジェクトが使われなくなったら呼び出される
        """
        print('good bye')


person = Person('Mike')
person.say_something()

# 直接呼び出す
del person

print('##########')