def nearest_value(values: set[int], one: int) -> int:
    values_list = list(values)
    values_list.append(one)
    values_list.sort()
    one_index = values_list.index(one)
    more = values_list.index(one) + 1
    less = values_list.index(one) - 1
    if one_index == 0:
        return values_list[1]
    elif values_list[one_index] == values_list[-1]:
        return values_list[-2]
    elif values_list[more] - values_list[one_index] < values_list[one_index] - values_list[less]:
        return values_list[more]
    else:
        return values_list[less]


print("Example:")
print(nearest_value({4, 7, 10, 11, 12, 17}, 9))

assert nearest_value({17, 4, 7, 10, 11, 12}, 9) == 10
assert nearest_value({17, 4, 7, 10, 11, 12}, 8) == 7
assert nearest_value({17, 4, 8, 10, 11, 12}, 9) == 8
assert nearest_value({17, 4, 9, 10, 11, 12}, 9) == 9
assert nearest_value({17, 4, 7, 10, 11, 12}, 0) == 4
assert nearest_value({17, 4, 7, 10, 11, 12}, 100) == 17
assert nearest_value({100, 5, 8, 89, 10, 12}, 7) == 8
assert nearest_value({2, 3, -1}, 0) == -1
assert nearest_value({5}, 5) == 5
assert nearest_value({5}, 7) == 5

print("The mission is done! Click 'Check Solution' to earn rewards!")