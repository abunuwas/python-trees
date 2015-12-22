"""
This module contains examples of how to use the functions in this library. 
"""

from find_max_value_path import findMaxValuePath
from generate_trees import generateTree
from nodes import buildTreeUpDown
from paths import findMaxPath

## Generate randomly a tree of 100 rows and save it to a file called
## 'random-tree.txt':
bigTree = generateTree(100, toFile='toFile', fileName='random-tree.txt')

## Convert the tree into a dictionary of nodes:
nodes = buildTreeUpDown(bigTree)

## Find the path in that three that yields the highest value:
highestPath, pathValue = findMaxValuePath(nodes)
print(highestPath, pathValue)

## Find the path that yields the highest value in a randomly generated tree
## of 10 rows:
highestPath, pathValue = findMaxValuePath(size=10)
print(highestPath, pathValue)

## Load a tree from a file and find the path in that tree that yields the
## highest value: 
highestPath, pathValue = findMaxValuePath('random-tree.txt')
print(highestPath, pathValue)

#### The following code snippet illustrates how to use the functions from the
#### paths module: 
smallTree = generateTree(5)
valueMaxPath, path = findMaxPath(smallTree)
print(valueMaxPath)
for p in path:
    print(p)

