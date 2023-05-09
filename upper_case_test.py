# first, second, third, fourth, fifth.
block_zero_upper_bottom = '    ****'
block_zero_middle = '***      ***'

block_one_bottom = '*********'
block_one_middle = '   **'
block_one_first = ' ****'

block_two_first = '  ******'
block_two_second = '        **'
block_two_third = '      **'
block_two_fourth = '   **'
block_two_fifth = '*********'

block_three_first_fifth = ' *****'
block_three_sec_fourth = '      **'
block_three_middle = '  ****'

block_four_first_sec = '**      **'
block_four_third = '**********'
block_four_fourth_fifth = '        **'

block_five_first = '  *******'
block_five_sec = ' **'
block_five_third = '  *****'
block_five_fourth = '       **'
block_five_fifth = '*******'

block_six_top_bottom = '  *****'
block_six_sec = '**'
block_six_third = ' *******'
block_six_fourth = '**     **'

block_seven_first = '********'
block_seven_sec = '      **'
block_seven_third = '    **'
block_seven_bottom = '   **'

block_eight_135 = '  ******'
block_eight_24 = '**      **'

block_nine_first_third = '  *******'
block_nine_sec = '**       **'
block_nine_fourth = '        **'
block_nine_bottom = '********'


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


def print_two(line):
    if line == 1:
        print(block_two_first)
        print_two(line + 1)
    elif line == 2:
        print(block_two_second)
        print_two(line + 1)
    elif line == 3:
        print(block_two_third)
        print_two(line + 1)
    elif line == 4:
        print(block_two_fourth)
        print_two(line + 1)
    else:
        print(block_two_fifth)


def print_three(line):
    if line == 3:
        print(block_three_middle)
        print_three(line + 1)
    elif line == 2 or line == 4:
        print(block_three_sec_fourth)
        print_three(line + 1)
    else:
        print(block_three_first_fifth)
        if line == 1:
            print_three(line + 1)


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
    elif input_array == 2:
        return max(len(block_two_first), len(block_two_second),
                   len(block_two_third), len(block_two_fourth),
                   len(block_two_fifth)) + 3
    elif input_array == 3:
        return max(len(block_three_middle), len(block_three_sec_fourth),
                   len(block_three_first_fifth)) + 3
    elif input_array == 4:
        return max(len(block_four_first_sec), len(block_four_third),
                   len(block_four_fourth_fifth)) + 3
    elif input_array == 5:
        return max(len(block_five_first), len(block_five_sec),
                   len(block_five_third), len(block_five_fourth),
                   len(block_five_fifth),) + 3
    elif input_array == 6:
        return max(len(block_six_top_bottom), len(block_six_sec),
                   len(block_six_third), len(block_six_fourth)) + 3
    elif input_array == 7:
        return max(len(block_seven_sec), len(block_seven_first),
                   len(block_seven_third), len(block_seven_bottom)) + 3
    elif input_array == 8:
        return max(len(block_eight_24), len(block_eight_135)) + 3
    elif input_array == 9:
        return max(len(block_nine_first_third), len(block_nine_sec),
                   len(block_nine_fourth), len(block_nine_bottom)) + 3


