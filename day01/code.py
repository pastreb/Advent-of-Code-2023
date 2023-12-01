import os.path

input_file = os.path.join(os.path.dirname(__file__), 'sample_input_2.txt')

def replace_spelled_digits(s):
    s = s.replace("one", "1")
    s = s.replace("two", "2")
    s = s.replace("three", "3")
    s = s.replace("four", "4")
    s = s.replace("five", "5")
    s = s.replace("six", "6")
    s = s.replace("seven", "7")
    s = s.replace("eight", "8")
    s = s.replace("nine", "9")
    return s

def read_input():
    with open(input_file, 'r') as f:
        lines = f.readlines()
        input = []
        for line in lines:
            line = replace_spelled_digits(line)
            print(line)
            line_numbers = []
            for character in line:
                if character.isdigit():
                    line_numbers.append(int(character))
            input.append(line_numbers)
        print(input)
        return input

def compute():
    input = read_input()
    sum = 0
    for line in input:
        sum += line[0]*10 + line[len(line)-1]
    return sum

if __name__ == '__main__':
    print(compute())