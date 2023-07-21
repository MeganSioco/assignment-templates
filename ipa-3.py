'''Individual Programming Assignment 3

70 points

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    ##takes the value of the dictionary of member's name
    fr = social_graph[from_member]
    to = social_graph[to_member]
    
    ##flags
    follower = 0
    followed_by = 0
    
    ##take the following lists
    frlist = fr["following"]
    tolist = to["following"]
    
    ##check if follower
    for name in frlist:
        if name == to_member:
            follower = 1
            break
    
    ##check if followed by
    for name in tolist:
        if name == from_member:
            followed_by = 1
            break
    
    if follower and followed_by:
        return "friends"
    elif follower == 1 and followed_by == 0:
        return "follower"
    elif follower == 0 and followed_by == 1:
        return "followed by"
    else:
        return "no relationship"


def tic_tac_toe(board):
    '''Tic Tac Toe.
    25 points.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    ##flag for if there is a winner or not
    flag = 0 #no winner for now and turns 1 if there is a winner
    
    ##check horizontally (rows)
    for row in board:
        row_flag = 0 #to check if all symbols are the same
        for i in range(1, len(row)):
            if row[i-1] == row[i]:
                row_flag += 1
        if row_flag == len(row)-1:
            flag = 1
            return row[0]
    
    ##check vertically (columns)
    column = list(zip(*board))
    for col in column:
        setlen = len(set(col))
        if setlen == 1:
            flag = 1
            return col[0]
    

    ##check diagonally            
    diag1 = []
    diag2 = []
    i = 0
    j = -1
    for row in board:
        diag1.append(row[i])
        diag2.append(row[j])
        i += 1
        j -= 1
    if len(set(diag1)) == 1:
        flag = 1
        return diag1[0]
    if len(set(diag2)) == 1:
        flag = 1
        return diag2[0]
    
    #if none matches or no one wins
    if flag == 0:
        return "NO WINNER"

def eta(first_stop, second_stop, route_map):
    '''ETA.
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    route = list(route_map.keys())
    #get the route from first to second stop
    first_stop_index = 0
    second_stop_index = 0
    index = 0
    for place in route:
        if place[0] == first_stop:
            first_stop_index = index
        elif place[1] == second_stop:
            second_stop_index = index
        index += 1
    
    ##we make a new route where it only goes from first to second stoop
    ##we add 1 because for example [0:3] it will only be 0-2
    new_route = route[first_stop_index : second_stop_index + 1]
    
    ##since we already have the new route, we just need to add the time
    time = 0
    for stops in new_route:
        dic = route_map[stops]
        time += dic['travel_time_mins']
    
    return time
