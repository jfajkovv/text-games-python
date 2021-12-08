####
###
### General utilities.
###
####

def ask_int_in_range(user_query, range_bottom, range_top):
    '''Returns an integer (as an answer to a question).'''

    reply = None
    while reply not in range(range_bottom, range_top + 1):
        reply = int(input('\t' + user_query))
    return reply


def ask_yes_no(user_query):
    '''Returns a "y" or "n" (as an answer to a question).'''

    reply = None
    while reply not in ('y', 'n'):
        reply = input('\t' + user_query).lower()
    return reply
