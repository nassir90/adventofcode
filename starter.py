import sys

def get_puzzle_input(day: int, old=True):
    if len(sys.argv) == 2 and sys.argv[1] == "r":
        file = open(("input%d" % day) if old else "input")
    else:
        file = open(("example%d" % day) if old else "example")
    return [ line.strip() for line in file ]
