with open("inputs/13", "r") as f:
    data = list(map(lambda x:x.splitlines(), f.read().split('\n\n')))

# with open("tests/13", "r") as f:
#     data = list(map(lambda x:x.splitlines(), f.read().split('\n\n')))

def is_hor_mirror(data, i, j):
    if not i+j+1 < len(data) or not i-j >= 0: return True
    if data[i+j+1] == data[i-j]:
        return is_hor_mirror(data, i, j+1)
    return False

def is_ver_mirror(data, i, j):
    if not i+j+1 < len(data[0]) or not i-j >= 0: return True
    column1 = ''.join(list(map(lambda x: x[i+j+1], data)))
    column2 = ''.join(list(map(lambda x: x[i-j], data)))
    if column1 == column2:
        return is_ver_mirror(data, i, j+1)
    return False

sum = 0
for stuff in data:
    rows = len(stuff)
    for i in range(rows - 1):
        if is_hor_mirror(stuff, i, 0):
            sum += 100 * (i + 1)
    columns = len(stuff[0])
    for i in range(columns - 1):
        if is_ver_mirror(stuff, i, 0):
            sum += i + 1
print(sum)
