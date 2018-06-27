# クラスの定義

# (object)は書いておいた方がいい
class Person(object):
    def say_something(self):
        print('hello')


def main():
    # オブジェクトの生成
    person = Person()
    # メソッドの呼び出し
    person.say_something()

if __name__ == 'main':
    main()

print('モジュール名: {}'.format(__name__))