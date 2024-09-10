import itertools

lst = ['a', 'b', 'c']

def allPossibleSets(lst):
    sets = []
    for i in lst:
        sets.append(i)
    for i in range(2,len(lst)+1):
        sets.extend(list(itertools.permutations(lst, i)))
    for i in range(len(sets)):
        if isinstance(sets[i], tuple):
            sets[i] = '|'.join(sets[i])
    return sets


lst = ['a', 'b', 'c']

print(f'All possible sets: {allPossibleSets(lst)}')