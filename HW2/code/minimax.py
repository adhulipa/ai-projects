## Homework 2
# Aditya
# MiniMax

from helper import *

weights = [[99, -8, 8, 6, 6, 8, -8, 99], [-8, -24, -4, -3, -3, -4, -24, -8], [8, -4, 7, 4, 4, 7, -4, 8], [6, -3, 4, 0, 0, 4, -3, 6], [6, -3, 4, 0, 0, 4, -3, 6], [8, -4, 7, 4, 4, 7, -4, 8], [-8, -24, -4, -3, -3, -4, -24, -8], [99, -8, 8, 6, 6, 8, -8, 99]]

def cutoff(state, cut_off_depth, current_depth):
    if current_depth >= cut_off_depth:
        return True
    else:
        return False

def get_actions(state, player):
    actions = set()
    # TODO: Write cleaner API
    # get_pos() is not necessary
    pos = get_pos(state, player)
    actions = get_moves_for_pos(state, player, pos)
    # TODO: maybe return actions after sort() - to ensure traverse order = positional order
    actions = list(actions)
    actions.sort()
    return actions

def utility(state, player):
    opp = get_opp(player)

    modifier = {}
    modifier[player] = +1
    modifier[opp] = -1

    util = 0
    
    for i in xrange(8):
        for j in xrange(8):
            if state[i][j] != '*':
                util += modifier[state[i][j]] * weights[i][j]
                
    return util

def make_copy(some_state):
    copy = [['null' for i in xrange(8)] for j in xrange(8)]
    for row in xrange(8):
        for col in xrange(8):
            copy[row][col] = some_state[row][col]
    return copy

def result(state, player, action):
    state_copy = make_copy(state)
    directs = [flip_down, flip_downleft, flip_downright, flip_left,
               flip_right, flip_up, flip_upleft, flip_upright]
    for flip_each_way in directs:
        #print flip_each_way, 'for action', action
        r = flip_each_way(state_copy, player, action)
##        if r:
##            pass
##            #print 'success for ', flip_each_way
    return state_copy

def print_formatted(node, depth, value):
    global log
    if value == float('inf'):
        value = 'Infinity'
    elif value == -float('inf'):
        value = '-Infinity'

    print str(node) + ',' + str(depth) + ',' + str(value)
    log.append(str(node) + ',' + str(depth) + ',' + str(value))


def update_node_vals(node, val, which):
    val1 = val
    val2 = value_of_node[node]
    if abs(val1) == float('inf') or abs(val2) == float('inf'):
        which = 'force_update'
    if which == 'force_update':
        value_of_node[node] = val
    elif which == 'keep_min':
        value_of_node[node] = min(val1,val2)
    elif which == 'keep_max':
        value_of_node[node] = max(val1,val2)

def terminal(state):
    min_a = get_actions(state, MIN_PLAYER)
    max_a = get_actions(state, MAX_PLAYER)

    if len(min_a) == 0 and len(max_a) == 0:
        return True
    else:
        return False
   
def max_val(state, current_depth, cut_off_depth, calling_action):
    global MAX_PLAYER
    global value_of_node

    if terminal(state):
        value_of_node[calling_action] = utility(state, MIN_PLAYER)
        print_formatted( pa(calling_action),current_depth,value_of_node[calling_action])
        return utility(state, MAX_PLAYER)
    
    if calling_action not in value_of_node:
        value_of_node[calling_action] = -float('inf')
    if (current_depth < cut_off_depth):
        print_formatted( pa(calling_action),current_depth,value_of_node[calling_action])

    if cutoff(state, cut_off_depth, current_depth):
        util_max = utility(result(state, MAX_PLAYER, calling_action), MAX_PLAYER) 
        update_node_vals(calling_action, util_max, 'keep_min')
        print_formatted( pa(calling_action),current_depth,value_of_node[calling_action])
        return utility(state, MIN_PLAYER)
    v = -float('inf')
    actions = get_actions(state, MAX_PLAYER)
    for a in actions:
        new_val = min_val(result(state, MAX_PLAYER, a), current_depth+1, cut_off_depth, a)
        value_of_node[calling_action] = max(value_of_node[calling_action],value_of_node[a])
        print_formatted( pa(calling_action),current_depth,value_of_node[calling_action])
        v = max(v, new_val)
    return v

def min_val(state, current_depth, cut_off_depth, calling_action):
    global MIN_PLAYER
    global value_of_node

    if terminal(state):
        value_of_node[calling_action] = utility(state, MAX_PLAYER)
        print_formatted( pa(calling_action),current_depth,value_of_node[calling_action])
        return utility(state, MIN_PLAYER)
    
    if calling_action not in value_of_node:
        value_of_node[calling_action] = float('inf')

    if current_depth < cut_off_depth:
        print_formatted( pa(calling_action),current_depth,value_of_node[calling_action])
    
    if cutoff(state, cut_off_depth, current_depth) or terminal(state):
        util_min = utility(result(state, MIN_PLAYER, calling_action), MIN_PLAYER)
        update_node_vals(calling_action, util_min, 'keep_max')
        print_formatted( pa(calling_action),current_depth,value_of_node[calling_action])
        return utility(state, MAX_PLAYER)
    
    v = float('inf')
    actions = get_actions(state, MIN_PLAYER)
    for a in actions:
        new_val = max_val(result(state, MIN_PLAYER, a), current_depth+1, cut_off_depth, a)
        value_of_node[calling_action] = min(value_of_node[calling_action],value_of_node[a])
        print_formatted( pa(calling_action),current_depth,value_of_node[calling_action])
        v = min(v, new_val)
    return v

def minimax_decision(state, player, cut_off_depth):
#### Uncomment to output to file
##    import sys
##    import os
##    
##    f = open('traverse.log', 'w')
##    sys.stdout = f

    global MAX_PLAYER, MIN_PLAYER
    global value_of_node
    global log

    log = []
    log.append( 'Node,Depth,Value')
    log.append( 'Root,0,-Infinity')
    
    value_of_node = {'root':-float('inf')}

    MAX_PLAYER = player
    MIN_PLAYER = get_opp(player)
    
    actions = get_actions(state, MAX_PLAYER)
    tmp = {}
    start_depth = 1

    for a in actions:
        tmp[a] = min_val(result(state, MAX_PLAYER, a), start_depth, cut_off_depth, a)
        value_of_node['root'] = max(value_of_node['root'],value_of_node[a])
        print 'root,0,' + str(value_of_node['root'])
        log.append('root,0,' + str(value_of_node['root']))
        
    rootval = value_of_node['root']
    choices = [child for child in actions if
               value_of_node[child] == rootval]
    choices.sort()
    result_state = result(state, player, choices[0])
    
##    f.close()
##    sys.stdout = sys.__stdout__
##
##    with open('traverse.log', 'r') as f:
##        traverse_log = f.readlines()
   # os.remove('traverse.log')
    return [make_copy(result_state), log[:], choices[:], dict(value_of_node)]
    # uncomment if return necessary
    #return value_of_node['root']
 
