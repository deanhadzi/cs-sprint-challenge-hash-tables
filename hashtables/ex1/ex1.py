def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # creating an empty hashtable.
    weights_dict = {}

    for index, weight in enumerate(weights):
        
        # check if we have limit - weight in the dict already.
        if limit - weight in weights_dict:

            # find the index of the value which is in the dict already.
            second_item = weights_dict.get(limit - weight), index
            
            # return the solution.
            return tuple(sorted(second_item, reverse=True))

        # otherwise, if item is not in hashtable, add it.
        else:
            weights_dict[weight] = index

    # return None if we didn't find anything.
    return None
