####
###
### General utilities.
###
####

def ask_int_in_range(question, low, high):
    '''Returns an integer (as an answer to a question).'''

    reply = None
    while reply not in range(low, high):
        reply = int(input('\t' + q))
    return reply
