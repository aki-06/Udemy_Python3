# optparse

from optparse import OptionParser


def main():
    usage = 'usage: %prog [options] arg1 arg2'
    parser = OptionParser(usage=usage)
    parser.add_option('-f', '--file', action='store', type='string', dest='filename', help='File Name')
    parser.add_option('-n', '--num', action='store', type='int', dest='num')
    parser.set_defaults(verbose=True)
    parser.add_option('-v', action='store_true', dest='verbose')
    parser.add_option('-q', action='store_false', dest='verbose')
    parser.add_option('-r', action='store_const', dest='user_name', const='root')
    options, args = parser.parse_args()
    print(options)
    print(args)


if __name__ == '__main__':
    main()