import sys

def get_puzzle_input(day: int):
    if len(sys.argv) == 2 and sys.argv[1] == "r":
        file = open("input%d" % day)
    else:
        file = open("example%d" % day)
    return [ line for line in file ]
