#! /usr/bin/python

## Homework 2
## Aditya Dhulipala

from collections import namedtuple
from helper import read_input
from minimax import *

weights = [[99, -8, 8, 6, 6, 8, -8, 99], [-8, -24, -4, -3, -3, -4, -24, -8], [8, -4, 7, 4, 4, 7, -4, 8], [6, -3, 4, 0, 0, 4, -3, 6], [6, -3, 4, 0, 0, 4, -3, 6], [8, -4, 7, 4, 4, 7, -4, 8], [-8, -24, -4, -3, -3, -4, -24, -8], [99, -8, 8, 6, 6, 8, -8, 99]]
st = [['*', '*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', 'O', 'X', '*', '*', '*'], ['*', '*', '*', 'X', 'O', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*', '*']]



#
s = [['*', '*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', 'O', '*', '*', '*', '*'], ['*', '*', '*', 'O', '*', '*', '*', '*'], ['*', '*', '*', 'O', 'X', '*', '*', '*'], ['*', '*', '*', 'X', 'O', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*', '*']]
a = [(1, 2), (4, 5), (5, 4), (3, 2), (0, 3)]
#

pl = 'X'

   
def alpha_beta(state, player):
    pass

[task, player, cut_off_depth, state] = read_input()

print 'started....try minimax_decision(s, "X", 1)'




s1 = [

['*', '*', '*', '*', 'O', '*', '*', '*'],
['*', '*', '*', 'O', 'O', '*', '*', '*'],
['*', '*', '*', 'O', 'O', '*', '*', '*'],
['*', '*', '*', 'O', 'O', '*', '*', '*'],
['*', '*', '*', 'X', 'O', '*', '*', '*'],
['*', '*', '*', '*', '*', '*', '*', '*'],
['*', '*', '*', '*', '*', '*', '*', '*'],
['*', '*', '*', '*', '*', '*', '*', '*']

]
s2 = [

['*', '*', '*', '*', '*', '*', '*', '*'],
['*', '*', '*', 'O', 'X', '*', '*', '*'],
['*', '*', '*', 'O', 'X', '*', '*', '*'],
['*', '*', '*', 'O', 'X', '*', '*', '*'],
['*', '*', '*', 'X', 'O', '*', '*', '*'],
['*', '*', '*', '*', '*', '*', '*', '*'],
['*', '*', '*', '*', '*', '*', '*', '*'],
['*', '*', '*', '*', '*', '*', '*', '*']

]
s3 = [

['*', '*', '*', '*', 'X', '*', '*', '*'],
['*', '*', '*', 'O', 'O', '*', '*', '*'],
['*', '*', '*', 'O', 'O', '*', '*', '*'],
['*', '*', '*', 'O', 'O', '*', '*', '*'],
['*', '*', '*', 'X', 'O', '*', '*', '*'],
['*', '*', '*', '*', '*', '*', '*', '*'],
['*', '*', '*', '*', '*', '*', '*', '*'],
['*', '*', '*', '*', '*', '*', '*', '*']

]

s4 = [
['*', '*', '*', '*', '*', '*', '*', '*'],
['*', 'O', 'O', 'O', 'O', 'O', 'O', '*'],
['*', 'O', 'O', 'O', 'O', 'O', 'O', '*'],
['*', 'O', 'O', 'X', 'X', 'O', 'O', '*'],
['*', 'O', 'O', 'X', 'X', 'O', 'O', '*'],
['*', 'O', 'O', 'O', 'O', 'O', 'O', '*'],
['*', 'O', 'O', 'O', 'O', 'O', 'O', '*'],
['*', '*', '*', '*', '*', '*', '*', '*']
]

# test
print "--END--", '\n','\n'
print 'line num 83 test fn'
acts = get_actions (s4, 'X')

from collections import defaultdict

d = {}
for a in acts:
    newstate = result(s4, 'X', a)
    u = utility(newstate, 'X')
    d[a] = u
    #print utility(result(s4, 'X', a), 'X')
    #print '\n -- action -- end -- '

