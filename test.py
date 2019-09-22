a = [1,2,3]
print(not a)

def getAllSubsets(lst):
    """
        lst: A list
    Returns the powerset of lst, i.e. a list of all the possible subsets of lst
    """
    print(lst)
    if not lst:
        return [[]]
    withFirst = [[lst[0]] + rest for rest in getAllSubsets(lst[1:])]
    withoutFirst = getAllSubsets(lst[1:])
    return withFirst + withoutFirst

print(getAllSubsets(a))
