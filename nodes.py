
def buildTreeGroundUp(tree):
    '''
    This function takes as input a tree in the form of a list of lists, in which each row
    is a list where every element is an independent member of the list. The function returns a
    dictionary of nodes from the tree. Because it is a dictionary, nodes are not stored in any
    particular order, and cannot be accesed by index. However, every node in the tree can be
    found with precision via its properties in the dictionary, in particular 'row' and
    'position' (this refers to its index in the row, starting from index 0). This function
    builds the tree from the ground up, so it is necessary to pass in an inverted tree as
    an argument. 
    '''
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


def buildTreeUpDown(tree):
    '''
    This function takes as input a tree in the form of a list of lists, in which each row
    is a list where every element is an independent member of the list. The function returns a
    dictionary of nodes from the tree. Because it is a dictionary, nodes are not stored in any
    particular order, and cannot be accesed by index. However, every node in the tree can be
    found with precision via its properties in the dictionary, in particular 'row' and
    'position' (this refers to its index in the row, starting from index 0). This function builds
    from the up, namely from its head, down. 
    '''
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


def checkCorrectednessTree(nodes):
    '''
    This function takes as input any of the tree-data structures returned by the buildTreeUpDown
    or the buildTreeGroundUp functions and, for each node in the tree, it prints their left-
    and right-hand children. This basically serves to ensure that the functions are working
    properly. 
    '''
    for key, node in nodes.items():
        value = node['value']
        try:
            L = nodes[node['L']]['value']
            R = nodes[node['R']]['value']
        except KeyError:
            L = R = 'None'
        print('Value: {}. L: {}; R: {}.'.format(value, L, R))
        
