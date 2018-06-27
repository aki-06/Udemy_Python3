# __name__と__main__

import lesson_package.talk.animal

import config

def calc(x, y):
    return x + y


def main():
    print(calc(5, 7))

if __name__ == '__main__':
    main()