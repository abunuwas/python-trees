
tree = [
    [1],
    [2, 3],
    [4, 5, 6],
    [7, 8, 9, 10],
    [11, 12, 13, 14, 15]
     ]

def buildPaths(tree):
    paths = []
    numberPaths = 2**(len(tree)-1)
    movs = ('L', 'R')    
    while len(paths) < numberPaths:
        if len(paths) == 0:
            for mov in movs:
                paths.append(mov)
        else:
            newPaths = []
            for path in paths:
                for mov in movs:
                    newPaths.append(path+mov)
            paths = newPaths

    return paths

paths = buildPaths(tree)

paths = set(paths)

for path in paths:
    print(path)
                
def buildTree(data):
    tree = []
    for index, row in enumerate(data):
        try:
            nextRow = data[index+1]
        except IndexError:
            break
        for position, value in enumerate(row):
            node = {'value': value,
                    'row': index,
                    'position': position,
                    'L': {'row': index+1, 'position': position},
                    'R': {'row': index+1, 'position': position+1}
                    }
            tree.append(node)
    return tree
            
nodes = buildTree(tree)

pathNumbers = []
for path in paths:
    newPath = []
    for index, mov in enumerate(path):
        for node in nodes:
            possibleTargets = []
            if node['row'] == index:
                possibleTargetValue = node[mov]
                possibleTargets.append(possibleTargetValue)
            for node in possibleTargets:
                try:
                    if node['position'] == newPath[-1]['position']:
                        newPath.append(node)
                except IndexError:
                    print(node)
                    newPath.append(node)
        pathNumbers.append(newPath)

pathValues = []
for path in pathNumbers:
    newPath = ''
    for node in path:
        value = tree[node['row']][node['position']]
        newPath += str(value)
    pathValues.append(newPath)

for path in pathValues:
    print(path)
                
        
    



    
    




