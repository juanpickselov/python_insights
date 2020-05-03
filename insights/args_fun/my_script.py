import sys


def do_something(start_at=1, stop_at=2):
    return start_at, stop_at


if __name__ == '__main__':
    do_something(*sys.argv[1:])
    print('Script Name:= ', sys.argv[0])
    print('Arg 1:', sys.argv[1])
    print('Arg 2:', sys.argv[2])
