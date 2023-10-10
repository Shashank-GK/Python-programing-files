# This program is written for flattening the Nested list
def flatten(L):
    for e in L:
        if hasattr(e, "__iter__"):
            yield from flatten(e)
        else:
            yield e


print(next(flatten([1, 2, 3, 4, 5, 6, 7, 8])))
