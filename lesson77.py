# クラスの定義

# (object)は書いておいた方がいい
class Person(object):
    def say_something(self):
        print('hello')


# オブジェクトの生成
person = Person()

# メソッドの呼び出し
person.say_something()