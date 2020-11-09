def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # creating an empty hashtable and our answer container.
    numbers_dict = {}
    result = []

    # populate all items into dict.
    for index, number in enumerate(a):
        numbers_dict[index] = number

    # iterate through dict:
    for value in numbers_dict.values():
        if value < 0:
            if -value in numbers_dict:
                result.append(-value)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
