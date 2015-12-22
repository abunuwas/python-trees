'''
This module provides functions to calcualte the path that yields the highest value
in a tree. The approach used here is to calculate, for every node, the value of the
sum of all their children-nodes in the tree, down to the base of the tree.
Graphically this is like dividing the tree into different areas which spring
from every node, which is the reason why the function which performs this task is
called sumArea. To perform this task, the function calls itself recursively once
per row. This works fine with trees of moderate size, but due to the maximum
recursion depth limit in Python, the function will not work with large trees. I will
start working soon on a new implementation that uses a different approach, like
iteration or decorators. 
'''

import time

from generate_trees import generateTree, getFromFile, getTree
from nodes import buildTreeUpDown
from paths import findMaxPath


def sumArea(nodes, node, initialValue):
    '''
    Calcualtes the sum of the value of all the children-nodes which spring from
    a given node. Grahpically, this is like calculating the value of an area of the
    tree, which is why this function is called sumArea. The function returns the value
    of this sum.
    ### WARNING ### This function is recursive, which means that, due to the maximum
    recursion depth of Python, it can only be applied to trees of moderate size.
    Big trees cause stack overflow and yield a RuntimeError. I will work soon on a new
    implementation that uses iteration or decorators to overcome this problem. 
    '''
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
        area = sumArea(nodes, set(children), initialValue)
        return area


def maxValuePath(nodes, node, highestPath):
    '''
    This function applies the sumArea function to all nodes in every row of the tree,
    to find out which yields the highest value. Iterating over all of the rows in
    the tree until the last row, the function finds which is the path that yields
    the highest value in the tree, and returns a list containing a reference to
    the key value in the tree-dictionary of every node included in the path. 
    '''
    leftChild = nodes[node]['L']
    rightChild = nodes[node]['R']
    children = [leftChild, rightChild]
    if None in children:
        return highestPath
    else:
        nextStep = []
        for child in children:
            area = sumArea(nodes, [child], 0)
            nextStep.append((area, child))
        highestValueStep = max(nextStep)[1]
        highestPath.append(highestValueStep)
        path = maxValuePath(nodes, highestValueStep, highestPath)
        return path


    

def walkPath(nodes, path):
    """
    This function can be used to walk a tree in the form returned by the
    buildTreeUpDown function from the ndoes module, i.e. in dictionary form.
    The path must be in the form of 'LRRL', where each letter indicates which
    child-node is next (L: left, R: right). The function returns a list of
    tuples, where the first member of each tuple is the key of the node in the
    tree-dictionary, and the second member its value in the tree.
    For a tree with 5 rows, the function can be called like this:
    path = walkPath(nodes, 'LRRL')
    """
    pathValues = []
    keys = list(nodes.keys())
    head = keys[0]
    previousMove = (head, nodes[head]['value'])
    pathValues.append(previousMove)
    for mov in path:
        currentMoveIndex = nodes[previousMove[0]][mov]
        currentMoveValue = nodes[currentMoveIndex]['value']
        previousMove = (currentMoveIndex, currentMoveValue)
        pathValues.append(previousMove)
    return pathValues


def checkPrintTree(tree, flag):
    if flag == 'yes':
        for line in tree:
            print(tree)
    elif flag == 'no':
        pass
    else: raise('Please provide a valid flag for this parameter.')

def getHighestPathValue(nodes, highestPath):
    path = [nodes[node]['value'] for node in highestPath]
    pathValue = sum(path)
    return pathValue

def getHighestPathAndPathValue(tree):
    nodes = buildTreeUpDown(tree)
    highestPath = maxValuePath(nodes, 1, [1])
    pathValue = getHighestPathValue(nodes, highestPath)
    return highestPath, pathValue

def findMaxValuePath(tree='random', size=5, printTree='no', fileName=None):
    """
    Returns the path which yields the highest value in a tree as a list, in which each
    member is an index that references the key value of the node in the tree. It also
    returns the sum of the nodes in that path.
    By default, it takes a small tree of 5 rows which is randomly generated, and
    returns its highest value path, together with the value of the nodes in that path.

    Parameters:
    ----------
    tree: set to 'random' by default, in which case the function builds a random tree.
          I you wish to pass in a specific tree, be sure it accords to one of the
          following data structures:
          1) A dictionary in which each element contains the following five properties:
             'value', 'position', 'row', 'L', 'R', as returned by the functions
             buildTreeUpDown and buildTreeGroundUp.
          2) A lists of lists, in which each sub-list is a row of the tree. Each row
             must be a list in which each member of the list is a float.
          3) A file name, which must be a string with extension .txt. The file must
             contain data representing a tree, with one row per line in the file, and
             numbers in each row separated by a single space. 

    size: in case you wish the function to work with a randomly generated tree, you
          can specify here how many rows you want the tree to have. Parameter must be
          int. Random: 5.

    printTree: in case you wish the function to work with a randomly generated tree,
               you can choose to print the tree to the interactive prompt or the
               standard output by setting this flat to 'yes'. Not recommended for big trees.

    fileName: in case you wish the function to work with a randomly generated tree, you
              can choose to save the tree data in a file, whose name (and if so desired,
              path) must be provided here as a string. The recommended file extension is
              .txt.     
    """

    if tree == 'random':
        
        if fileName:
            tree = generateTree(size, toFile='toFile', fileName=fileName)
            checkPrintTree(tree, printTree)
            highestPath, pathValue = getHighestPathAndPathValue

        elif fileName is None:
            tree = generateTree(size)
            checkPrintTree(tree, printTree)
            highestPath, pathValue = getHighestPathAndPathValue(tree)

        else: raise TypeError(fileName,
                              'Please provide a valid file name and extension.')

    properties = ['value',
                  'position',
                  'row',
                  'L',
                  'R'
                  ]
    if (isinstance(tree, dict) and [node.__contains__(pro)
                                     for key, node in tree.items()
                                     for pro in properties]):
        nodes = tree
        highestPath = maxValuePath(nodes, 1, [1])
        pathValue = getHighestPathValue(nodes, highestPath)

    elif isinstance(tree, str) and tree.endswith('.txt'):
        rawTree = getFromFile(tree)
        tree = getTree(rawTree)
        highestPath, pathValue = getHighestPathAndPathValue(tree)

    elif ([isinstance(row, list) 
           for row in tree]
          and [isinstance(num, float)
               for row in tree
               for num in row]):
        highestPath, pathValue = getHighestPathAndPathValue(tree)

    else: raise TypeError(tree, 'Plase provide a valid data structure.')

    return highestPath, pathValue

    



                
 
