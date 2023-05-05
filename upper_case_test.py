
block_zero_upper_bottom = '    ****'
block_zero_middle = '***      ***'

block_one_bottom = '*********'
block_one_middle = '   **'


def print_zero(line):
    if line == 1:
        print(block_zero_upper_bottom)
        print_zero(line + 1)
    elif line == 5:
        print(block_zero_upper_bottom)
    else:
        print(block_zero_middle)
        print_zero(line + 1)


def print_one(line):
    if line == 5:
        print(block_one_bottom)
    else:
        print(block_one_middle)
        print_one(line + 1)


def array_space(input_array):
    array_length = []
    for b in range(len(input_array)):
        array_length.append(append_space(input_array[b]))
    return array_length


def append_space(input_array):
    if input_array == 0:
        return len(block_zero_middle) + 3
    elif input_array == 1:
        return len(block_one_bottom) + 3


def print_res(input_array, dist):
    array_all = [[], [], [], [], []]
    line = 5
    for k in range(line):
        if k == 0:
            for d in range(len(input_array)):
                if input_array[d] == 0:
                    elem_length = len(block_zero_upper_bottom)
                    array_all[0].append(block_zero_upper_bottom)
                    array_all[0].append((dist[d] - elem_length) * " ")
                elif input_array[d] == 1:
                    elem_length = len(block_one_middle)
                    array_all[0].append(block_one_middle)
                    array_all[0].append((dist[d] - elem_length) * " ")
        elif k == 4:
            for d in range(len(input_array)):
                if input_array[d] == 0:
                    elem_length = len(block_zero_upper_bottom)
                    array_all[4].append(block_zero_upper_bottom)
                    array_all[4].append((dist[d] - elem_length) * " ")
                elif input_array[d] == 1:
                    elem_length = len(block_one_bottom)
                    array_all[4].append(block_one_bottom)
                    array_all[4].append((dist[d] - elem_length) * " ")
        else:
            for d in range(len(input_array)):
                if input_array[d] == 0:
                    elem_length = len(block_zero_middle)
                    array_all[k].append(block_zero_middle)
                    array_all[k].append((dist[d] - elem_length) * " ")
                elif input_array[d] == 1:
                    elem_length = len(block_one_middle)
                    array_all[k].append(block_one_middle)
                    array_all[k].append((dist[d] - elem_length) * " ")
    return array_all


if __name__ == "__main__":
    n = input()
    n = n.split()
    n = [int(i) for i in n]
    distance = array_space(n)
    value = print_res(n, distance)
    res = ''
    for v in value:
        for q in range(len(v)):
            if q == len(v) - 1:
                res += v[q] + '\n'
            else:
                res += v[q]
    print(res)
