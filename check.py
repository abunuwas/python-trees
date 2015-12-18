
tree = [
    [1],
    [2, 3],
    [4, 5, 6],
    [7, 8, 9, 10],
    [11, 12, 13, 14, 15]
     ]


##nodes = {
##    11: {'value': 11,
##         'L': None,
##         'R': None
##         },
##    12: {'value': 12,
##         'L': None,
##         'R': None}
##    }
##
##nodes[7] = {'value': 7,
##            'L': nodes[11],
##            'R': nodes[12]}


tree2 = reversed(tree)
nodes = {}
nodeCounter = 0
justAdded=[]
to_add = []
for index, line in enumerate(tree2):
    adding=[]
    for position, value in enumerate(line):
        if index == 0:
            nodeCounter += 1
            nodes[nodeCounter] = {'value': value,
                           'L': None,
                           'R': None,
                           'row': index,
                           'position': position}
            adding.append(nodeCounter)
        else:
            nodeCounter += 1
            nodes[nodeCounter] = {'value': value,
                                  'row': index,
                                  'position': position}
            for node in justAdded:
                if nodes[node]['position'] == position and nodes[node]['row'] == index-1:
                    nodes[nodeCounter] = {'L': nodes[node]}
                    
                elif nodes[node]['position'] == position+1 and nodes[node]['row'] == index-1:
                    nodes[nodeCounter] = {'R': nodes[node]}
            adding.append(nodeCounter)

    justAdded = set(adding)


                    
##            for key, values in nodes.items():
##                if values['position'] in (position, position+1) and values['row'] == index-1:
##                    print(value, {key: value})
##            nodes[nodeCounter] = {'value': value,
##                                  'L': 

def getTree(file):
    rawData = open(file, 'r', encoding='utf-8').read().splitlines()

    tree=[]
    for line in rawData:
        tree.append([float(num) for num in line.split()])
    return tree

##tree = getTree('triangleio.txt')


def buildPaths(tree):
    '''
    This function finds all possible paths in a tree.
    The tree must be passed as an argument in the form of a list of lists.
    Every sub-list or row must contain individual elements, i.e. a single
    string with all the elements in the row is not valid. 
    '''
    paths = []
    numberPaths = 2**(len(tree)-1) # Calculates the number of paths. This only works for balanced trees in which every node has exactly two children. 
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

##paths = buildPaths(tree)

def transPathsPositions(paths):
    '''
    Translates the outcome returned by the buildPaths function into a list
    of movements, in which every movement is a tuple where the first value
    represents the row and the second value represents the position in the row. 
    '''
    pathsPositions = []
    for path in paths:
        newPath = [(0, 0)]
        position = 0
        for index, mov in enumerate(path):
            if mov == 'L':
                position = position
                newPath.append((index+1, position))
            else:
                position = position+1
                newPath.append((index+1, position))
        pathsPositions.append(newPath)

    return pathsPositions

##pathsPositions = transPathsPositions(paths)

def pathValues(pathPositions):
    '''
    This function builds the paths with their corresponding values, based
    in the information about the row and position values of every movement
    as provided by the transPathsPositions function. This function basically
    serves to check that we're considering all possible paths in the tree. 
    '''
    pathValues = []
    for path in pathsPositions:
        newPath=[]
        for row, position in path:
            newPath.append(tree[row][position])
        pathValues.append(newPath)

    return pathValues

##pathValues = pathValues(pathsPositions)
##for path in pathValues:
##    print(path)
    

def sumPaths(pathsValues):
    return [sum(path) for path in pathValues]

##sumPaths = sumPaths(pathValues)

def findMaxPath(data):
    print('Building tree...')
    tree = getTree(data)
    print('Building paths...')
    paths = buildPaths(tree)
    tree=None
    print('Obtaining positions...')
    pathsPositions = transPathsPositions(paths)
    paths=None
    print('Obtaining values...')
    pathsValues = pathValues(pathsPositions)
    pathsPositions=None
    print('Summing values...')
    sumPaths = sumPaths(pathsValues)
    pathsValues=None
    print('Calculating highest value...')
    return max(sumPaths)

##data = 'triangleio.txt'
##maxPath = findMaxPath(data)
##print(maxPath)

                
def buildTree(data):
    '''
    This builds a list of nodes out of a row tree. Each node contains
    information about its value, row, position in the row, and its
    left- and right-side children. Because each node contains all of this
    information, it is not necessary to store them in lists of rows.     
    '''
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
            
##nodes = buildTree(tree)
##
##pathNumbers = []
##for path in paths:
##    newPath = []
##    for index, mov in enumerate(path):
##        for node in nodes:
##            possibleTargets = []
##            if node['row'] == index:
##                possibleTargetValue = node[mov]
##                possibleTargets.append(possibleTargetValue)
##            for node in possibleTargets:
##                try:
##                    if node['position'] == newPath[-1]['position']:
##                        newPath.append(node)
##                except IndexError:
##                    newPath.append(node)
##        pathNumbers.append(newPath)
##
##pathValues = []
##for path in pathNumbers:
##    newPath = ''
##    for node in path:
##        value = tree[node['row']][node['position']]
##        newPath += str(value)
##    pathValues.append(newPath)

##for path in pathValues:
##    print(path)
                
        
    



    
    




