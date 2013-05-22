import sys

def main():
  args = sys.argv[1:]

  mod = __import__(args[0])
  mod.main(*args[0])

if __name__ == '__main__':
  main()

