# NO IMPORTS ALLOWED!

import json

def getActor(data, actorid):
    """ data is dicionary: {actor:actor id} """
    for actor in data.keys():
        if data[actor] == actorid:
            return actor
    raise Exception('actor id doesn\'t exist')
    
def did_x_and_y_act_together(data, actor_id_1, actor_id_2):
    """ data is list: [[actor_id_1, actor_id_2, film_id]] """
    for mov in data:
        if actor_id_1 in mov and actor_id_2 in mov:
            return True
    return False

def baconDict(data):
    """ data is list: [[actor_id_1, actor_id_2, film_id]] """
    neighbors = {}
    for mov in data:
        actor1,actor2 = mov[0],mov[1]
        if actor1 not in neighbors:
            neighbors[actor1] = set([actor2])
        else:
            neighbors[actor1].add(actor2)
        if actor2 not in neighbors:
            neighbors[actor2] = set([actor1])
        else:
            neighbors[actor2].add(actor1)
    for actor in neighbors:
        neighbors[actor] = list(neighbors[actor])
    return neighbors
    
def get_actors_with_bacon_number(data, n):
    """ data is list: [[actor_id_1, actor_id_2, film_id]] """
    neighbors = baconDict(data)
    
    #if n=0 or n=1
    if n == 0:
        return set([4724])
    elif n == 1:
        return set(neighbors[4724])
    
    #for n>1
    queue = [(4724,0)]
    visited = set([])
    baconDicts = {0:visited}
    while queue:
        actor = queue.pop(0)
        if actor[0] not in visited:
            visited.add(actor[0])
            if actor[1] not in baconDicts:
                baconDicts[actor[1]] = set([actor[0]])
            else:
                baconDicts[actor[1]].add(actor[0])
            for ids in neighbors[actor[0]]:
                queue.append((ids,actor[1]+1))
    if n not in baconDicts:
        return set([])
    return baconDicts[n]

def get_bacon_path(data, actor_id):
    """ data is list: [[actor_id_1, actor_id_2, film_id]] """
    neighbors = baconDict(data)
    queue = [[4724]]
    visited = set([])
    while queue:
        path = queue.pop(0)
        for ids in neighbors[path[-1]]:
            if ids == actor_id:
                path.append(ids)
                return path
            if ids not in visited:
                pcopy = path.copy()
                pcopy.append(ids)
                queue.append(pcopy)
            visited.add(ids)

def get_path(data, actor_id_1, actor_id_2):
    """ data is list: [[actor_id_1, actor_id_2, film_id]] """
    neighbors = baconDict(data)
    queue = [[actor_id_1]]
    visited = set([])
    while queue:
        path = queue.pop(0)
        for ids in neighbors[path[-1]]:
            if ids == actor_id_2:
                path.append(ids)
                return path
            if ids not in visited:
                pcopy = path.copy()
                pcopy.append(ids)
                queue.append(pcopy)
            visited.add(ids)

def getMovie(data, actor1, actor2):
    """ data is list: [[actor_id_1, actor_id_2, film_id]] 
        actor1 and actor2 are id numbers """
    for mov in data:
        if actor1 in mov and actor2 in mov:
            return mov[2]
    raise Exception('actors did\'t act together')

if __name__ == '__main__':
    with open('resources/small.json') as f:
        smalldb = json.load(f)