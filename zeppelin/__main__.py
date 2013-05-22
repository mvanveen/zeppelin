import sys


def main():
    args = sys.argv[1:]

    module = __import__(args[0])
    module.main(*args[1:])

if __name__ == '__main__':
    main()

