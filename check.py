import multiprocessing
import time

tree = [
    [1],
    [2, 3],
    [4, 5, 6],
    [7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [40, 50, 100, 2, 1, 0]
     ]


tree2 = reversed(tree)

def getTree(file):
    rawData = open(file, 'r', encoding='utf-8').read().splitlines()

    tree=[]
    for line in rawData:
        tree.append([float(num) for num in line.split()])
    return tree

data = 'triangle.txt'
tree = getTree(data)

def buildTreeGroundUp(tree):
    nodes = {}
    nodeCounter = 0
    justAdded=[]
    to_add = []
    for index, line in enumerate(tree):
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
                        nodes[nodeCounter]['L'] = node
                        
                    elif nodes[node]['position'] == position+1 and nodes[node]['row'] == index-1:
                        nodes[nodeCounter]['R'] = node
                adding.append(nodeCounter)

        justAdded = set(adding)

    return nodes

def checkCorrectednessTree(nodes):
    for key, node in nodes.items():
        value = node['value']
        try:
            L = nodes[node['L']]['value']
            R = nodes[node['R']]['value']
        except KeyError:
            L = R = 'None'
        print('Value: {}. L: {}; R: {}.'.format(value, L, R))

def buildTreeUpDown(tree):
    nodes = {}
    nodeCounter = 0
    justAdded=[]
    to_add = []
    for index, line in enumerate(tree):
        adding=[]
        for position, value in enumerate(line):
            if index == 0:
                nodeCounter += 1
                nodes[nodeCounter] = {'value': value,
                               'row': index,
                               'position': position}
                adding.append(nodeCounter)
            else:
                nodeCounter += 1
                nodes[nodeCounter] = {'value': value,
                                      'row': index,
                                      'position': position}
                for node in justAdded:
                    if position == nodes[node]['position']:
                        nodes[node]['L'] = nodeCounter

                    if position == nodes[node]['position']+1:
                        nodes[node]['R'] = nodeCounter
                if index == len(tree)-1: nodes[nodeCounter].update({'L': None, 'R': None})
                adding.append(nodeCounter)

        justAdded = set(adding)

    return nodes

nodes = buildTreeUpDown(tree)
##checkCorrectednessTree(nodes)

def sumArea(node, initialValue): 
    currentNodes = [nodes[n]['value'] for n in node]
    initialValue += sum(currentNodes)
    children = []
    for n in node:
        leftChild = nodes[n]['L']
        rightChild = nodes[n]['R']
        children.append(leftChild)
        children.append(rightChild)
    children = set(children)
    if None in children:
        return initialValue
    else:
        area = sumArea(set(children), initialValue)
        return area


def maxValuePath(node, highestPath):
    leftChild = nodes[node]['L']
    rightChild = nodes[node]['R']
    children = [leftChild, rightChild]
    if None in children:
        return highestPath
    else:
        nextStep = []
        for child in children:
            area = sumArea([child], 0)
            nextStep.append((area, child))
        highestValueStep = max(nextStep)[1]
        highestPath.append(highestValueStep)
        path = maxValuePath(highestValueStep, highestPath)
        return path
    

highestPath = maxValuePath(1, [1])
print(highestPath)
path = [nodes[node]['value'] for node in highestPath]
print(path)
print(sum(path))



##path = 'LRRL'
##
##keys = list(nodes.keys())
##head = keys[0]
##previousMove = (head, nodes[head]['value'])
##print(previousMove[1])
##for mov in path:
##    currentMoveIndex = nodes[previousMove[0]][mov]
##    currentMoveValue = nodes[currentMoveIndex]['value']
##    previousMove = (currentMoveIndex, currentMoveValue)
##    print(mov, previousMove[1])
    



def buildPaths(tree):
    '''
    This function finds all possible paths in a tree.
    The tree must be passed as an argument in the form of a list of lists.
    Every sub-list or row must contain individual elements, i.e. a single
    string with all the elements in the row is not valid. 
    '''
    print('Initializing function buildPaths...')
    start = time.time()
    paths = []
    numberPaths = 2**(len(tree)-1) # Calculates the number of paths. This only works for balanced trees in which every node has exactly two children. 
    print('Number of paths expected: ', numberPaths)
    movs = ('L', 'R')
    k=0
    while len(paths) < numberPaths:
        if len(paths) == 0:
            for mov in movs:
                paths.append(mov)
                k+=1
        else:
            newPaths = []
            for path in paths:
                for mov in movs:
                    newPaths.append(path+mov)
                    k+=1
            paths = newPaths

        print(k)
        print('time to compute this iteation: ', time.time()-start)

    end = time.time()-start
    print('Time to complete buildPaths (lists): ', end)
    return paths

def buildPaths2(tree):
    '''
    This function finds all possible paths in a tree.
    The tree must be passed as an argument in the form of a list of lists.
    Every sub-list or row must contain individual elements, i.e. a single
    string with all the elements in the row is not valid. 
    '''
    print('\n\nInitializing buildPaths2...')
    start = time.time()
    paths = {}
    numberPaths = 2**(len(tree)-1) # Calculates the number of paths. This only works for balanced trees in which every node has exactly two children.
    print('Number of paths expected: ', numberPaths)
    movs = ('L', 'R')
    e=0
    k=0
    while len(paths) < numberPaths:
        if len(paths) == 0:
            for mov in movs:
                paths[e] = mov
                e += 1
                k += 1
        else:
            newPaths = {}
            j=0
            for i in range(e):
                for mov in movs:
                    newPaths[j] = paths[i] + mov
                    j += 1
                    k += 1
            paths = newPaths
            e = j

        print(k)
        print('time to compute this iteation: ', time.time()-start)

    end = time.time()-start
    print('Time to complete buildPaths2 (dictionaries): ', end)
    return paths


def buildPaths3(tree):
    '''
    This function finds all possible paths in a tree.
    The tree must be passed as an argument in the form of a list of lists.
    Every sub-list or row must contain individual elements, i.e. a single
    string with all the elements in the row is not valid. 
    '''
    print('\n\nInitializing buildPaths3...')
    start = time.time()
    paths = ''
    numberPaths = 2**(len(tree)-1) # Calculates the number of paths. This only works for balanced trees in which every node has exactly two children.
    print('Number of paths expected: ', numberPaths)
    movs = ('L', 'R')
    k=0
    while len(paths.split('-')) < numberPaths:
        if len(paths) == 0:
            for mov in movs:
                paths += '-'+mov
                k += 1
        else:
            newPaths = ''
            paths = paths.split('-')[1:]
            for path in paths:
                for mov in movs:
                    newPaths += '-'+path+mov
                    k += 1
            paths = newPaths

        print(k)
        print('time to compute this iteation: ', time.time()-start)

    end = time.time()-start
    print('Time to complete buildpaths3 (strings): ', end)
    return paths

output = multiprocessing.Queue()
def buildInnerPaths(paths, output):
    print('building inner paths...')
    newPaths = ''
    k = 0
    for path in paths:
        for mov in movs:
            newPaths += '-'+path+mov
            k += 1
    print(newPaths)
    output.put(newPaths, k)

def buildPaths4(tree):
    '''
    This function finds all possible paths in a tree.
    The tree must be passed as an argument in the form of a list of lists.
    Every sub-list or row must contain individual elements, i.e. a single
    string with all the elements in the row is not valid. 
    '''
    paths = ''
    numberPaths = 2**(len(tree)-1) # Calculates the number of paths. This only works for balanced trees in which every node has exactly two children.
    print(numberPaths)
    movs = ('L', 'R')
    k=0
    while len(paths.split('-')) < numberPaths:
        if len(paths) == 0:
            for mov in movs:
                paths += '-'+mov
                k += 1
        else:
            paths = paths.split('-')[1:]
            middle = int(len(paths)/2)
            paths = [paths[:middle][0], paths[middle:][0]]
            print(paths)
            jobs = []
            for path in paths:
                process = multiprocessing.Process(target=buildInnerPaths,
                                                     args=(path, output))
                jobs.append(process)
            print('starting processes...')
            for z in jobs:
                z.start()
            for z in jobs:
                z.join()
            results = [output.get() for p in jobs]
            print(results)
            paths = newPaths

        print(k)

    print(k)

    return paths

#633825300114114700748351602688
#16777214
##print('Building paths...')
##paths = buildPaths(tree)
##file = open('triangle-nodes.txt', 'w', encoding='utf-8')
##file.write(str(paths))
##file.close()
##paths = buildPaths2(tree)
##paths = buildPaths3(tree).split('-')[1:]
####paths = paths.split('-')[1]
##print(len(paths))
####for path in paths:
####    print(path)

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

##def findMaxPath(data):
##    print('Building tree...')
##    tree = getTree(data)
##    print('Building paths...')
##    paths = buildPaths(tree)
##    tree=None
##    print('Obtaining positions...')
##    pathsPositions = transPathsPositions(paths)
##    paths=None
##    print('Obtaining values...')
##    pathsValues = pathValues(pathsPositions)
##    pathsPositions=None
##    print('Summing values...')
##    sumPaths = sumPaths(pathsValues)
##    pathsValues=None
##    print('Calculating highest value...')
##    return max(sumPaths)
##
##
##maxPath = findMaxPath(data)
##print(maxPath)

                
 
