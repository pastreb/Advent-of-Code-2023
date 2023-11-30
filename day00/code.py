import os.path

input_file = os.path.join(os.path.dirname(__file__), 'input.txt')

def read_input():
    with open(input_file, 'r') as f:
        lines = f.readlines()
        input = []
        for line in lines:
            input.append([int(num) for num in line.split()])
        print(input)
        return input

def compute():
    input = read_input()
    return 0

if __name__ == '__main__':
    compute()