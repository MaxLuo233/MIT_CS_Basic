permutations = []
permutations2 = set([])

def getPerms(l, path=[]):
    """ Get all permutations from a list of a list. Used as a helper 
    function for query. """
    global permutations
    if not l:
        permutations.append(path)
        return
    for item in l[0]:
        if item not in path:
            getPerms(l[1:], path+[item])

test = [['age','df'],['fefe','sfaf']]
getPerms(test)
print(permutations)