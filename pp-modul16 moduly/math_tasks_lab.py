def check_numbers(list):
    for number in list:
        if not isinstance(number, int):
            return False
        else:
            return True


def sum_of_numbers(list):
    sum_total = 0
    for i in list:
        sum_total += i
    return (sum_total)


def multiply_all_numbers(list):
    multiply_total = 1
    for num in list:
        multiply_total *= num
    return (multiply_total)


if __name__ == "__main__":
    print(check_numbers([0.5, 0.11, 23, 21]))
    print(check_numbers([0.5, 0.11, 23, 21, "szesc"]))
    print(check_numbers([23, 21]))
    print(sum_of_numbers([1, 2, 3, 4, 5]))
    print(multiply_all_numbers([1, 2, 3, 4, 5]))
