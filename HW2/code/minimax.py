## Homework 2
# Aditya
# MiniMax

from helper import *


# Remmeber: Format of action = (i, j)
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
    return actions

def cutoff(state, depth):
    global cut_off_depth
    if depth == cut_off_depth:
        return True
    else:
        return False

def result(state, player, action):
    state = state[:]
    print 'TODO result --> state, player, action = ', state, player, action

def max_val(state):
    if cutoff(state, depth):
        return utility(state)
    v = -float('inf')
    actions = get_actions(state, player_TODO) # TODO: figure out how to pass player  val
    for a in actions:
        v = max(v, min_val(result(state, a)))
    return v

def min_val(state):
    if cutoff(state, depth):
        return utility(state)
    v = float('inf')
    actions = get_actions(state, player_TODO) # TODO: figure out how to pass player  val
    for a in actions:
        v = min(v, max_val(result(state, a)))
    return v


def minimax_decision(state, player):
    actions = get_actions(state, player)
    tmp = {}
    for a in actions:
        tmp[min_val(result(state, player, a))] = a
    return tmp[max(tmp)]
 
