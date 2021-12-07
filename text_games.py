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


def ask_yes_no(question):
    '''Returns a "y" or "n" (as an answer to a question).'''

    reply = None
    while reply not in ('y', 'n'):
        reply = input('\t' + q).lower()
    return reply
