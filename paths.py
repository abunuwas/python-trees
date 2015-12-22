"""
##### Unfinished module ######
The functions in this module provide utilities to build all possible paths
in a tree. The paths can later be used to navigate the tree and perform
operations with its nodes. 
This procedure is highly inefficient when the tree is very big, so it is
recommended to use these functions only with small trees.
The module outlines four approaches to building the paths of a tree, using
different data structures in Python, namely with lists (buildPaths),
dictionaries (buildPaths2), and strings (buildPaths3). The buildPath4 function
is a not yet successful attempt at using the multiprocessing library for this
task.
The functions transPathsPositions, pathValues use the data returned by any
of the previous functions to find the values in the tree of each of the
movements in the path. transPathsPositions expects an iterable object as input. 
"""

import multiprocessing
import time

def buildPaths(tree):
    '''
    This function finds all possible paths in a tree.
    The tree must be passed as an argument in the ffoorm of a list of lists.
    Every sub-list or row must contain individual elements, i.e. a single
    string with all the elements in the row is not valid. 
    '''
    print('Initializing function buildPaths...')
    numberPaths = 2**(len(tree)-1) # Calculates the number of paths. This only works for balanced trees in which every node has exactly two children.
    print('Number of paths expected: ', numberPaths)
    start = time.time()
    paths = []
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
    while len(paths) < numberPaths:
        if len(paths) == 0:
            for mov in movs:
                paths[e] = mov
                e += 1
        else:
            newPaths = {}
            j=0
            for i in range(e):
                for mov in movs:
                    newPaths[j] = paths[i] + mov
                    j += 1
            paths = newPaths
            e = j
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
    while len(paths.split('-')) < numberPaths:
        if len(paths) == 0:
            for mov in movs:
                paths += '-'+mov
        else:
            newPaths = ''
            paths = paths.split('-')[1:]
            for path in paths:
                for mov in movs:
                    newPaths += '-'+path+mov
            paths = newPaths
    end = time.time()-start
    print('Time to complete buildpaths3 (strings): ', end)
    return paths

##output = multiprocessing.Queue()
##def buildInnerPaths(paths, output):
##    print('building inner paths...')
##    newPaths = ''
##    k = 0
##    for path in paths:
##        for mov in movs:
##            newPaths += '-'+path+mov
##            k += 1
##    print(newPaths)
##    output.put(newPaths, k)
##
##def buildPaths4(tree):
##    '''
##    This function finds all possible paths in a tree.
##    The tree must be passed as an argument in the form of a list of lists.
##    Every sub-list or row must contain individual elements, i.e. a single
##    string with all the elements in the row is not valid. 
##    '''
##    paths = ''
##    numberPaths = 2**(len(tree)-1) # Calculates the number of paths. This only works for balanced trees in which every node has exactly two children.
##    print(numberPaths)
##    movs = ('L', 'R')
##    while len(paths.split('-')) < numberPaths:
##        if len(paths) == 0:
##            for mov in movs:
##                paths += '-'+mov
##        else:
##            paths = paths.split('-')[1:]
##            middle = int(len(paths)/2)
##            paths = [paths[:middle][0], paths[middle:][0]]
##            print(paths)
##            jobs = []
##            for path in paths:
##                process = multiprocessing.Process(target=buildInnerPaths,
##                                                     args=(path, output))
##                jobs.append(process)
##            print('starting processes...')
##            for z in jobs:
##                z.start()
##            for z in jobs:
##                z.join()
##            results = [output.get() for p in jobs]
##            print(results)
##            paths = newPaths
##
##    return paths


def transPathsPositions(paths):
    '''
    Translates the outcome returned by the buildPaths function into a list
    of movements, in which every movement is a tuple where the first value
    represents the row and the second value represents the position in the row. 
    '''
    pathsPositions = []
    for path in paths:
        translatedPath = [(0, 0)]
        position = 0
        for index, mov in enumerate(path):
            if mov == 'L':
                position = position
                translatedPath.append((index+1, position))
            else:
                position = position+1
                translatedPath.append((index+1, position))
        pathsPositions.append((path, translatedPath))

    return pathsPositions


def pathValues(pathsPositions, tree):
    '''
    This function builds the paths with their corresponding values, based
    on the information about the row and position values of every movement
    as provided by the transPathsPositions function. This function basically
    serves to check that we're considering all possible paths in the tree. 
    '''
    pathsValues = []
    for path, translatedPath in pathsPositions:
        pathValue=[]
        for row, position in translatedPath:
            pathValue.append(tree[row][position])
        pathsValues.append((path, pathValue))

    return pathsValues
    

def sumPaths(pathsValues):
    '''
    Sums up the values of the nodes in each path. 
    '''
    return [(sum(pathValue), path) for path, pathValue in pathsValues]


def findMaxPath(tree):
    '''
    Returns the path which yields the highest value in the tree. 
    '''
    paths = buildPaths(tree)
    pathsPositions = transPathsPositions(paths)
    pathsValues = pathValues(pathsPositions, tree)
    sumOfPaths = sumPaths(pathsValues)
    valueMaxPath = max(sumOfPaths)
    return valueMaxPath

