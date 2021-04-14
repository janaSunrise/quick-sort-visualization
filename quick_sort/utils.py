import random


def generate_random_values(length, range_: tuple):
    lst = [random.randint(range_[0], range_[1]) for _ in range(length)]
    return lst


def scale_value(value, old_range: tuple, new_range: tuple):
    old_range_v = old_range[1] - old_range[0]
    new_range_v = new_range[1] - new_range[0]

    new_value = (((value - old_range[0]) * new_range_v) / old_range_v) + new_range[0]
    return new_value


def scale_list(lst: list, range_: tuple):
    old_range = (min(lst), max(lst))

    scaled_list = [round(scale_value(elem, old_range, range_)) for elem in lst]
    return scaled_list
