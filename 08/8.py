from starter import get_puzzle_input
import pdb

numbers = []

for line in get_puzzle_input(8):
    four_signal = ""
    one_signal = ""
    seven_signal = ""

    bottom = ""
    top = ""
    middle = ""
    top_left = ""
    bottom_right = ""
    bottom_left = ""
    top_right = ""

    left, right = line.split("|")
    all_ten = list(left.split())
    output = list(right.split())
    for elem in all_ten:
        if len(elem) == 2:
            one_signal = elem
        elif len(elem) == 3:
            seven_signal = elem
        elif len(elem) == 4:
            four_signal = elem

    for signal in seven_signal:
        if signal not in one_signal:
            top = signal
    for digit in all_ten:
        if len(digit) == 5 and all(signal in digit for signal in seven_signal):
            middle = [signal for signal in four_signal if signal not in one_signal and signal in digit][0]
            top_left = [signal for signal in four_signal if signal not in digit][0]
            bottom = [signal for signal in digit if signal != top and signal not in one_signal and signal != middle][0]
            break
    for digit in all_ten:
        if len(digit) == 5 and all(part in digit for part in (bottom, top, middle, top_left)):
            bottom_right = [signal for signal in digit if signal not in (bottom, top, middle, top_left)][0]
            break
    top_right = [signal for signal in one_signal if signal != bottom_right][0]
    for digit in all_ten:
        if len(digit) == 7:
            bottom_left = [signal for signal in digit if signal not in (bottom,top,middle,top_left,top_right,bottom_right)][0]
    
    output_string = ""

    for digit in output:
        if top_right in digit and bottom_right in digit:
            if len(digit) == 2:
                output_string += "1"
            elif len(digit) == 4:
                output_string += "4"
            elif len(digit) == 3:
                output_string += "7"
            elif len(digit) == 7:
                output_string += "8"
            elif len(digit) == 6 and middle not in digit:
                output_string += "0"
            elif top in digit and bottom in digit and middle in digit:
                if top_left in digit:
                    output_string += "9"
                else:
                    output_string += "3"
        elif top in digit and bottom in digit and middle in digit:
            if top_left in digit:
                if bottom_left in digit:
                    output_string += "6"
                else:
                    output_string += "5"
            else:
                output_string += "2"
    print(output_string)
    numbers.append(int(output_string))

print(sum(numbers))