def print_res(input_array, dist):
    array_all = [[], [], [], [], []]
    line = 5
    for k in range(line):
        if k == 0:
            for d in range(len(input_array)):
                if input_array[d] == 0:
                    elem_length = block_zero_upper_bottom
                elif input_array[d] == 1:
                    elem_length = block_one_first
                elif input_array[d] == 2:
                    elem_length = block_two_first
                elif input_array[d] == 3:
                    elem_length = block_three_first_fifth
                elif input_array[d] == 4:
                    elem_length = block_four_first_sec
                elif input_array[d] == 5:
                    elem_length = block_five_first
                elif input_array[d] == 6:
                    elem_length = block_six_top_bottom
                elif input_array[d] == 7:
                    elem_length = block_seven_first
                elif input_array[d] == 8:
                    elem_length = block_eight_135
                elif input_array[d] == 9:
                    elem_length = block_nine_first_third

                array_all[k].append(elem_length)
                array_all[k].append((dist[d] - len(elem_length)) * " ")

        elif k == 1:
            for d in range(len(input_array)):
                if input_array[d] == 0:
                    elem_length = block_zero_middle
                elif input_array[d] == 1:
                    elem_length = block_one_middle
                elif input_array[d] == 2:
                    elem_length = block_two_second
                elif input_array[d] == 3:
                    elem_length = block_three_sec_fourth
                elif input_array[d] == 4:
                    elem_length = block_four_first_sec
                elif input_array[d] == 5:
                    elem_length = block_five_sec
                elif input_array[d] == 6:
                    elem_length = block_six_sec
                elif input_array[d] == 7:
                    elem_length = block_seven_sec
                elif input_array[d] == 8:
                    elem_length = block_eight_24
                elif input_array[d] == 9:
                    elem_length = block_nine_sec

                array_all[k].append(elem_length)
                array_all[k].append((dist[d] - len(elem_length)) * " ")

        elif k == 2:
            for d in range(len(input_array)):
                if input_array[d] == 0:
                    elem_length = block_zero_middle
                elif input_array[d] == 1:
                    elem_length = block_one_middle
                elif input_array[d] == 2:
                    elem_length = block_two_third
                elif input_array[d] == 3:
                    elem_length = block_three_middle
                elif input_array[d] == 4:
                    elem_length = block_four_third
                elif input_array[d] == 5:
                    elem_length = block_five_third
                elif input_array[d] == 6:
                    elem_length = block_six_third
                elif input_array[d] == 7:
                    elem_length = block_seven_third
                elif input_array[d] == 8:
                    elem_length = block_eight_135
                elif input_array[d] == 9:
                    elem_length = block_nine_first_third
                
                array_all[k].append(elem_length)
                array_all[k].append((dist[d] - len(elem_length)) * " ")

        elif k == 3:
            for d in range(len(input_array)):
                if input_array[d] == 0:
                    elem_length = block_zero_middle
                elif input_array[d] == 1:
                    elem_length = block_one_middle
                elif input_array[d] == 2:
                    elem_length = block_two_fourth
                elif input_array[d] == 3:
                    elem_length = block_three_sec_fourth
                elif input_array[d] == 4:
                    elem_length = block_four_fourth_fifth
                elif input_array[d] == 5:
                    elem_length = block_five_fourth
                elif input_array[d] == 6:
                    elem_length = block_six_fourth
                elif input_array[d] == 7:
                    elem_length = block_seven_bottom
                elif input_array[d] == 8:
                    elem_length = block_eight_24
                elif input_array[d] == 9:
                    elem_length = block_nine_fourth
                array_all[k].append(elem_length)
                array_all[k].append((dist[d] - len(elem_length)) * " ")

        elif k == 4:
            for d in range(len(input_array)):
                if input_array[d] == 0:
                    elem_length = block_zero_upper_bottom
                elif input_array[d] == 1:
                    elem_length = block_one_bottom
                elif input_array[d] == 2:
                    elem_length = block_two_fifth
                elif input_array[d] == 3:
                    elem_length = block_three_first_fifth
                elif input_array[d] == 4:
                    elem_length = block_four_fourth_fifth
                elif input_array[d] == 5:
                    elem_length = block_five_fifth
                elif input_array[d] == 6:
                    elem_length = block_six_top_bottom
                elif input_array[d] == 7:
                    elem_length = block_seven_bottom
                elif input_array[d] == 8:
                    elem_length = block_eight_135
                elif input_array[d] == 9:
                    elem_length = block_nine_bottom
                array_all[k].append(elem_length)
                array_all[k].append((dist[d] - len(elem_length)) * " ")

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
