lines = open(0).readlines()

def parse_line(line):
    snum = int(find_first_digit(line)+find_first_digit(line,reverse=True))
    return snum

def find_first_digit(line,reverse=False):
    digit_indexes = [0]*9
    digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    if reverse:
        digits = list(map(lambda x:x[::-1], digits))
        line = line[::-1]
    for c in line:
        if c.isdigit(): return c
        for di, digit in enumerate(digits):
            if c == digit[digit_indexes[di]]:
                digit_indexes[di] += 1
                if len(digit) == digit_indexes[di]:
                    return str(di+1)
            else:
                if digit[0] == c:
                    digit_indexes[di] = 1
                else:
                    digit_indexes[di] = 0
    return '0'

print(sum(map(parse_line,lines)))
