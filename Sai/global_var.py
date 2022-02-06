def init():
    global ai_colour
    ai_colour = 'black' #default cpu colour
    global player_colour
    player_colour = 'white' #default player colour
    global game_running
    game_running = False
    # track num of expected stones in game:
    global b_exp
    b_exp = 0
    global w_exp
    w_exp = 0
    # tack prev captured num of stones
    global b_prev
    b_prev = 0
    global w_prev
    w_prev = 0
    # track turn number
    global turn
    turn = 0
    global status
    status = 'default'
    # unique name for each game's sgf
    global sgf_name
    sgf_name = ''
    global game_date
    game_date = ''
    global p_engine