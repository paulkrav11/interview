import re
import sys

def main(input_string):
    numbers = re.findall(r'-?\b\d+\b', input_string)
    unique_numbers = set(map(int, numbers))
    sorted_numbers = sorted(unique_numbers)
    result = ' '.join(map(str, sorted_numbers))

    print(result)

if __name__ == "__main__":

    if len(sys.argv) > 1:
        input_string = ' '.join(sys.argv[1:])
        main(input_string)
    else:
        print("Введите строку с числами в качестве аргумента")