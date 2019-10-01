from functools import reduce
from operator import mul


def find_maximum_product(sequence: list):
    if not all([type(x) == int for x in sequence]):
        raise TypeError("Every elements must be integer.")

    # I am assuming that you want 0 if there is no elements, alternatively It can throw an error here.
    if len(sequence) == 0:
        return 0

    # I am assuming that you want the whole product if there is less than 3 elements.
    if len(sequence) < 3:
        return reduce(mul, sequence)

    # All negatives is a special case:
    # If we have access to positives we want smallest negatives to have maximum absolute value
    # If we don't have any positives we are trying to find largest negatives to minimize the lost.
    if all([x < 0 for x in sequence]):
        negatives = sequence[:3]
        negatives.sort(reverse=True)

        for x in sequence[3:]:
            for i, y in enumerate(negatives):
                if x > y:
                    negatives.insert(i, x)
                    negatives.pop()
                    break
        return reduce(mul, negatives)

    # If you want to generalize this to product of k, it is better to use heaps rather than lists.
    top_negatives = [0, 0]
    top_positives = [0, 0, 0]

    # Going through each elements to find smallest negatives and largest positives.
    for x in sequence:
        if x < 0:
            for i, y in enumerate(top_negatives):
                if x < y:
                    top_negatives.insert(i, x)
                    top_negatives.pop()
                    break
        elif x > 0:
            for i, y in enumerate(top_positives):
                if x > y:
                    top_positives.insert(i, x)
                    top_positives.pop()
                    break

    # Comparing + * + * + VS. - * - * + cases.
    return max(reduce(mul, top_positives), reduce(mul, top_negatives) * top_positives[0])
