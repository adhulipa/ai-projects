## Homework 2
# Aditya
# MiniMax

from helper import *

weights = [[99, -8, 8, 6, 6, 8, -8, 99], [-8, -24, -4, -3, -3, -4, -24, -8], [8, -4, 7, 4, 4, 7, -4, 8], [6, -3, 4, 0, 0, 4, -3, 6], [6, -3, 4, 0, 0, 4, -3, 6], [8, -4, 7, 4, 4, 7, -4, 8], [-8, -24, -4, -3, -3, -4, -24, -8], [99, -8, 8, 6, 6, 8, -8, 99]]

# Remeber: Format of action = (i, j)
# (i, j) = (1,2) , (3, 4) etc
# i = number
# j = letter
# if   a = (i,j)
# then x = ascii_lowercase[a[1]] + str(a[0])
# now x = 'd2', 'c3' etc (add +1 to num to get 1-index based repr)
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

def cutoff(state, cut_off_depth, current_depth):
    if current_depth == cut_off_depth:
        return True
    else:
        return False

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
        if r:
            pass
            #print 'success for ', flip_each_way
    return state_copy

def max_val(state, current_depth, cut_off_depth):
    global MAX_PLAYER
    print MAX_PLAYER, 'max pla'
    if cutoff(state, cut_off_depth, current_depth):
        # Since we've reached the cutoff,
        # whatever state was passed here
        # was passed from the min_player
        # HENCE - Return untility for MIN_PLAYER
        return utility(state, MIN_PLAYER)
    v = -float('inf')
    actions = get_actions(state, MAX_PLAYER) # TODO: figure out how to pass player  val
    for a in actions:
        v = max(v, min_val(result(state, MAX_PLAYER, a), current_depth+1, cut_off_depth))
    return v

def min_val(state, current_depth, cut_off_depth):
    global MIN_PLAYER
    print MIN_PLAYER, 'min pl'

    if cutoff(state, cut_off_depth, current_depth):
        # Since we've reached the cutoff,
        # whatever state was passed here
        # was passed from the max_player
        # HENCE - Return untility for MAX_PLAYER
        return utility(state, MAX_PLAYER) 
    v = float('inf')
    actions = get_actions(state, MIN_PLAYER) # TODO: figure out how to pass player  val
    for a in actions:
        v = min(v, max_val(result(state, MIN_PLAYER, a), current_depth+1, cut_off_depth))
    return v


def minimax_decision(state, player, cut_off_depth):

    print player, 'root pla, max pl'
    global MAX_PLAYER, MIN_PLAYER
    
    MAX_PLAYER = player
    MIN_PLAYER = get_opp(player)
    
    actions = get_actions(state, player)
    tmp = {}
    start_depth = 1
    for a in actions:
        tmp[a] = min_val(result(state, MAX_PLAYER, a), start_depth, cut_off_depth)
    print 'tmp= ', tmp
    
    return tmp[max(tmp)]
 
